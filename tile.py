# http://civilization.wikia.com/wiki/Terrain_(Civ5)

PURPLE = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'

class Tile(object):

    def __init__(self):
        self.base_food = 0
        self.base_production = 0
        self.base_gold = 0
        self.color = ENDC
        self.symbol = '.'
        self.visible = False # True
        self.occupant = None
        self.forest = False
        self.hill = False

    def food(self):
        return self.base_food

    def production(self):
        return self.base_production

    def gold(self):
        return self.base_gold
        
    def pprint(self):
        mid = '   '
        if self.occupant:
            mid = ' ' + self.occupant + ' '
        bottom = ' ' + str(self.food()) + str(self.production()) + str(self.gold()) + ' '
        return ' '+self.symbol*3+' ', self.symbol+mid+self.symbol, bottom, self.color

    def blocks_sight(self):
        if isinstance(self, Mountain) or self.forest or self.hill:
            return True
        return False

    def set_hill(self):
        self.hill = True
        self.base_food = 0
        self.base_production = 2
        self.base_gold = 0
        self.symbol = '^'

    def set_forest(self):
        self.forest = True
        self.base_food = 1
        self.base_production = 1
        self.base_gold = 0
        self.symbol = '%'
        if self.hill:
            self.symbol = 'F'

class Grassland(Tile):
    
    def __init__(self):
        super(Grassland, self).__init__()
        self.base_food = 2
        self.color = GREEN
        self.symbol = ','

class Plain(Tile):
    
    def __init__(self):
        super(Plain, self).__init__()
        self.base_food = 1
        self.base_production = 1
        self.color = YELLOW

class Mountain(Tile):
    
    def __init__(self):
        super(Mountain, self).__init__()
        self.color = RED
        self.symbol = 'A'
