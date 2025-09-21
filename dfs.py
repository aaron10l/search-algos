def dfs(start_city, goal_city, adjacency_matrix):
    stack = [start_city]
    visited = set()
    path = []

    while stack:
        current_city = stack.pop()
        visited.add(current_city)
        path.append(current_city)

        if current_city == goal_city:
            return (path, len(visited))
        
        for neighbor in adjacency_matrix[current_city]:
            if neighbor not in visited and neighbor not in stack:
                stack.append(neighbor)

    return ([], len(visited))