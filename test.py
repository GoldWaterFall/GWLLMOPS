#!/usr/bin/env-python
# -*- coding: utf-8 -*-
"""
@Time 2025-03-06 5:28
@Author ShiqiDing
@File test.py
"""
from injector import Injector, inject


class A:
    name: str = "llmops"


@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def print(self):
        print(f"Class A name:{self.a.name}")


injector = Injector()
b = injector.get(B)
b.print()
