'''
Created on May 8, 2013

@author: Victor J
'''
import sys

tests = open(sys.argv[1], 'r')
# tests = open("n", 'r')
n = int(tests.readline())
lines = map(str.strip,tests.readlines())
lines.sort(key = lambda x:len(x), reverse= True)
lines = lines[:n if n <= len(lines) else len(lines)]
for line in lines:
    if line:
        print line



