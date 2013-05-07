'''
Created on May 6, 2013

@author: TheZen
'''

import sys

def movements(size):
    
    #Make the grid and initialize it
    #The ones are need for the border cases
    grid = [[1]*(size+1)]*(size+1)
    
    #start from the bottom right corner, up to the starting corner
    for i in xrange(size-1, -1,-1):
        for j in xrange(size -1, -1,-1):
            grid[i][j] = grid[i+1][j] + grid[i][j+1]
            
    return grid[0][0] #The result is stored in the start corner


print movements(4)