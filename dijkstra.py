def main():
    # = Open and read file =
    fp = open("paths.txt")
    start = fp.readline().strip('\n')
    goal = fp.readline().strip('\n')

    paths = {}
    queue = [([start],0)]

    # - Assemble path dictionary -
    for line in fp.readlines():
        (a, b, c) = line.strip('\n').split(',')
        cost = int(c)
        # add each path head for the first time
        if not(a in paths.keys()):
            paths[a] = {}
        if not(b in paths[a].keys()):
            paths[a][b] = cost
        elif paths[a][b] > cost : paths[a][b] = cost


    # - Find path from `start` to `goal` via Dijkstra's algorithm -
    while len(queue) > 0:
        # Pop first element in queue and add children
        (path, c) = queue.pop(0)

        if path[-1] == goal:
            # end state reached!
            print(F"Path: {path}, Cost: {c}")
            return 0
        
        # Add possible paths to queue
        if path[-1] in paths.keys():
            s = paths[path[-1]]
            for (k,v) in s.items():
                # Insert new nodes into list, sorted by ascending pathcost
                queue.insert(1, (path + [k], c+v))
        else:
            # no known paths for location - dead node
            continue

        # Queue step update
        # print(F"Queue: {queue}")


    # if code reaches this point, no valid paths to goal state
    print(F"No path found from {start} to {goal}!")
    return -1

main()