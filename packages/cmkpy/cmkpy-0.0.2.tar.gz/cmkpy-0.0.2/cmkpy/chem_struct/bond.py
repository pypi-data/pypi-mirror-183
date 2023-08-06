#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/11/26 20:19
# @Author  : zhangbc0315@outlook.com
# @File    : bond.py
# @Software: PyCharm

from enum import Enum


class BondType(Enum):

    UNSPECIFIED = 0
    SINGLE = 1
    DOUBLE = 2
    TRIPLE = 3
    QUADRUPLE = 4
    QUINTUPLE = 5
    HEXTUPLE = 6
    ONEANDAHALF = 7
    TWOANDAHALF = 8
    THREEANDAHALF = 9
    FOURANDAHALF = 10
    FIVEANDAHALF = 11
    DATIVEONE = 12
    DATIVE = 13
    DATIVEL = 14
    DATIVER = 15
    AROMATIC = 16,
    IONIC = 17,
    ZERO = 18


class BondDir(Enum):

    NONE = 0
    BEGIN_WEDGE = 1
    BEGIN_DASH = 2
    END_DOWNRIGHT = 3
    END_UPRIGHT = 4
    EITHER_DOUBLE = 5
    ANY = 6


class BondStereo(Enum):

    NONE = 0
    Z = 1
    E = 2
    CIS = 3
    TRANS = 4
    ANY = 5


class Bond:

    symbol_to_bond_type = {':': BondType.AROMATIC,
                           '=': BondType.DOUBLE,
                           '#': BondType.TRIPLE,
                           '->': BondType.DATIVER,
                           '<-': BondType.DATIVEL}
    symbol_to_bond_dir = {'\\': BondDir.END_DOWNRIGHT,
                          '\\\\': BondDir.END_DOWNRIGHT,
                          '/': BondDir.END_UPRIGHT}

    def __init__(self, bond_type: BondType):
        self._idx: int = 0
        self._bond_type: BondType = bond_type if bond_type is not None else BondType.UNSPECIFIED
        self._bond_dir: BondDir = BondDir.NONE
        self._bond_stereo: BondStereo = BondStereo.NONE

    @classmethod
    def init_from_symbol(cls, symbol):
        bond = Bond(cls.symbol_to_bond_type.get(symbol))
        return bond

    @classmethod
    def init_from_dir_symbol(cls, dir_symbol):
        bond = Bond(BondType.UNSPECIFIED)
        bond.bond_dir = cls.symbol_to_bond_dir.get(dir_symbol)
        return bond

    def __repr__(self):
        return str(self.bond_type)

    # region ===== bond_type =====
    @property
    def bond_type(self):
        return self._bond_type

    @bond_type.setter
    def bond_type(self, value):
        self._bond_type = value
    # endregion

    # region ===== bond_dir =====
    @property
    def bond_dir(self):
        return self._bond_dir

    @bond_dir.setter
    def bond_dir(self, value):
        self._bond_dir = value if value is not None else BondDir.NONE
    # endregion

    # region ===== bond_stereo =====
    @property
    def bond_stereo(self):
        return self._bond_stereo

    @bond_stereo.setter
    def bond_stereo(self, value):
        self._bond_stereo = value
    # endregion


if __name__ == "__main__":
    pass
