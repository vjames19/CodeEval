'''
Created on May 7, 2013

@author: Victor J
'''
import sys


def doIt(test):
    test = test.strip()
    left = "([{"
    right = ")]}"
    stack = []
    for p in test:
        if p in left:
            stack.append(p)
        elif len(stack) == 0 or left.index(stack[-1]) != right.index(p):
            print False
            return
        else:
            stack.pop()
    
    print len(stack) == 0

tests = open(sys.argv[1], 'r')
for test in tests:
    if test:
       doIt(test)
tests.close()



