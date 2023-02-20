#!/usr/bin/env python3

import os
import pytest
import sys
from   time import time

try:
    thisdir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(thisdir, '..'))
except:
    sys.path.append('..')

from spiral import *

inputs = [
    'alllower',
    'ALLUPPER',
    'a_delimiter',
    'a.delimiter',
    'a$delimiter',
    'a:delimiter',
    'a_fooBar',
    'fooBar',
    'FooBar',
    'Foobar',
    'fooBAR',
    'fooBARbif',
    'fooBARzBif',
    'ABCfoo',
    'ABCFoo',
    'ABCFooBar',
    'ABCfooBar',
    'fooBar2day',
    'fooBar2Day',
    'fooBAR2day',
    'fooBAR2Day',
    'foo3000',
    '99foo3000',
    'foo2Bar',
    'foo2bar2',
    'Foo2Bar2',
    'MyInt32',
    'MyInt42',
    'MyInt32Var',
    '2ndvar',
    'the2ndvar',
    'the2ndVar',
    'row10',
    'utf8',
    'aUTF8var',
    'J2SE4me',
    'IPv4addr'
]

expected = {
'pure_camelcase_split': [
    'alllower',
    'ALLUPPER',
    'a_delimiter',
    'a.delimiter',
    'a$delimiter',
    'a:delimiter',
    'a_foo Bar',
    'foo Bar',
    'Foo Bar',
    'Foobar',
    'foo BAR',
    'foo BARbif',
    'foo BARz Bif',
    'ABCfoo',
    'ABCFoo',
    'ABCFoo Bar',
    'ABCfoo Bar',
    'foo Bar2day',
    'foo Bar2Day',
    'foo BAR2day',
    'foo BAR2Day',
    'foo3000',
    '99foo3000',
    'foo2Bar',
    'foo2bar2',
    'Foo2Bar2',
    'My Int32',
    'My Int42',
    'My Int32Var',
    '2ndvar',
    'the2ndvar',
    'the2nd Var',
    'row10',
    'utf8',
    'a UTF8var',
    'J2SE4me',
    'IPv4addr'],

'safe_simple_split': [
    'alllower',
    'ALLUPPER',
    'a delimiter',
    'a delimiter',
    'a delimiter',
    'a delimiter',
    'a foo Bar',
    'foo Bar',
    'Foo Bar',
    'Foobar',
    'fooBAR',
    'fooBARbif',
    'fooBARzBif',
    'ABCfoo',
    'ABCFoo',
    'ABCFooBar',
    'ABCfooBar',
    'foo Bar2day',
    'foo Bar2Day',
    'fooBAR2day',
    'fooBAR2Day',
    'foo3000',
    '99foo3000',
    'foo2Bar',
    'foo2bar2',
    'Foo2Bar2',
    'My Int32',
    'My Int42',
    'My Int32Var',
    '2ndvar',
    'the2ndvar',
    'the2nd Var',
    'row10',
    'utf8',
    'aUTF8var',
    'J2SE4me',
    'IPv4addr'],

'simple_split': [
    'alllower',
    'ALLUPPER',
    'a delimiter',
    'a delimiter',
    'a delimiter',
    'a delimiter',
    'a foo Bar',
    'foo Bar',
    'Foo Bar',
    'Foobar',
    'foo BAR',
    'foo BARbif',
    'foo BARz Bif',
    'ABCfoo',
    'ABCFoo',
    'ABCFoo Bar',
    'ABCfoo Bar',
    'foo Bar2day',
    'foo Bar2Day',
    'foo BAR2day',
    'foo BAR2Day',
    'foo3000',
    '99foo3000',
    'foo2Bar',
    'foo2bar2',
    'Foo2Bar2',
    'My Int32',
    'My Int42',
    'My Int32Var',
    '2ndvar',
    'the2ndvar',
    'the2nd Var',
    'row10',
    'utf8',
    'a UTF8var',
    'J2SE4me',
    'IPv4addr'],

'elementary_split': [
    'alllower',
    'ALLUPPER',
    'a delimiter',
    'a delimiter',
    'a delimiter',
    'a delimiter',
    'a foo Bar',
    'foo Bar',
    'Foo Bar',
    'Foobar',
    'foo BAR',
    'foo BARbif',
    'foo BARz Bif',
    'ABCfoo',
    'ABCFoo',
    'ABCFoo Bar',
    'ABCfoo Bar',
    'foo Bar 2 day',
    'foo Bar 2 Day',
    'foo BAR 2 day',
    'foo BAR 2 Day',
    'foo 3000',
    '99 foo 3000',
    'foo 2 Bar',
    'foo 2 bar 2',
    'Foo 2 Bar 2',
    'My Int 32',
    'My Int 42',
    'My Int 32 Var',
    '2 ndvar',
    'the 2 ndvar',
    'the 2 nd Var',
    'row 10',
    'utf 8',
    'a UTF 8 var',
    'J 2 SE 4 me',
    'IPv 4 addr'],

'heuristic_split': [
    'alllower',
    'ALLUPPER',
    'a delimiter',
    'a delimiter',
    'a delimiter',
    'a delimiter',
    'a foo Bar',
    'foo Bar',
    'Foo Bar',
    'Foobar',
    'foo BAR',
    'foo BARbif',
    'foo BARz Bif',
    'ABCfoo',
    'ABCFoo',
    'ABCFoo Bar',
    'ABCfoo Bar',
    'foo Bar 2 day',
    'foo Bar 2 Day',
    'foo BAR 2 day',
    'foo BAR 2 Day',
    'foo 3000',
    '99 foo 3000',
    'foo 2 Bar',
    'foo 2 bar 2',
    'Foo 2 Bar 2',
    'My Int32',
    'My Int 42',
    'My Int32 Var',
    '2nd var',
    'the 2nd var',
    'the 2nd Var',
    'row 10',
    'utf8',
    'a UTF8 var',
    'J2SE 4 me',
    'IPv4 addr']
}

class TestClass:
    def check(self, splitter):
        for index, case in enumerate(inputs):
            func = getattr(sys.modules['spiral.simple_splitters'], splitter)
            assert ' '.join(func(case)) == expected[splitter][index]

    def test_pure_camelcase_split(self, capsys):
        self.check('pure_camelcase_split')

    def test_safe_simple_split(self, capsys):
        self.check('safe_simple_split')

    def test_simple_split(self, capsys):
        self.check('simple_split')

    def test_elementary_split(self, capsys):
        self.check('elementary_split')

    def test_heuristic_split(self, capsys):
        self.check('heuristic_split')