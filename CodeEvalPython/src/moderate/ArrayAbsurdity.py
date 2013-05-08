'''
Created on May 7, 2013

@author: Victor J
'''
import sys
from collections import OrderedDict

def doIt(test):
    arg = map(str.strip, test.split(';'))
    if len(arg) < 2:
        return
    
    arg = map(str.strip, arg[1].split(','))
    s = set(arg)
    print sum(arg) - sum(s)

def sum(iterable):
    return reduce(lambda x, y: int(x) + int(y), iterable)


tests = open(sys.argv[1], 'r')
for test in tests:
    if test:
       doIt(test)
tests.close()

#doIt("20;0,1,10,3,2,4,5,7,6,8,11,9,15,12,13,4,16,18,17,14")


