
import random, sys
import math

import tile
from helper import *

GRIDSIZE = 11

SETTLER = 'S'
WARRIOR = 'W'
sx, sy = None, None
wx, wy = None, None

# create (small) map

# assumed within starting range: 2 different luxuries, 1 horses, 1 iron

# even gridrows will have an indent -> hexagonal
grid = [[random.random() for i in range(GRIDSIZE)] for j in range(GRIDSIZE)]

def set_visibility(x, y, n, hill=False, prev=None):
    if not prev:
        grid[y][x].visible = True
        for xn, yn in neighbours(x, y):
            if not (xn < 0 or xn > GRIDSIZE-1 or yn < 0 or yn > GRIDSIZE-1):
                grid[yn][xn].visible = True
    elif not prev.blocks_sight() or hill:
        grid[y][x].visible = True
    if n > 0:
        for xn, yn in neighbours(x, y):
            if not (xn < 0 or xn > GRIDSIZE-1 or yn < 0 or yn > GRIDSIZE-1):
                if not prev or not ((grid[y][x].hill and grid[y][x].forest) or isinstance(grid[y][x], tile.Mountain)):
                    set_visibility(xn, yn, n-1, hill, grid[y][x])
    #elif n == 0:
        # show mountains/hills beyond vision range that are higher than tiles in path of vision
    #    for xn, yn in neighbours(x, y):
    #        if not (xn < 0 or xn > GRIDSIZE-1 or yn < 0 or yn > GRIDSIZE-1):
    #            t = grid[yn][xn]
    #            if t.hill and not (isinstance(grid[y][x], tile.Mountain) or grid[y][x].hill or grid[y][x].forest):
    #               t.visible = True
    #            if isinstance(t, tile.Mountain) and not (isinstance(grid[y][x], tile.Mountain) or grid[y][x].hill):
    #                t.visible = True

for g in grid:
    for i in range(len(g)):
        if g[i] < 0.3: 
            g[i] = tile.Grassland()
        elif g[i] < 0.4: 
            g[i] = tile.Grassland()
            g[i].set_forest()
        elif g[i] < 0.45: 
            g[i] = tile.Grassland()
            g[i].set_hill()
        elif g[i] < 0.5: 
            g[i] = tile.Grassland()
            g[i].set_hill()
            g[i].set_forest()
        elif g[i] < 0.7: 
            g[i] = tile.Plain()
        elif g[i] < 0.8: 
            g[i] = tile.Plain()
            g[i].set_forest()
        elif g[i] < 0.85: 
            g[i] = tile.Plain()
            g[i].set_hill()
        elif g[i] < 0.9: 
            g[i] = tile.Plain()
            g[i].set_hill()
            g[i].set_forest()
        else: 
            g[i] = tile.Mountain()

# create settler, warrior
sx = int(math.ceil(GRIDSIZE/2))
sy = sx
if isinstance(grid[sy][sx], tile.Mountain):
    grid[sy][sx] = tile.Grassland()
grid[sy][sx].occupant = SETTLER
set_visibility(sx, sy, 2, grid[sy][sx].hill)

wx,wy = random.choice(neighbours(sx, sy))
if isinstance(grid[wy][wx], tile.Mountain):
    grid[wy][wx] = tile.Grassland()
grid[wy][wx].occupant = WARRIOR
set_visibility(wx, wy, 2, grid[wy][wx].hill)

print_map(grid)

# determine moves, where to settle
inp = ''
while(not inp.upper() in ['NW','NE','W','E','SW','SE']):
    inp = raw_input("Move Warrior: ")

x,y = eval(inp.upper() + '(' + str(wx) + ',' + str(wy) + ')')
grid[y][x].occupant = WARRIOR
grid[wy][wx].occupant = None
wx, wy = x, y
set_visibility(wx, wy, 2, grid[wy][wx].hill)

print_map(grid)

if not grid[wy][wx].blocks_sight():
    inp = ''
    while(not inp.upper() in ['NW','NE','W','E','SW','SE']):
        inp = raw_input("Move Warrior: ")

    x,y = eval(inp.upper() + '(' + str(wx) + ',' + str(wy) + ')')
    grid[y][x].occupant = WARRIOR
    grid[wy][wx].occupant = None
    wx, wy = x, y
    set_visibility(wx, wy, 2, grid[wy][wx].hill)

    print_map(grid)

inp = ''
while(not inp.upper() in ['NW','NE','W','E','SW','SE']):
    inp = raw_input("Move Settler: ")

x,y = eval(inp.upper() + '(' + str(sx) + ',' + str(sy) + ')')
grid[y][x].occupant = SETTLER
grid[sy][sx].occupant = None
sx, sy = x, y
set_visibility(sx, sy, 2, grid[sy][sx].hill)

print_map(grid)

if not grid[sy][sx].blocks_sight():
    inp = ''
    while(not inp.upper() in ['NW','NE','W','E','SW','SE']):
        inp = raw_input("Move Settler: ")

    x,y = eval(inp.upper() + '(' + str(sx) + ',' + str(sy) + ')')
    grid[y][x].occupant = SETTLER
    grid[sy][sx].occupant = None
    sx, sy = x, y
    set_visibility(sx, sy, 2, grid[sy][sx].hill)

    print_map(grid)








