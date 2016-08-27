# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
#n, m = 5, 5
#lines = [1, 1, 1, 1, 1]
#n, m  = 6, 4
#lines = [10, 0, 5, 0, 3, 3]
rank = [1] * n
parent = list(range(0, n))
p = max(lines)


def getParent(table):
    # find parent and compress path
    if table != parent[table]:
        parent[table] = getParent(parent[table])
    return parent[table]


def merge(destination, source):
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        if p > lines[realDestination]:
            print(p)
        else:
            print(lines[realDestination])
        return

    parent[realSource] = realDestination

    lines[realDestination], lines[realSource] = (lines[realDestination] + lines[realSource]), 0

    if p > lines[realDestination]:
        print(p)
    else:
        print(lines[realDestination])
    #print("parents of d and s", realDestination, realSource)
    #print("lines", lines)
    #print("rank", rank)
    #print("parents list", parent)
    #print()
    #print()
    # merge two components
    # use union by rank heuristic
    # update ans with the new maximum table size
    return

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)

#Test

#destination, source = 3, 5
#merge(destination - 1, source - 1)

#destination, source =2, 4
#merge(destination - 1, source - 1)

#destination, source = 1, 4
#merge(destination - 1, source - 1)

#destination, source = 5, 4
#merge(destination - 1, source - 1)

#destination, source = 5, 3
#merge(destination - 1, source - 1)

#destination, source = 6, 6
#merge(destination - 1, source - 1)

#destination, source = 6, 5
#merge(destination - 1, source - 1)

#destination, source = 5, 4
#merge(destination - 1, source - 1)

#destination, source = 4, 3
#merge(destination - 1, source - 1)
