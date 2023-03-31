import math
from util.util import QueryParser, StoreParser
from util.haversine import haversine

def main():
    qp = QueryParser()
    wb = StoreParser()
    sb = StoreParser()
    qp.parse("tests/Queries.csv")
    wb.parse("tests/whataburger/WhataburgerData.csv")
    sb.parse("tests/starbucks/StarbucksData.csv")
    
    for q in qp.queries:
        print(f"The {q.stores} closest Whataburgers to ({q.point.x}, {q.point.y})")
        distances = []
        for store in wb.stores:
            distance = haversine(q.point.x, q.point.y, store.lat, store.long)
            distances.append(distance)
            # compute order statistics
            
            radiusOfEarth = '3958.8'# miles
            
            #convert lat/long to radians
            lat1 = math.radians(q.point.x)
            lon1 = math.radians(q.point.y)
            lat2 = math.radians(store.lat)
            lon2 = math.radians(store.long)
            
            #then apply harvesine formula
            a = math.sin((lat2 - lat1)/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1)/2)**2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
            distance = radiusOfEarth * c
            
            # sort first 30 stores in increasing order (any O(n^2))
            
            # output stores from closest to farthest
            # format: [store] #[id]. [addr] [street], [city], [state], [zip]. - [distance] miles

    for q in qp.queries:
        print(f"The {q.stores} closest Starbucks to ({q.point.x}, {q.point.y})")

if __name__ == "__main__":
    main()
