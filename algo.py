import turtle

s = 10

def rect(p):
    tur = turtle.Turtle()
    
    #setters
    tur.ht()
    tur.up()
    tur.speed(0)
    for i in p:
        if i[2] in (" ", "0"): continue
        x = i[0] * s
        y = i[1] * -s
        
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
    return x, y   

#flags
draw = False
visited = []
path = []


def resetFlags():
    global visited
    global path
    visited = []
    path = []   
    
def showSearch(boolean):
    global draw
    draw = boolean

def dfs(graph, node):
    global path
    if draw: path += rect((node[0], node[1]))
    if graph[node][0] == "G": return path
    
    if node not in visited:
        visited.append(node)
            
        for neighbour in graph[node][1:]:
            dfs(graph, neighbour)
    return

def bfs(graph, node):
    global path
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        h = queue.pop(0)
        if draw: path += rect([(h[0], h[1])])
        for neighbour in graph[h][1:]:
            if neighbour not in visited:
                visited.append(neighbour)
                if graph[neighbour][0] != "X":
                    queue.append(neighbour)
                if graph[neighbour][0] == "G": return
    
def astar(graph, node, end, g = 0, par = None):
    global path
    if draw: path += rect((node[0], node[1]))
    if not node[0] - end[0] + node[1] - end[1]: return path
    
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
    global path
    if draw: path += rect((node[0], node[1]))
    if graph[node][0] == "G": return path
    if node not in visited:
        visited.append(node)
        
        for neighbour in graph[node][1:]:
            if neighbour in ((node[0], node[1] - 1), (node[0], node[1] + 1), (node[0] - 1, node[1]), (node[0] + 1, node[1])):
                custom(graph, neighbour)
    return
