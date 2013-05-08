'''
Created on May 7, 2013

@author: Victor J
'''
import sys


def doIt(test):
    words = map(str.strip, test.strip().split())
    print words[-2]

tests = open(sys.argv[1], 'r')
for test in tests:
    if test:
       doIt(test)
tests.close()




