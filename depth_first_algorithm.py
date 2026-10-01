def dfs(graph, root):
    visited = []
    stack = [root]

    while stack:
        current_node = stack.pop()
        
        if current_node not in visited:
            visited.append(current_node)
            
            for neighbor in range(len(graph[current_node]) - 1, -1, -1):
                if graph[current_node][neighbor] == 1 and neighbor not in visited:
                    stack.append(neighbor)
                    
    return visited