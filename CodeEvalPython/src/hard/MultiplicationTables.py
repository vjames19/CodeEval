'''
Created on May 7, 2013

@author: TheZen
'''
for i in range(1,13):
    line = ''
    for j in range(1,13):
        line += "{:>4d}".format(i*j)
    print line.strip()
