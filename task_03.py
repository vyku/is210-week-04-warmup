#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A complex testcase."""

EXPENSE = 14.23
LOOKS_NICE = True
MAX_EXPENSE = 12
GET_OUT_ALIVE = False

SCRIFICE = LOOKS_NICE or EXPENSE <= MAX_EXPENSE or GET_OUT_ALIVE is False


print SCRIFICE
