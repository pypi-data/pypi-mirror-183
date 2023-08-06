#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/11/30 22:11
# @Author  : zhangbc0315@outlook.com
# @File    : smiles_yacc.py
# @Software: PyCharm

from typing import Optional

from ply import yacc

from cmkpy.chem_struct.smiles.smiles_lex import tokens
from cmkpy.chem_struct.atom import Atom, AtomChiral
from cmkpy.chem_struct.bond import Bond, BondType
from cmkpy.chem_struct.mol import Mol


def SmilesYacc():

    # region ===== Begin =====
    # 'C***'
    def p_atom(p):
        """expression : ATOM"""
        mol = Mol()
        atom = p[1]
        mol.add_atom(atom)
        p[0] = [mol]
        set_activate_atom(atom)

    # '[C***'
    def p_atom_after_square(p):
        """expression : LSQUARE ATOM"""
        mol = Mol()
        atom = p[2]
        mol.add_atom(atom)
        p[0] = [mol]
        set_activate_atom(atom)

    # '[H***'
    def p_h_atom_after_square(p):
        """expression : LSQUARE ATOM_H"""
        mol = Mol()
        atom = Atom(1)
        mol.add_atom(atom)
        p[0] = [mol]
        set_activate_atom(atom)

    # '(C***'
    def p_atom_after_paren(p):
        """expression : LPAREN ATOM"""
        nonlocal num_lparen
        num_lparen += 1
        mol = Mol()
        atom = p[2]
        mol.add_atom(atom)
        p[0] = [mol]
        set_activate_atom(atom)

    # '([C***'
    def p_atom_after_square_after_paren(p):
        """expression : LPAREN LSQUARE ATOM"""
        nonlocal num_lparen
        num_lparen += 1
        mol = Mol()
        atom = p[3]
        mol.add_atom(atom)
        p[0] = [mol]
        set_activate_atom(atom)

    # '([H***'
    def p_atom_h_after_square_after_paren(p):
        """expression : LPAREN LSQUARE ATOM_H"""
        nonlocal num_lparen
        num_lparen += 1
        mol = Mol()
        atom = Atom(1)
        mol.add_atom(atom)
        p[0] = [mol]
        set_activate_atom(atom)
    # endregion

    # region ===== DOT =====
    def p_dot(p):
        """expression : expression DOT"""
        nonlocal activate_link_atom
        nonlocal activate_prop_atom
        activate_link_atom = None
        activate_prop_atom = None
        p[0] = p[1]
        if num_lparen == 0:
            mol = Mol()
            p[0].append(mol)
        elif num_lparen > 0:
            pass
        else:
            raise ValueError("括号不匹配, 出现类似这样的情况: (***)).***")
    # endregion

    # region ===== Charge =====
    def p_charge(p):
        """expression : expression CHARGE"""
        nonlocal activate_prop_atom
        p[0] = p[1]
        activate_prop_atom.charge = p[2]
    # endregion

    # region ===== Chiral =====
    def p_cw_chiral(p):
        """expression : expression AT AT"""
        nonlocal activate_prop_atom
        p[0] = p[1]
        activate_prop_atom.chiral =AtomChiral.TETRAHEDRAL_CW
    # endregion

    # region ===== Chiral =====
    def p_ccw_chiral(p):
        """expression : expression AT"""
        nonlocal activate_prop_atom
        p[0] = p[1]
        activate_prop_atom.chiral = AtomChiral.TETRAHEDRAL_CCW
    # endregion

    # region ===== Bond =====
    def p_bond(p):
        """expression : expression BOND"""
        nonlocal current_bond
        p[0] = p[1]
        current_bond = p[2]

    def p_bond_atom(p):
        """expression : expression ATOM"""
        nonlocal activate_link_atom
        nonlocal current_bond
        p[0] = p[1]
        atom = p[2]
        p[0][-1].add_atom(atom)
        if activate_link_atom is not None:
            add_bond(p[0][-1], activate_link_atom, atom)
        set_activate_atom(atom)
        current_bond = Bond(BondType.UNSPECIFIED)

    def p_bond_many_h(p):
        """expression : expression ATOM_H NUM"""
        nonlocal activate_link_atom
        p[0] = p[1]
        activate_link_atom.num_explicit_hs = p[3]
        activate_link_atom.implicit_valence = p[3]

    def p_bond_one_h(p):
        """expression : expression ATOM_H"""
        nonlocal activate_link_atom
        p[0] = p[1]
        activate_link_atom.num_explicit_hs = 1
        activate_link_atom.implicit_valence = 1
    # endregion

    # region ===== Paren =====
    def p_begin_paren(p):
        """expression : expression LPAREN"""
        nonlocal branch_atoms
        nonlocal activate_link_atom
        nonlocal num_lparen
        branch_atoms.append(activate_link_atom)
        p[0] = p[1]
        num_lparen += 1

    def p_end_paren(p):
        """expression : expression RPAREN"""
        nonlocal branch_atoms
        nonlocal activate_link_atom
        nonlocal num_lparen
        if len(branch_atoms) > 0:
            set_activate_atom(branch_atoms[-1])
            branch_atoms.pop(-1)
        p[0] = p[1]
        num_lparen -= 1
    # endregion

    # region ===== Map Num =====
    def p_map_num(p):
        """expression : expression MAP_NUM"""
        nonlocal activate_prop_atom
        p[0] = p[1]
        activate_prop_atom.map_num = p[2]
    # endregion

    # region ===== Cycle =====
    def p_complex_cycle_num(p):
        """expression : expression CYCLE_NUM"""
        nonlocal activate_link_atom
        nonlocal cycle_nums_atoms
        p[0] = p[1]
        cycle_num = p[2]
        if cycle_num not in cycle_nums_atoms.keys():
            cycle_nums_atoms[cycle_num] = activate_link_atom
        else:
            add_bond(p[0][-1], activate_link_atom, cycle_nums_atoms[cycle_num])
            cycle_nums_atoms.pop(cycle_num)

    def p_simple_cycle_num(p):
        """expression : expression NUM"""
        nonlocal activate_link_atom
        nonlocal cycle_nums_atoms
        nonlocal current_bond
        p[0] = p[1]
        cycle_nums = [int(n) for n in str(p[2])]
        for cycle_num in cycle_nums:
            if cycle_num not in cycle_nums_atoms.keys():
                cycle_nums_atoms[cycle_num] = activate_link_atom
            else:
                add_bond(p[0][-1], activate_link_atom, cycle_nums_atoms[cycle_num])
                cycle_nums_atoms.pop(cycle_num)

    # endregion

    # region ===== Square, Colon =====
    def p_only_square(p):
        """expression : expression RSQUARE
                      | expression LSQUARE"""
        p[0] = p[1]

    def p_colon(p):
        """expression : expression COLON"""
        p[0] = p[1]
    # endregion

    def set_activate_atom(atom: Atom):
        nonlocal activate_link_atom
        nonlocal activate_prop_atom
        activate_link_atom = atom
        activate_prop_atom = atom

    def add_bond(mol: Mol, begin_atom: Atom, end_atom: Atom):
        nonlocal current_bond
        mol.add_bond_between_atom_idxes(current_bond, begin_atom.idx, end_atom.idx)
        current_bond = Bond(BondType.UNSPECIFIED)

    activate_link_atom: Optional[Atom] = None
    activate_prop_atom: Optional[Atom] = None
    branch_atoms: [Atom] = []
    current_bond: Bond = Bond(BondType.UNSPECIFIED)
    cycle_nums_atoms = {}
    num_lparen = 0
    return yacc.yacc()


if __name__ == "__main__":
    pass
