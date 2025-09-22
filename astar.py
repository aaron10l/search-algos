import heapq
from heuristics import h_sum_neighbors, h_min_neighbor

class llPath:
    def __init__(self, city, g , h, prev = None):
        self.city = city 
        self.g = g 
        self.h = h 
        self.f = g + h
        self.prev = prev 

    def __lt__(self, right):
        return self.f < right.f

    def fullPath(self): # build path to node recursively
        if self.prev:
            return self.prev.fullPath() + [self.city]
        else:
            return [self.city]

def astarSearch(start, end, map, h_func=h_sum_neighbors):
    '''
    A*
    Computes h and g to find the cheapest path
    returns (path, expansions)
    '''
    # initialize with value of start node and its heuristic value
    queue = [llPath(start, 0, h_func(start, end, map))]
    explored = set() 
    expansions = 0         

    while queue:
        current = heapq.heappop(queue)
        expansions += 1

        if current.city == end:
            return current.fullPath(), expansions

        if current.city in explored:
            continue

        explored.add(current.city)
        for neighbor, cost in map[current.city].items():
            neighborCost = current.g + cost 
            h = h_func(neighbor, end, map)
            next = llPath(neighbor, neighborCost, h, current)
            heapq.heappush(queue, next)

    return None, expansions
