#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/12/1 14:51
# @Author  : zhangbc0315@outlook.com
# @File    : chem_base.py
# @Software: PyCharm


class ChemBase:

    def __init__(self):
        self._temp_props = {}

    # region ===== props =====
    @property
    def temp_props(self):
        return self._temp_props

    @temp_props.setter
    def temp_props(self, value):
        self._temp_props = value
    # endregion

    # region ===== add/del/query/change =====

    def add_temp_prop(self, key: str, value):
        self._temp_props[key] = value

    def get_temp_prop(self, key: str):
        return self._temp_props.get(key)

    # endregion


if __name__ == "__main__":
    pass
