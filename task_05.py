#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A BP project"""

MYINPUT = raw_input('What is your blood pressure? ')
MYINPUT= int(MYINPUT)
BP_STATUS = ('Low')


if MYINPUT <= 89:
    print BP_STATUS

    if MYINPUT >=90 or MYINPUT <=119:
        print BP_STATUS       
else:
        print 'Emergency'
    
    

OUTPUT = ' Your status is currently:{}'.format(BP_STATUS)
print OUTPUT


