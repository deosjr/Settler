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

    # printing
def print_map(grid):
    ENDC = '\033[0m'
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