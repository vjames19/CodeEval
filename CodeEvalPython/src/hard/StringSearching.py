'''
Created on May 6, 2013

@author: Victor J
'''

import sys
import re
tests = open(sys.argv[1], 'r')
for test in tests:
    if test:
        a = map(str.strip,test.split(','))
        if re.search(a[1],a[0]):
            print 'true'
        else:
            print 'false'

tests.close()

