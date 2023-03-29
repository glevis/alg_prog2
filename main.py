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

            # sort first 30 stores in increasing order (any O(n^2))
            
            # output stores from closest to farthest
            # format: [store] #[id]. [addr] [street], [city], [state], [zip]. - [distance] miles

    for q in qp.queries:
        print(f"The {q.stores} closest Starbucks to ({q.point.x}, {q.point.y})")

if __name__ == "__main__":
    main()
