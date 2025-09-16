from collections import deque

def bfs(start_city, goal_city, adjacency_matrix) -> list:
    queue = deque([start_city])
    visited = set()

    path = []
    while queue:
        current_city = queue.popleft()
        visited.add(current_city)
        path.append(current_city)

        if current_city == goal_city:
            return path
        
        for neighbor in adjacency_matrix[current_city]:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)

    return []