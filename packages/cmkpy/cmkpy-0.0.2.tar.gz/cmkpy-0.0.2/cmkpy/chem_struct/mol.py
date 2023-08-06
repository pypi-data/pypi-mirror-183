#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/11/26 20:19
# @Author  : zhangbc0315@outlook.com
# @File    : mol.py
# @Software: PyCharm

import networkx as nx

from cmkpy.chem_struct.atom import Atom
from cmkpy.chem_struct.bond import Bond, BondType
from cmkpy.utils_general import CMKAssert


class Mol:

    def __init__(self):
        self._graph = nx.Graph()

    # region ===== Atom =====
    def add_atom(self, atom: Atom) -> int:
        """ 添加原子
        不可重复添加原子

        :param atom: 原子
        :return: 原子 index
        """
        CMKAssert.assert_false(self.is_contain_atom(atom), f"重复添加原子: {atom}")
        atom_idxes = self.get_atom_idxes()
        if len(atom_idxes) == 0:
            atom_idx = 0
        else:
            atom_idx = atom_idxes[-1] + 1
        self._graph.add_node(atom_idx, atom=atom)
        atom.idx = atom_idx
        return atom.idx

    def get_atoms(self) -> [Atom]:
        """ 获得所有原子

        :return: 所有原子
        """
        return list(dict(self._graph.nodes.data('atom')).values())

    def get_num_atoms(self) -> int:
        """ 获得原子数目

        :return: 原子数目
        """
        return len(self._graph.nodes)

    def get_atom_with_idx(self, idx: int) -> Atom:
        """ 获得具有指定 index 的原子

        :param idx: 原子 index
        :return: index
        """
        return self._graph.nodes.data('atom')[idx]

    def is_contain_atom(self, atom: Atom) -> bool:
        """ 是否包含原子

        :param atom: 原子
        :return:
        """
        return atom in self.get_atoms()

    def get_atom_idxes(self) -> [int]:
        return list(self._graph.nodes)

    def get_nbr_atom_idxes(self, atom_idx: int) -> [int]:
        CMKAssert.assert_true(atom_idx in self.get_atom_idxes(), f"分子中未包含原子{atom_idx}")
        return list(self._graph.neighbors(atom_idx))
    # endregion

    # region ===== Bond =====
    def add_bond_by_type_between_atom_idxes(self, bond_type: BondType, begin_aid: int, end_aid: int):
        bond = Bond(bond_type)
        return self.add_bond_between_atom_idxes(bond, begin_aid, end_aid)

    def add_bond_between_atom_idxes(self, bond: Bond, begin_aid: int, end_aid: int):
        CMKAssert.assert_true(begin_aid in self.get_atom_idxes(), f"在分子未包含的原子({begin_aid})间建立键连关系")
        CMKAssert.assert_true(end_aid in self.get_atom_idxes(), f"在分子未包含的原子({end_aid})间建立键连关系")
        CMKAssert.assert_false(begin_aid == end_aid, f"在index相同的原子间建立键连关系")
        CMKAssert.assert_false(bond in self.get_bonds(), f"重复添加键: {bond}")
        CMKAssert.assert_false(self.get_bond_between_atom_idxes(begin_aid, end_aid),
                               f"在原子({begin_aid})与原子({end_aid})间重复添加键")
        bonds = self.get_bonds()
        if len(bonds) == 0:
            bond_idx = 0
        else:
            bond_idx = bonds[-1].idx + 1
        self._graph.add_edge(begin_aid, end_aid, bond=bond, weight=1)
        bond.idx = bond_idx
        return bond.idx

    def get_bonds(self) -> [Bond]:
        return [aab[-1] for aab in self._graph.edges.data('bond')]

    def get_bonds_and_atom_idx_pair(self) -> [(Bond, int, int)]:
        return [(aab[-1], aab[0], aab[1]) for aab in self._graph.edges.data('bond')]

    def get_num_bonds(self) -> int:
        return len(self._graph.edges)

    def get_bond_between_atom_idxes(self, begin_aid: int, end_aid: int):
        data = self._graph.get_edge_data(begin_aid, end_aid, 'bond')
        if isinstance(data, dict):
            return data.get('bond')
        else:
            return None

    def get_bonds_on_atom_idx(self, aid: int) -> [Bond]:
        nbrs = self._graph[aid]
        bonds = []
        for node, edge in nbrs.items():
            bonds.append(edge['bond'])
        return bonds
    # endregion

    # region ===== Fragment =====
    def get_shortest_path(self, begin_atom_idx: int, end_atom_idx: int) -> [int]:
        CMKAssert.assert_true(begin_atom_idx in self.get_atom_idxes(), f"分子中未包含原子{begin_atom_idx}")
        CMKAssert.assert_true(end_atom_idx in self.get_atom_idxes(), f"分子中未包含原子{end_atom_idx}")
        return nx.dijkstra_path(self._graph, begin_atom_idx, end_atom_idx)

    @classmethod
    def _clean_rings(cls, rings: [[int]]) -> [[int]]:
        cleaned_set_rings = []
        cleaned_ids = []
        for i, ring in enumerate(rings):
            if set(ring) not in cleaned_set_rings:
                cleaned_ids.append(i)
                cleaned_set_rings.append(set(ring))
        cleaned_rings = []
        for i in cleaned_ids:
            cleaned_rings.append(rings[i])
        return cleaned_rings

    def get_rings(self) -> [[int]]:
        aids = self.get_atom_idxes()
        if len(aids) <= 2:
            return []
        rings = []
        for bond, aid1, aid2 in self.get_bonds_and_atom_idx_pair():
            self._graph[aid1][aid2]['weight'] = 999999
            sp = self.get_shortest_path(aid1, aid2)
            if len(sp) > 2:
                rings.append(sp)
            self._graph[aid1][aid2]['weight'] = 1
        return self._clean_rings(rings)
    # endregion


if __name__ == "__main__":
    pass
