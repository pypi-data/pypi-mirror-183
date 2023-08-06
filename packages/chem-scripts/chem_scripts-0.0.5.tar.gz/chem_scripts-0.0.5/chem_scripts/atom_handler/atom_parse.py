#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/8/23 10:49
# @Author  : zhangbc0315@outlook.com
# @File    : atom_parse.py
# @Software: PyCharm

from typing import Optional

from rdkit.Chem.AllChem import GetPeriodicTable


class AtomParse:

    @classmethod
    def symbol_to_atomic_num(cls, symbol: str) -> Optional[int]:
        try:
            atomic_num = GetPeriodicTable().GetAtomicNumber(symbol)
            return atomic_num
        except Exception as e:
            return None

    @classmethod
    def atomic_num_to_symbol(cls, atomic_num: int) -> Optional[str]:
        if 1 <= atomic_num <= 118:
            symbol = GetPeriodicTable().GetElementSymbol(atomic_num)
            return symbol
        else:
            return None


if __name__ == "__main__":
    pass
