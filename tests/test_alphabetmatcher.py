#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `alphabetmatcher` package."""


import pytest


def test_empty_string():
    from alphabetmatcher.alphabetmatcher import Matcher

    dd = Matcher('')
    assert not dd.success()


def test_exact_match():
    from alphabetmatcher.alphabetmatcher import Matcher

    dd = Matcher('abcdefghijklmnopqrstuvwxyz')
    assert dd.success()

def test_case_mixing():
    from alphabetmatcher.alphabetmatcher import Matcher

    dd = Matcher('abcdefGhijklmnopqrStuvwxyz')
    assert dd.success()

def test_reorder_and_junk():
    from alphabetmatcher.alphabetmatcher import Matcher

    dd = Matcher('CBAhjsvdf734y4tu9820h%$%$&%defGhijklmnopqrStuvwxyz')
    assert dd.success()

def test_repeats():
    from alphabetmatcher.alphabetmatcher import Matcher

    dd = Matcher('aaaaaaaaaabcdefGhijklmnopqrStuvwxyz')
    assert dd.success()
