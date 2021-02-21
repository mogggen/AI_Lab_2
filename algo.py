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
Found = False
draw = False
visited = []
#path = []


def resetFlags():
    global Found
    global visited
    #global path
    visited = []
    #path = []   
    
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
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        path = queue.pop(0)
        if draw: rect(path)
        for neighbour in graph[path][1:]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                if graph[neighbour][0] == "G": return
    
def astar(graph, node, end, g = 0, par = None):
    global Found
    global path
    if draw: path += rect(node)
    if not node[0] - end[0] + node[1] - end[1]: Found = True
    if Found: return path
    
    if node not in visited:
        visited.append(node)
        g + 1
        improved = {}
        for neighbour in graph[node][1:]:
            improved[g + (neighbour[0] - end[0])**2 + (neighbour[1] - end[1])**2] = neighbour
        ud = improved
        improved = dict(sorted(ud.items()))
        
        for best in improved:
            astar(graph, improved[best], end, g, node)

def custom(graph, node):
    global Found
    global path
    if draw: path += rect(node)
    if graph[node][0] == "G": Found = True
    if Found: return path
    if node not in visited and not Found:
        visited.append(node)
        
        for neighbour in graph[node][1:]:
            if neighbour in ((node[0], node[1] - 1), (node[0], node[1] + 1), (node[0] - 1, node[1]), (node[0] + 1, node[1])):
                custom(graph, neighbour)
    return
