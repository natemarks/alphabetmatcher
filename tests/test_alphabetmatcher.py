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

