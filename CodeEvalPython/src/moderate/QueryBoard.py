'''
Created on May 8, 2013

@author: Victor J
'''
import sys


class Board(object):
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.board = [[0] * c] * r

    def setcol(self, cmd):
        j, x = self.getargs(cmd)
        for lis in self.board:
            lis[j] = x

    def setrow(self, cmd):
        i, x = self.getargs(cmd)
        self.board[i] = [x] * self.c

    def queryrow(self, cmd):
        row = int(cmd[1])
        print sum(self.board[row])
    def querycol(self, cmd):
        col = int(cmd[1])
        s = 0
        for lis in self.board:
            s += lis[col]
        print s
    def getargs(self, cmd):
        return map(int, cmd[1:])
b = Board(256,256)
tests = open(sys.argv[1], 'r')
# tests = open('n', 'r')
for test in tests:
    if test:
        cmd = map(str.strip,test.split())
        getattr(b,cmd[0].lower())(cmd)
tests.close()