import time
from bfs import bfs
from dfs import dfs
from greedy_search import greedy_search, h_sum_neighbors, h_min_neighbor


weighted_adjacency_matrix = {}
weighted_adjacency_matrix["Oradea"] = {"Zerind": 71, "Sibiu": 151}
weighted_adjacency_matrix["Zerind"] = {"Oradea": 71, "Arad": 75}
weighted_adjacency_matrix["Arad"] = {"Zerind": 75, "Sibiu": 140, "Timisoara": 118}
weighted_adjacency_matrix["Timisoara"] = {"Arad": 118, "Lugoj": 111}
weighted_adjacency_matrix["Lugoj"] = {"Timisoara": 111, "Mehadia": 70}
weighted_adjacency_matrix["Mehadia"] = {"Lugoj": 70, "Drobeta": 75}
weighted_adjacency_matrix["Drobeta"] = {"Mehadia": 75, "Craiova": 120}
weighted_adjacency_matrix["Craiova"] = {"Drobeta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138}
weighted_adjacency_matrix["Rimnicu Vilcea"] = {"Craiova": 146, "Sibiu": 80, "Pitesti": 97}
weighted_adjacency_matrix["Sibiu"] = {"Oradea": 151, "Arad": 140, "Fagaras": 99, "Rimnicu Vilcea": 80}
weighted_adjacency_matrix["Fagaras"] = {"Sibiu": 99, "Bucharest": 211}
weighted_adjacency_matrix["Pitesti"] = {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucharest": 101}
weighted_adjacency_matrix["Bucharest"] = {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90, "Urziceni": 85}
weighted_adjacency_matrix["Giurgiu"] = {"Bucharest": 90}
weighted_adjacency_matrix["Urziceni"] = {"Bucharest": 85, "Hirsova": 98, "Vaslui": 142}
weighted_adjacency_matrix["Hirsova"] = {"Urziceni": 98, "Eforie": 86}
weighted_adjacency_matrix["Eforie"] = {"Hirsova": 86}
weighted_adjacency_matrix["Vaslui"] = {"Urziceni": 142, "Iasi": 92}
weighted_adjacency_matrix["Iasi"] = {"Vaslui": 92, "Neamt": 87}
weighted_adjacency_matrix["Neamt"] = {"Iasi": 87}


def time_1000_runs(search_func, start, goal, graph, heuristic=None):
    # this function runs the specified search function 1000 times and returns the time taken for ALL 1000 RUNS.
    start_time = time.time()
    path, expansions = None, None
    for _ in range(1000):
        if heuristic:
            path, expansions = search_func(start, goal, graph, heuristic)
        else:
            path, expansions = search_func(start, goal, graph)
    end_time = time.time()
    return (end_time - start_time, path, expansions)

def time_all_search_algos(START_CITY, GOAL_CITY):
    results = {}
    print(f"Timing search algorithms from {START_CITY} to {GOAL_CITY}...")
    bfs_time, bfs_path, bfs_expansions = time_1000_runs(bfs, START_CITY, GOAL_CITY, weighted_adjacency_matrix)
    print(f"BFS took {bfs_time:.6f} seconds for 1000 runs with nodes expanded: {bfs_expansions} and path: {bfs_path}")

    dfs_time, dfs_path, dfs_expansions = time_1000_runs(dfs, START_CITY, GOAL_CITY, weighted_adjacency_matrix)
    print(f"DFS took {dfs_time:.6f} seconds for 1000 runs with nodes expanded: {dfs_expansions} and path: {dfs_path}")

    greedy_sum_time, greedy_sum_path, greedy_sum_expansions = time_1000_runs(greedy_search, START_CITY, GOAL_CITY, weighted_adjacency_matrix, heuristic=h_sum_neighbors)
    print(f"Greedy (sum heuristic) took {greedy_sum_time:.6f} seconds for 1000 runs with nodes expanded: {greedy_sum_expansions} and path: {greedy_sum_path}")
    
    greedy_min_time, greedy_min_path, greedy_min_expansions = time_1000_runs(greedy_search, START_CITY, GOAL_CITY, weighted_adjacency_matrix, heuristic=h_min_neighbor)
    print(f"Greedy (min heuristic) took {greedy_min_time:.6f} seconds for 1000 runs with nodes expanded: {greedy_min_expansions} and path: {greedy_min_path}")

    # TODO: Add A* timing here when A* is implemented.

    results['BFS'] = bfs_time
    results['DFS'] = dfs_time
    results['Greedy_Sum'] = greedy_sum_time
    results['Greedy_Min'] = greedy_min_time
    # TODO: Add A* results here when A* is implemented.

    return results

START_CITY = "Arad"
GOAL_CITY = "Bucharest"
