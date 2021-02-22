from turtle import Turtle, Screen

s = 10
screen = Screen()
screen.tracer(0, 0)

def rect(p):
    tur = Turtle()
    
    #setters
    tur.ht()
    tur.up()
    tur.speed(0)

    x = p[0] * s
    y = p[1] * -s
    
    #continue
    tur.fillcolor("gray")

    #position
    tur.goto(x - s / 2, y - s / 2)

    #fill rec
    tur.begin_fill()
    
    tur.setx(x + s / 2)
    tur.sety(y + s / 2)
    tur.setx(x - s / 2)
    tur.sety(y - s / 2)
    tur.end_fill()
    screen.update()
    return x, y   

#flags
draw = False
visited = []


def resetFlags():
    global visited
    visited = []
    
def showSearch(boolean):
    global draw
    draw = boolean

def dfs(graph, node):
    if graph[node][0] == "G": return [node]
    
    if node not in visited:
        visited.append(node)
        if draw: rect(node)
        for neighbour in graph[node][1:]:
            isType = dfs(graph, neighbour)
            if isType:    
                return [node] + isType
        return []
    return []

def bfs(graph, node):
    node = node + (None,)
    queue = [node]
    while queue:
        path = queue.pop(0)
        
        if draw: rect(path)
        for neighbour in graph[path[:-1]][1:]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour + (path,))
                if graph[neighbour][0] == "G":
                    print(queue[-1])    
                    #print(path)
                    return
    
def astar(graph, node, end, g = 0):
    if node == end: return [node]
    
    if node not in visited:
        visited.append(node)
        if draw: rect(node)
        improved = {}
        for neighbour in graph[node][1:]:
            if neighbour in ((node[0], node[1] - 1), (node[0], node[1] + 1), (node[0] - 1, node[1]), (node[0] + 1, node[1])):
                improved[g + 10 + ((neighbour[0] - end[0])**2 + (neighbour[1] - end[1])**2) * 10] = neighbour
            else: improved[g + 14 + ((neighbour[0] - end[0])**2 + (neighbour[1] - end[1])**2) * 10] = neighbour
        ud = improved
        improved = dict(sorted(ud.items()))
        
        for best in improved:
            isType = astar(graph, improved[best], end, g)
            if isType:
                return [node] + isType
        return []
    return[]
            

def custom(graph, node):
    if graph[node][0] == "G": return [node]
    
    if node not in visited:
        visited.append(node)
        if draw: rect(node)
        for neighbour in graph[node][1:]:
            if neighbour in ((node[0], node[1] - 1), (node[0], node[1] + 1), (node[0] - 1, node[1]), (node[0] + 1, node[1])):
                isType = custom(graph, neighbour)
                if isType:
                    return [node] + isType
        return []
    return []