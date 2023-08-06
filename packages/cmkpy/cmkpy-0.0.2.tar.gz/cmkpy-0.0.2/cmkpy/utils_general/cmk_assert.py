#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/6/2 21:29
# @Author  : zhangbc0315@outlook.com
# @File    : cmk_assert.py
# @Software: PyCharm

import logging


class CMKAssert:

    @staticmethod
    def assert_equal(value1, value2, msg):
        if value1 != value2:
            logging.error(msg)
            raise ValueError(msg)

    @staticmethod
    def assert_true(expr, msg):
        if not expr:
            logging.error(msg)
            raise ValueError(msg)

    @staticmethod
    def assert_false(expr, msg):
        if expr:
            logging.error(msg)
            raise ValueError(msg)


if __name__ == "__main__":
    pass
