'''
Created on May 7, 2013

@author: Victor J
'''
import sys


def doIt(test):
    n = test.strip()
    i = 1
    while True:
        r = n[::-1]
        s = int(n) + int(r)
        if isPalindrome(s):
            print i, s
            break
        i += 1
        n = str(s)

def isPalindrome(n):
    s = str(n)
    return s == s[::-1]

tests = open(sys.argv[1], 'r')
for test in tests:
    if test:
       doIt(test)
tests.close()


