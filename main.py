from util.util import QueryParser, StoreParser
from random import randrange
from util.haversine import haversine
import random

def rand_select(a, l, r, i):
    if l == r:
            return a[l]
    if l < r:
        z = rand_partition(a, l, r)
        k = z - l

        if i==k:
            return a[z]
        elif i < k:
            return rand_select(a, l, z-1, i)
        else:
            return rand_select(a, z+1, r, i-k-1)

def rand_partition(a, l, r):
    k = random.randrange(l, r+1)
    (a[k], a[l]) = (a[l], a[k])
    x = a[l].distance
    i = l
    for j in range(l+1, r+1):
        if a[j].distance <= x:
            i = i + 1
            (a[j], a[i]) = (a[i], a[j])
    (a[l], a[i]) = (a[i], a[l])
    return i

def sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and key.distance < a[j].distance :
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

def main():
    qp = QueryParser()
    wb = StoreParser()
    sb = StoreParser()
    qp.parse("tests/Queries.csv")
    wb.parse("tests/whataburger/WhataburgerData.csv")
    sb.parse("tests/starbucks/StarbucksData.csv")

    for q in qp.queries:
        wb_distances = []
        print(f"\nThe {q.stores} closest Whataburgers to ({q.point.x}, {q.point.y})")
        for store in wb.stores:
            distance = haversine(q.point.x, q.point.y, store.lat, store.long)
            store.setDistance(distance)
            wb_distances.append(store)
               

        # compute order statistics
        i = int(q.stores) - 1
        rand_select(wb_distances, 0, len(wb_distances) - 1, i) 
        # sort first x stores in increasing order (any O(n^2))
        sorted = wb_distances[0:int(q.stores)]
        sort(sorted)
        count = 1
        # output stores from closest to farthest
        # format: [store] #[id]. [addr] [street], [city], [state], [zip]. - [distance] miles
        for store in sorted:
            if count <= int(q.stores):
                print(f"Store #{store.id}. {store.addr}, {store.city}, {store.state}, {store.zip}. - {round(store.distance, 2)} miles.")
            count = count + 1

    for q in qp.queries:
        sb_distances = []
        print(f"\nThe {q.stores} closest Starbucks to ({q.point.x}, {q.point.y})")
        for store in sb.stores:
            distance = haversine(q.point.x, q.point.y, store.lat, store.long)
            store.setDistance(distance)
            sb_distances.append(store)

        # compute order statistics
        i = int(q.stores) - 1
        rand_select(sb_distances, 0, len(sb_distances) - 1, i)
        # sort first X stores in increasing order
        sorted = sb_distances[0:int(q.stores)]
        sort(sorted)
        count = 1

        # output stores from closest to farthest
        # format: [store] #[id]. [addr] [street], [city], [state], [zip]. - [distance] miles
        for store in sorted:
            if count <= int(q.stores):
                print(f"Store #{store.id}. {store.addr}, {store.city}, {store.state}, {store.zip}. - {round(store.distance, 2)} miles.")
            count = count + 1

if __name__ == "__main__":
    main()

