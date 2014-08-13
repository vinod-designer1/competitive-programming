#!/bin/python
def nextMove(n,r,c,grid):
    princF = False
    princP = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'p':
                princP = [i,j]
                princF = True
                break
        if princF:
            break
    move = ''
    if r == princP[0]:
        if c > princP[1]:
            move = 'RIGHT'
        else:
            move = 'LEFT'
    else:
        if r > princP[0]:
            move = 'DOWN'
        else:
            move = 'UP'
                
    return move
n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)
