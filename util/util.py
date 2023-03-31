import csv 

class QueryParser:
    def __init__(self):
        self.queries = []

    def parse(self, path):
        f = open(path, "r")
        # header
        f.readline() 
        for line in f:
           line = line.replace('\n', '')
           x, y, stores = line.split(',') 
           point = Point(x, y)
           query = Query(point, stores)
           self.queries.append(query)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Query:
    def __init__(self, point, stores):
        self.point = point
        self.stores = stores

class StoreParser:
    def __init__(self):
        self.stores = []

    def parse(self, path):
        with open(path, newline='') as f:
            # header
            next(f)
            lines = csv.reader(f, delimiter=',', quotechar='"')
            for line in lines:
                id, addr, city, state, zip, lat, long = line
                store = Store(id, addr, city, state, zip, lat, long)
                self.stores.append(store)

class Store:
    def __init__(self, id, addr, city, state, zip, lat, long):
        self.id = id
        self.addr = addr
        self.city = city
        self.state = state
        self.zip = zip
        self.lat = lat
        self.long = long
        self.distance = 0

    def setDistance(self, dist):
        self.distance = dist
