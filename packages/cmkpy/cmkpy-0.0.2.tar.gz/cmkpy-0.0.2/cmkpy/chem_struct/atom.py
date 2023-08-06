#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/11/26 20:19
# @Author  : zhangbc0315@outlook.com
# @File    : atom.py
# @Software: PyCharm

from enum import Enum

from cmkpy.chem_data import PeriodicTable, AtomicData


class AtomChiral(Enum):

    UNSPECIFIED = 0
    TETRAHEDRAL_CW = 1
    TETRAHEDRAL_CCW = 2
    ANY = 3


class Atom:

    def __init__(self, atomic_num: int):
        self._idx = 0
        self._symbol = None
        self._atomic_num = atomic_num
        self._is_aromatic = False
        self._is_explicit = False
        self._num_explicit_hs = 0
        self._num_implicit_hs = 0
        self._chiral = AtomChiral.UNSPECIFIED

    @classmethod
    def init_from_symbol(cls, symbol: str):
        is_aromatic = False
        if symbol.islower():
            symbol = symbol.title()
            is_aromatic = True

        atomic_num = PeriodicTable.get_instance().get_atomic_num_with_symbol(symbol)
        if atomic_num is None:
            atomic_num = 0

        atom = Atom(atomic_num)
        atom.is_aromatic = is_aromatic and atomic_num != 0
        atom.symbol = symbol
        return atom

    def __repr__(self):
        return self.symbol

    # region ===== idx =====
    @property
    def idx(self):
        return self._idx

    @idx.setter
    def idx(self, value):
        self._idx = value
    # endregion

    # region ===== symbol =====
    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value
    # endregion

    # region ===== is_aromatic =====
    @property
    def is_aromatic(self):
        return self._is_aromatic

    @is_aromatic.setter
    def is_aromatic(self, value):
        self._is_aromatic = value
    # endregion

    # region ===== is_explicit =====
    @property
    def is_explicit(self):
        return self._is_explicit

    @is_explicit.setter
    def is_explicit(self, value):
        self._is_explicit = value
    # endregion

    # region ===== chiral =====
    @property
    def chiral(self):
        return self._chiral

    @chiral.setter
    def chiral(self, value):
        self._chiral = value
    # endregion

    def get_atomic_data(self) -> AtomicData:
        return PeriodicTable.get_instance().get_atomic_data_with_atomic_num(self._atomic_num)


if __name__ == "__main__":
    pass
