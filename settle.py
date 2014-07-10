
import random, sys
import math
import tile

GRIDSIZE = 11
ENDC = '\033[0m'
SETTLER = 'S'
WARRIOR = 'W'
sx, sy = None, None
wx, wy = None, None

# create (small) map

# assumed within starting range: 2 different luxuries, 1 horses, 1 iron

# even gridrows will have an indent -> hexagonal
grid = [[random.random() for i in range(GRIDSIZE)] for j in range(GRIDSIZE)]

def set_visibility(x, y, n, hill=False, first=True):
    grid[y][x].visible = True
    if n > 0:
        #clear = not (not first and grid[y][x].blocks_sight())
        #if clear and :
        for xn, yn in neighbours(x, y):
            if not (xn < 0 or xn > GRIDSIZE-1 or yn < 0 or yn > GRIDSIZE-1):
                t = grid[y][x]
                if first or (hill and not (isinstance(t, tile.Mountain) or (t.hill and t.forest))) or not t.blocks_sight():
                    set_visibility(xn, yn, n-1, hill, False)

def NW(x, y):
    if y % 2 == 0:
        return (x,y-1)
    else:
        return (x-1,y-1)

def NE(x, y):
    if y % 2 == 0:
        return (x+1,y-1)
    else:
        return (x,y-1)

def W(x, y):
    return (x-1,y)

def E(x, y):
    return (x+1, y)

def SW(x, y):
    if y % 2 == 0:
        return (x,y+1)
    else:
        return (x-1,y+1)

def SE(x, y):
    if y % 2 == 0:
        return (x+1,y+1)
    else:
        return (x,y+1)

def neighbours(x, y):
    return [NW(x,y), NE(x,y), W(x,y), E(x,y), SW(x,y), SE(x,y)]

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

# printing
def print_map():
    space = True
    print ''

    for g in grid:
        g1 = []
        g2 = []
        g3 = []
        colors = []
        if space:
            g1.append(' ')
            g2.append(' ')
            g3.append(' ')
            colors.append(ENDC)
            space = False
        else:
            space = True
        for t in g:
            top, middle, bottom, color = '     ', '     ', '     ', ENDC
            if t.visible:
                top, middle, bottom, color = t.pprint()
            g1.append(top)
            g2.append(middle)
            g3.append(bottom)
            colors.append(color) 
        for i in range(len(g1)):
            print colors[i], g1[i], ENDC,
        print ''
        for i in range(len(g1)):
            print colors[i], g2[i], ENDC,
        print ''
        for i in range(len(g1)):
            print colors[i], g3[i], ENDC,
        print ''

    print ''

print_map()

# determine moves, where to settle
inp = ''
while(not inp.upper() in ['NW','NE','W','E','SW','SE']):
    inp = raw_input("Move Warrior: ")

x,y = eval(inp.upper() + '(' + str(wx) + ',' + str(wy) + ')')
grid[y][x].occupant = WARRIOR
grid[wy][wx].occupant = None
wx, wy = x, y
set_visibility(wx, wy, 2, grid[wy][wx].hill)

print_map()

if not grid[wy][wx].blocks_sight():
    inp = ''
    while(not inp.upper() in ['NW','NE','W','E','SW','SE']):
        inp = raw_input("Move Warrior: ")

    x,y = eval(inp.upper() + '(' + str(wx) + ',' + str(wy) + ')')
    grid[y][x].occupant = WARRIOR
    grid[wy][wx].occupant = None
    wx, wy = x, y
    set_visibility(wx, wy, 2, grid[wy][wx].hill)

    print_map()

inp = ''
while(not inp.upper() in ['NW','NE','W','E','SW','SE']):
    inp = raw_input("Move Settler: ")

x,y = eval(inp.upper() + '(' + str(sx) + ',' + str(sy) + ')')
grid[y][x].occupant = SETTLER
grid[sy][sx].occupant = None
sx, sy = x, y
set_visibility(sx, sy, 2, grid[sy][sx].hill)

print_map()

if not grid[sy][sx].blocks_sight():
    inp = ''
    while(not inp.upper() in ['NW','NE','W','E','SW','SE']):
        inp = raw_input("Move Settler: ")

    x,y = eval(inp.upper() + '(' + str(sx) + ',' + str(sy) + ')')
    grid[y][x].occupant = SETTLER
    grid[sy][sx].occupant = None
    sx, sy = x, y
    set_visibility(sx, sy, 2, grid[sy][sx].hill)

    print_map()








