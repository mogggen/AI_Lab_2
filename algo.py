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



#flags
Found = False
draw = False
visited = []

queue = []


def resetFlags():
    global Found
    global visited
    global queue
    
    Found = False

    visited = []
    queue = []
    
def setAlgoType(boolean):
    global draw
    draw = boolean

def dfs(graph, node):
    global Found
    if graph[node][0] == "G": Found = True
    if graph[node][0] == "X" or Found: return
    if draw: rect([(node[0], node[1], "T")])
    
    if node not in visited:
        visited.append(node)
            
        for neighbour in graph[node][1:]:
            dfs(graph, neighbour)
    return

def bfs(graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        h = queue.pop(0) 
        for neighbour in graph[h][1:]:
            if neighbour not in visited:
                visited.append(neighbour)
                if graph[neighbour][0] != "X":
                    queue.append(neighbour)
                if graph[neighbour][0] == "G": return
                if draw: rect([(neighbour[0], neighbour[1], "T")])
    
def astar(graph, node, end, g = 0, par = None):
    global Found
    if not node[0] - end[0] + node[1] - end[1]: Found = True
    if graph[node][0] == "X" or Found: return
    if draw: rect([(node[0], node[1], "T")])
    
    if node not in visited:
        visited.append(node)
        g + 1
        improved = {}
        for neighbour in graph[node][1:]: #let's hope that astar finds a decent path instantly and don't backtrack trough parent, otherwise use 'if is parent' guard parameter to give it g - 1. But this should really never occur because if it looked through all the neighbours, it should return to a more sane path without having to check the values, the algo don't need a carrot to go back.            
            improved[g + (neighbour[0] - end[0])**2 + (neighbour[1] - end[1])**2] = neighbour
        ud = improved
        improved = dict(sorted(ud.items(), reverse=False))
        print(improved)
        #- 1 + 2 * (par == neighbour)
        for best in improved:
            astar(graph, improved[best], end, g, node)

def custom(graph, node):
    global Found
    if graph[node][0] == "G": Found = True
    if graph[node][0] == "X" or Found: return
    if draw: rect([(node[0], node[1], "T")])
    if node not in visited:
        visited.append(node)
        
        for neighbour in graph[node][1:]:
            if neighbour in ((node[0], node[1] - 1), (node[0], node[1] + 1), (node[0] - 1, node[1]), (node[0] + 1, node[1])):
                custom(graph, neighbour)
    return
