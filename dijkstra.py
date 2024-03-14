# --- Imports ---
from pathlib import Path

# --- Constants ---
FILENAME = 'paths.txt'

def main():
    # = Open and read file =
    file = Path(__file__).with_name(FILENAME)
    fp = open(file, "r")

    start = fp.readline().strip('\n')
    goal = fp.readline().strip('\n')

    # - Assemble path dictionary -
    paths = {}
    for line in fp.readlines():
        (a, b, c) = line.strip('\n').split(',')
        cost = int(c)
        # add each path head for the first time
        if not(a in paths.keys()):
            paths[a] = {}
        if not(b in paths[a].keys()):
            paths[a][b] = cost
        elif paths[a][b] > cost : paths[a][b] = cost


    # = Searching algorithm =
    queue = [([start],0)]
    seen = []

    # - Find path from `start` to `goal` via Dijkstra's algorithm -
    while len(queue) > 0:
        # Pop first element in queue and add children
        (p, c) = queue.pop(0)
        curr = p[-1]

        if curr == goal:
            # end state reached!
            print(F"Path: {p}, Cost: {c}")
            fp.close()
            return 0
        # Drop nodes already explored by some cheaper path
        elif curr in seen:
            continue
        else:
            # otherwise add node to list of seen nodes
            seen.append(curr)
        
        # Add possible paths to queue
        if curr in paths.keys():
            for (k,v) in paths[curr].items():
                # Insert new nodes into list, sorted by ascending pathcost
                # could optimise futher here by checking `seen` list... 
                queue.insert(1, (p + [k], c+v))
        else:
            # no known paths for location - dead node
            continue

        # Queue step update
        # print(F"Queue: {queue}")


    # if code reaches this point, no valid paths to goal state
    print(F"No path found from {start} to {goal}!")
    fp.close()
    return -1

main()