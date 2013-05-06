'''
Created on May 6, 2013

@author: TheZen
'''

import sys
def fibonacci(n):
    if(n == 0):
        print 0
    a =0
    b =1
    for i in xrange(1, n):
        c = a + b
        a = b
        b = c
    print b

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test:
        fibonacci(int(test))
        

test_cases.close()