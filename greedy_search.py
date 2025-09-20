
import heapq
from heuristics import h_sum_neighbors, h_min_neighbor

def greedy_search(origin, target, graph, h_func=h_sum_neighbors):
    """
    Greedy Best-First Search (GBFS)
    Expands the most promising node based on h(n).
    Returns (path, nodes_expanded).
    """
    # Priority queue holds tuples (h_value, current_node, path_so_far)
    frontier = [(0, origin, [origin])]
    explored = set()
    expansions = 0

    while frontier:
        h_value, current, route = heapq.heappop(frontier)
        expansions += 1

        if current == target:
            return route, expansions

        if current in explored:
            continue

        explored.add(current)
        for neighbor in graph[current]:
            priority = h_func(neighbor, target, graph)
            heapq.heappush(frontier, (priority, neighbor, route + [neighbor]))

    return None, expansions

#Testing

if __name__ == "__main__":
    from analysis import weighted_adjacency_matrix, START_CITY, GOAL_CITY

    path1, expanded1 = greedy_search(START_CITY, GOAL_CITY, weighted_adjacency_matrix, h_sum_neighbors)
    path2, expanded2 = greedy_search(START_CITY, GOAL_CITY, weighted_adjacency_matrix, h_min_neighbor)

    print(f"GBFS with Sum heuristic: {path1} | Nodes expanded: {expanded1}")
    print(f"GBFS with Min heuristic: {path2} | Nodes expanded: {expanded2}")
