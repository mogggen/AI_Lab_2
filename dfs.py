def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

found = False
visited = []
def DFS(pos, nodes):
    global found
    global visited
    if nodes[pos] == "G": found = True
    if nodes[pos] == "X" or found:
        return
    visited += nodes[pos]
    x = pos[0]
    y = pos[1]
    DFS((x + 1, y - 1), nodes) # 3
    DFS((x + 1, y), nodes) # 6
    DFS((x, y - 1), nodes) # 2
    DFS((x - 1, y - 1), nodes) # 1
    DFS((x + 1, y + 1), nodes) # 9
    DFS((x, y + 1), nodes) # 8
    DFS((x - 1, y), nodes) # 4
    DFS((x - 1, y + 1), nodes) # 7

#DFS((1, 1), nodes)
