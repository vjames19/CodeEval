'''
Created on May 7, 2013

@author: Victor J
'''
import sys
from collections import Counter

def doIt(test):
    freq = Counter(test.strip())
    for i, n in enumerate(test.strip()):
        if freq[str(i)] != int(n):
            print 0
            return
    print 1

tests = open(sys.argv[1], 'r')
for test in tests:
    if test:
       doIt(test)
tests.close()

#doIt("1210")


