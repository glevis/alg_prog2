from util.util import QueryParser

def main():
    qp = QueryParser()
    qp.parse("tests/Queries.csv")
    for q in qp.queries:
        print(q.point.x, q.point.y)

if __name__ == "__main__":
    main()
