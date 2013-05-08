'''
Created on May 7, 2013

@author: TheZen
'''
import sys

tests = open(sys.argv[1], 'r')
for test in tests:
    if test:
        print reduce(lambda x,y: int(x)+ int(y), test.strip())

tests.close()