'''
Created on May 7, 2013

@author: TheZen
'''
import sys
import bisect


def doIt(test):
    args = map(str.strip, test.split(';'))
    ar = map(int, args[0].split(','))
    lo = 1
    pairs = []
    for i in ar:
        x = int(args[1]) - i
        index = bisect.bisect_left(ar, x, lo)
        lo += 1
        if index != len(ar) and ar[index] == x:
            pairs.append("{:d},{:d}".format(i, ar[index]))
    
    if len(pairs) == 0:
        print 'NULL'
    else:
        print ";".join(pairs)

tests = open(sys.argv[1], 'r')
for test in tests:
    if test:
       doIt(test)
tests.close()

#doIt("2,4,5,6,9,11,15;20")