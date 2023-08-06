#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/11/18 19:27
# @Author  : zhangbc0315@outlook.com
# @File    : periodic_table.py
# @Software: PyCharm

import os
from collections import namedtuple

AtomicData = namedtuple('AtomicData', ['atomic_num',
                                       'symbol',
                                       'radius_covalent',
                                       'radius_b0',
                                       'radius_vdw',
                                       'mass',
                                       'num_out_shell_electrons',
                                       'most_common_isotope',
                                       'mass_most_common_isotope',
                                       'valences',
                                       'electrons',
                                       'electron_negativity'])


class PeriodicTable:

    _periodic_table = None

    def __init__(self):
        self.data_list = []
        self.symbol_to_atomic_num = {}
        self._load_data()

    @classmethod
    def get_instance(cls):
        if cls._periodic_table is None:
            cls._periodic_table = PeriodicTable()
        return cls._periodic_table

    def get_symbol_with_atomic_num(self, atomic_num: int) -> str:
        atomic_data = self.get_atomic_data_with_atomic_num(atomic_num)
        return atomic_data.symbol

    def get_atomic_num_with_symbol(self, symbol: str) -> int:
        return self.symbol_to_atomic_num.get(symbol)

    def get_valences_with_atomic_num(self, atomic_num: int) -> [int]:
        atomic_data = self.get_atomic_data_with_atomic_num(atomic_num)
        return atomic_data.valences

    def get_atomic_data_with_atomic_num(self, atomic_num: int) -> AtomicData:
        return self.data_list[atomic_num]

    def get_num_out_shell_electrons_with_atomic_num(self, atomic_num: int) -> int:
        return self.data_list[atomic_num].num_out_shell_electrons

    def get_atomic_data_with_symbol(self, symbol: str) -> AtomicData:
        return self.get_atomic_data_with_atomic_num(self.symbol_to_atomic_num[symbol])

    def _load_data(self):
        fp = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'resource/periodic_data.tsv')
        idx_to_col = None
        with open(fp, 'r', encoding='utf-8')as f:
            for n, line in enumerate(f.readlines()):
                line = line.strip('\n')
                if len(line) == 0:
                    continue
                if n == 0:
                    idx_to_col = self._get_idx_to_col(line)
                else:
                    values = line.split('\t')
                    data = {col: values[idx] for idx, col in idx_to_col.items()}
                    atomic_data = self._get_atomic_data(data)
                    self.symbol_to_atomic_num[atomic_data.symbol] = atomic_data.atomic_num
                    if atomic_data.atomic_num + 1 == len(self.data_list):
                        continue
                    self.data_list.append(atomic_data)

    @staticmethod
    def _get_idx_to_col(line) -> {str, int}:
        cols = line.split('\t')
        return {idx: col for idx, col in enumerate(cols)}

    @staticmethod
    def _get_atomic_data(data: {str, str}) -> AtomicData:
        for col, val in data.items():
            if col == 'atomic_num':
                data[col] = int(val)
            elif col == 'symbol':
                data[col] = val
            elif col == 'radius_covalent':
                data[col] = float(val)
            elif col == 'radius_b0':
                data[col] = float(val)
            elif col == 'radius_vdw':
                data[col] = float(val)
            elif col == 'mass':
                data[col] = float(val)
            elif col == 'num_out_shell_electrons':
                data[col] = int(val)
            elif col == 'most_common_isotope':
                data[col] = int(val)
            elif col == 'mass_most_common_isotope':
                data[col] = float(val)
            elif col == 'valences':
                data[col] = [int(v) for v in val.split(',')]
            elif col == 'electron_negativity':
                data[col] = float(val)
        return AtomicData(**data)


if __name__ == "__main__":
    pt = PeriodicTable.get_instance()
