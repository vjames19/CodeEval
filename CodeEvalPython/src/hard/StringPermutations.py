'''
Created on May 7, 2013

@author: TheZen
'''
import sys

def permute(s):
    res = []
    if len(s) == 1:
        res = [s]
    else:
        for i, c in enumerate(s):
            for perm in permute(s[:i] + s[i+1:]):
                res += [c + perm]

    return res
        
tests = open(sys.argv[1], 'r')
for test in tests:
    if test:
        print ",".join(sorted(permute(test.strip())))

tests.close()

