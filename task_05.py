#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A BP project"""

MYINPUT = raw_input('What is your blood pressure? ')
MYINPUT = int(MYINPUT)
#BP_STATUS = ()


if MYINPUT <= 89:
    print 'low'

if MYINPUT >= 90 or MYINPUT <= 119:
        print 'Ideal'
if MYINPUT >= 120 or MYINPUT <= 130:
            print 'Warning'
            
#if MYINPUT >= 140 or MYINPUT <= 159:

                #elif:
                    #print 'Emergency'

OUTPUT = ' Your status is currently:{}'.format(BP_STATUS)
print OUTPUT
