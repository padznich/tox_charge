#!/usr/bin/env python
# -*- coding: utf-8 -*-


from modules import summator


def test_summator_s1():
    assert summator.s1(2, 3) == 5


def test_summator_s2():
    assert summator.s2(5, 4) == 1
