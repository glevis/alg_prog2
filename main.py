from util.util import QueryParser, StoreParser
from random import randrange
from util.haversine import haversine
import random

def rand_select(a, l, r, i):
    if l==r:
        return a[l]
    z = rand_partition(a, l, r)
    k = z - l

    if i==k:
        return a[z]
    elif i < k:
        return rand_select(a, l, z-1, i)
    else:
        return rand_select(a, z+1, r, i-k)

def rand_partition(a, l, r):
    k = random.randrange(l, r)
    (a[k], a[l]) = (a[l], a[k])
    x=a[l]
    i = l
    for j in range(l+1, r+1):
        if a[j] <= x:
            i = i + 1
            (a[j], a[i]) = (a[i], a[j])
    (a[l], a[i]) = (a[i], a[l])
    return i

def sort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and key < a[j] :
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
        print(f"The {q.stores} closest Whataburgers to ({q.point.x}, {q.point.y})")
        for store in wb.stores:
            distance = haversine(q.point.x, q.point.y, store.lat, store.long)
            wb_distances.append(distance)

        # compute order statistics
        i = int(q.stores) - 1
        rand_select(wb_distances, 0, len(wb_distances) - 1, i) 
        # sort first x stores in increasing order (any O(n^2))
        sorted = wb_distances[0:int(q.stores)]
        sort(sorted)
        count = 1
        for i in sorted:
            if count <= int(q.stores):
                print(i)
            count = count + 1
        # output stores from closest to farthest
        # format: [store] #[id]. [addr] [street], [city], [state], [zip]. - [distance] miles

    for q in qp.queries:
        print(f"The {q.stores} closest Starbucks to ({q.point.x}, {q.point.y})")

if __name__ == "__main__":
    main()

