
# Straight-line distances to Bucharest 
sld_to_bucharest = {
    "Arad": 366, "Bucharest": 0, "Craiova": 160, "Drobeta": 242, "Eforie": 161,
    "Fagaras": 176, "Giurgiu": 77, "Hirsova": 151, "Iasi": 226, "Lugoj": 244,
    "Mehadia": 241, "Neamt": 234, "Oradea": 380, "Pitesti": 100,
    "Rimnicu Vilcea": 193, "Sibiu": 253, "Timisoara": 329,
    "Urziceni": 80, "Vaslui": 199, "Zerind": 374
}

def h_sum_neighbors(node, destination, graph):
    """
    Heuristic 1: Sum of all edge weights from this node.
    If destination is Bucharest, use precomputed straight-line distances.
    """
    if destination == "Bucharest":
        return sld_to_bucharest[node]
    return sum(graph[node].values())

def h_min_neighbor(node, destination, graph):
    """
    Heuristic 2: Minimum edge weight to any neighbor.
    """
    if destination == "Bucharest":
        return sld_to_bucharest[node]
    return min(graph[node].values())
