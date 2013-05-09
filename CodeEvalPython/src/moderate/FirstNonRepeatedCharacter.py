'''
Created on May 8, 2013

@author: Victor J
'''
import sys
from collections import OrderedDict

def doIt(test):
    test = test.strip()
    d = OrderedDict()
    for i in test:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for k,v in d.items():
        if v== 1:
            print k
            return




tests = open(sys.argv[1], 'r')
for test in tests:
    if test:
        doIt(test)
tests.close()


