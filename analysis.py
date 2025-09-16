from bfs import bfs
from dfs import dfs

city_names = ["Oradea", "Zerind", "Arad", "Timisoara", "Lugoj", "Mehadia", "Drobeta", "Craiova", "Rimnicu Vilcea", "Sibiu", "Fagaras", "Pitesti", "Bucharest", "Giurgiu", "Urziceni", "Hirsova", "Eforie", "Vaslui", "Iasi", "Neamt"]
city_names.sort()

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


START_CITY = "Arad"
GOAL_CITY = "Bucharest"

print(f"bfs path: {bfs(START_CITY, GOAL_CITY, weighted_adjacency_matrix)}")
print(f"dfs path: {dfs(START_CITY, GOAL_CITY, weighted_adjacency_matrix)}")