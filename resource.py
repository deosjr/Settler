# http://civilization.wikia.com/wiki/Resources_(Civ5)

class Resource(object):

    def __init__(self):
        self.base_food = 0
        self.base_production = 0
        self.base_gold = 0
        self.improvement_food = 0
        self.improvement_production = 0
        self.improvement_gold = 0
        self.luxury = False
        self.symbol = 'X'

class Wheat(Resource):

    def __init__(self):
        super(Wheat, self).__init__()
        self.base_food = 1
        self.symbol = 'w'
        self.improvement_food = 1

class Cattle(Resource):

    def __init__(self):
        super(Cattle, self).__init__()
        self.base_food = 1
        self.symbol = 'c'
        self.improvement_production = 1

class Sheep(Resource):

    def __init__(self):
        super(Sheep, self).__init__()
        self.base_food = 1
        self.symbol = 's'
        self.improvement_food = 1

class Deer(Resource):

    def __init__(self):
        super(Deer, self).__init__()
        self.base_food = 1
        self.symbol = 'd'
        self.improvement_production = 1

class Stone(Resource):

    def __init__(self):
        super(Stone, self).__init__()
        self.base_production = 1
        self.symbol = 'r'
        self.improvement_production = 1

class Horses(Resource):

    def __init__(self):
        super(Horses, self).__init__()
        self.base_production = 1
        self.symbol = 'h'
        self.improvement_production = 1

class Iron(Resource):

    def __init__(self):
        super(Iron, self).__init__()
        self.base_production = 1
        self.symbol = 'i'
        self.improvement_production = 1

class Spices(Resource):

    def __init__(self):
        super(Spices, self).__init__()
        self.base_gold = 2
        self.symbol = 'K'
        self.improvement_gold = 1

class Furs(Resource):

    def __init__(self):
        super(Furs, self).__init__()
        self.base_gold = 2
        self.symbol = 'F'
        self.improvement_gold = 1

class Ivory(Resource):

    def __init__(self):
        super(Ivory, self).__init__()
        self.base_gold = 2
        self.symbol = 'I'
        self.improvement_gold = 1

class Silk(Resource):

    def __init__(self):
        super(Silk, self).__init__()
        self.base_gold = 2
        self.symbol = 'Z'
        self.improvement_gold = 1

class Dyes(Resource):

    def __init__(self):
        super(Dyes, self).__init__()
        self.base_gold = 2
        self.symbol = 'D'
        self.improvement_gold = 1

class Wine(Resource):

    def __init__(self):
        super(Wine, self).__init__()
        self.base_gold = 2
        self.symbol = 'W'
        self.improvement_gold = 1

class Gold(Resource):

    def __init__(self):
        super(Gold, self).__init__()
        self.base_gold = 2
        self.symbol = 'G'
        self.improvement_production = 1

class Silver(Resource):

    def __init__(self):
        super(Silver, self).__init__()
        self.base_gold = 2
        self.symbol = 'S'
        self.improvement_production = 1

class Marble(Resource):

    def __init__(self):
        super(Marble, self).__init__()
        self.base_gold = 2
        self.symbol = 'M'
        self.improvement_production = 1

class Cotton(Resource):

    def __init__(self):
        super(Cotton, self).__init__()
        self.base_gold = 2
        self.symbol = 'C'
        self.improvement_gold = 1