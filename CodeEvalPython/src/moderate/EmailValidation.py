'''
Created on May 8, 2013

@author: Victor J
'''
import sys
import re

regex = re.compile(r"\w+@\w+\.\w+$")

def doIt(test):
    print 'true' if regex.match(test.strip()) else 'false'


tests = open(sys.argv[1], 'r')
for test in tests:
    if test:
        doIt(test)
tests.close()


