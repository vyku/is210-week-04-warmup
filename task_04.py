#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A single if statement."""

MYINPUT = raw_input('Tell me a story! ')
MAX_LENGTH = 80
LENMAX = len(MYINPUT)
LONGSTR = 'short'


if MYINPUT <= MAX_LENGTH:
    MYINPUT >= LENMAX 
    print LONGSTR
    
   

OUTPUT = 'That certainly was a {} story!'.format(LONGSTR)
print OUTPUT


 
