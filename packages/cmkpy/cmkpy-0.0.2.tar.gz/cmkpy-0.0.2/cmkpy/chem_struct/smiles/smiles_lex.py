#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/11/29 15:19
# @Author  : zhangbc0315@outlook.com
# @File    : smiles_lex.py
# @Software: PyCharm

import logging

from ply import lex

from cmkpy.chem_struct.atom import Atom
from cmkpy.chem_struct.bond import Bond


states = [
    ('inquare', 'inclusive'),
]

tokens = [
    'ATOM', 'ATOM_H', 'BOND',
    'LSQUARE', 'RSQUARE',
    'LPAREN', 'RPAREN',
    'AT', 'DOT', 'COLON',
    'CHARGE', 'MAP_NUM', 'CYCLE_NUM', 'NUM'
]


def SmilesLex():

    t_AT = r'@'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_DOT = r'\.'
    t_inquare_COLON = r'\:'

    r_atom = r'He|' \
             r'Li|Ne|' \
             r'Na|Mg|Al|Si|Cl|Ar|' \
             r'Ca|Sc|Ti|Cr|Mn|Fe|Co|Ni|Cu|Zn|Ga|Ge|As|Se|Br|Kr|' \
             r'Rb|Sr|Zr|Nb|Mo|Tc|Ru|Rh|Pd|Ag|Cd|In|Sn|Sb|Te|Xe|' \
             r'Cs|Ba|La|Ce|Pr|Nd|Pm|Sm|Eu|Gd|Tb|Dy|Ho|Er|Tm|Tb|Lu|Hf|Ta|Re|Os|Ir|Pt|Au|Hg|Tl|Pb|Bi|Po|At|Rn|' \
             r'Fr|Ra|Ac|Th|Pa|U|Np|Pu|Am|Cm|Bk|Cf|Es|Fm|Md|No|Lr|Rf|Db|Sg|Bh|Hs|Mt|Ds|Rg|Cn|Nh|Fl|Mc|Lv|Ts|Og|' \
             r'si|as|se|te|b|c|n|o|p|s|' \
             r'H|B|C|N|O|F|P|S|K|V|Y|I|W'

    @lex.TOKEN(r"\[")
    def t_begin_inquare(t):
        t.lexer.begin('inquare')
        t.type = 'LSQUARE'
        return t

    @lex.TOKEN(r"\]")
    def t_inquare_end(t):
        t.lexer.begin('INITIAL')
        t.type = 'RSQUARE'
        return t

    def t_inquare_ATOM(t):
        r"""[A-Z][a-z]"""
        if t.value == 'H':
            t.type = 'ATOM_H'
        else:
            t.value = Atom.init_from_symbol(t.value)
            t.value.is_explicit = True
        return t

    @lex.TOKEN(r_atom)
    def t_ATOM(t):
        if t.value == 'H':
            t.type = 'ATOM_H'
        else:
            t.value = Atom.init_from_symbol(t.value)
        return t

    def t_BOND(t):
        r"""\:|\=|\#|\<\-|\-\>"""
        t.value = Bond.init_from_symbol(t.value)
        return t

    def t_DIR_BOND(t):
        r"""\\\\|\\|\/"""
        t.value = Bond.init_from_dir_symbol(t.value)
        return t

    def t_CHARGE(t):
        r"""\+\d+|\-\d+|\++|\-+"""
        if len(t.value) == 1:
            t.value = 1 if t.value == '+' else -1
        elif t.value[-1].isdigit():
            t.value = int(t.value)
        else:
            t.value = len(t.value) if t.value[0] == '+' else -len(t.value)
        return t

    def t_CYCLE_NUM(t):
        r"""[0-9]+\%"""
        t.value = int(t.value[:-1])
        return t

    def t_NUM(t):
        r"""[0-9]+"""
        t.value = int(t.value)
        return t

    def t_inquare_MAP_NUM(t):
        r"""\:[0-9]+"""
        t.value = int(t.value[1:])
        return t

    def t_error(t):
        logging.error(f"Syntax error in input in lex {t.value} in {t}")

    return lex.lex(optimize=1, debug=True, lextab='_smileslex')


if __name__ == "__main__":
    pass
    sl = SmilesLex()
    sl.input('H->He<-\\\\[He]\\#H=C')
    for token in sl:
        print(token)
