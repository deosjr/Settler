# http://civilization.wikia.com/wiki/Terrain_(Civ5)

import random

import resource

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
        self.visible = False #True
        self.occupant = None
        self.forest = False
        self.hill = False
        self.resource = None
        self.luxury = False

    def food(self):
        food = self.base_food
        if self.resource:
            food += self.resource.base_food #+ self.resource.improvement_food
        return food

    def production(self):
        production = self.base_production
        if self.resource:
            production += self.resource.base_production #+ self.resource.improvement_production
        return production

    def gold(self):
        gold = self.base_gold
        if self.resource:
            gold += self.resource.base_gold #+ self.resource.improvement_gold
        return gold
        
    def pprint(self):
        top = ' '+self.symbol*3+' '
        if self.resource:
            top = ' '+self.symbol+self.resource.symbol+self.symbol+' '
        mid = '   '
        if self.occupant:
            mid = ' ' + self.occupant + ' '
        bottom = ' ' + str(self.food()) + str(self.production()) + str(self.gold()) + ' '
        return top, self.symbol+mid+self.symbol, bottom, self.color

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
            self.symbol = '#'

class Grassland(Tile):
    
    def __init__(self):
        super(Grassland, self).__init__()
        self.base_food = 2
        self.color = GREEN
        self.symbol = ','

    def random_resource(self):
        if self.hill and self.forest:
            return
        r = random.random()
        if r > 0.7:
            if r > 0.95:
                self.random_luxury()
            else:
                if self.forest:
                    self.resource = resource.Deer()
                elif self.hill:
                    self.resource = resource.Sheep()
                else:
                    if r < 0.8:
                        self.resource = resource.Wheat()
                    elif r < 0.85:
                        self.resource = resource.Stone()
                    elif r < 0.9:
                        self.resource = resource.Cattle()

    def random_luxury(self):
        self.luxury = True
        r = random.random()
        if self.hill:
            if r > 0.5:
                self.resource = resource.Silver()
            else:
                self.resource = resource.Gold()
        elif self.forest:
            if r > 0.5:
                self.resource = resource.Furs()
            else:
                self.resource = resource.Silk()
        else:
            if r > 0.5:
                self.resource = resource.Wine()
            else:
                self.resource = resource.Marble()
        self.color = PURPLE

class Plain(Tile):
    
    def __init__(self):
        super(Plain, self).__init__()
        self.base_food = 1
        self.base_production = 1
        self.color = YELLOW

    def random_resource(self):
        if self.hill and self.forest:
            return
        r = random.random()
        if r > 0.7:
            if r > 0.95:
                self.random_luxury()
            else:
                if self.forest:
                    self.resource = resource.Deer()
                elif self.hill:
                    self.resource = resource.Sheep()
                else:
                    if r < 0.8:
                        self.resource = resource.Wheat()
                    elif r < 0.85:
                        self.resource = resource.Stone()
                    elif r < 0.9:
                        self.resource = resource.Cattle()

    def random_luxury(self):
        self.luxury = True
        r = random.random()
        if self.hill:
            if r > 0.5:
                self.resource = resource.Silver()
            else:
                self.resource = resource.Gold()
        elif self.forest:
            if r > 0.5:
                self.resource = resource.Spices()
            else:
                self.resource = resource.Silk()
        else:
            if r > 0.5:
                self.resource = resource.Ivory()
            else:
                self.resource = resource.Cotton()
        self.color = PURPLE

class Mountain(Tile):
    
    def __init__(self):
        super(Mountain, self).__init__()
        self.color = RED
        self.symbol = 'A'
