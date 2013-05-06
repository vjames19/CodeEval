'''
Created on May 6, 2013

@author: Victor J.
'''

import sys
import re

def removeCharacters(test):
    args = map(str.strip, test.split(','))
    return re.sub('[%s]' % args[1], '', args[0])
    
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        print removeCharacters(test) 

test_cases.close()

