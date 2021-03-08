from turtle import Turtle, Screen

s = 10
screen = Screen()
screen.tracer(0, 0)

def tupAs(value, tup, index):
    return tup[:index] + (value,) + tup[index + 1:]

def rect(p, c = "gray"):
    tur = Turtle()
    
    #setters
    tur.ht()
    tur.up()
    tur.speed(0)

    x = p[0] * s
    y = p[1] * -s
    
    #continue
    tur.fillcolor(c)

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
    
def drawSearch(boolean):
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
    node += None,
    queue = [node]
    while queue:
        path = queue.pop(0)
        
        if draw: rect(path)
        for neighbour in graph[path[:-1]][1:]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour + (path,))
                if graph[neighbour][0] == "G":
                    tem = []
                    temp = queue[-1]
                    while temp:
                        tem += [(temp[0], temp[1])]
                        temp = temp[2]
                    return tem[::-1]

def astar(graph, node):
    goal = ()
    for s in graph:
        if graph[s][0] == 'G': goal = s

    node += 0, (abs(goal[0] - node[0]) + abs(goal[1] - node[1])) * 10, None
    openlist = []
    closedlist = []

    if draw: rect(node)
    visited.append(node)
    openlist.append(node)

    while openlist:
        for f in openlist:
            if node[2] + node[3] > f[2] + f[3]:
                node = f
                #nodeIndex = f[0]

        pos = node[:2]
        g = node[2]
        #h = node[3]
        par = node[4]

        if pos == goal:
            path = []
            while par:
                path.append(pos)
                node = par
            path.append(pos)
            return path[::-1]
        
        print(openlist)
        openlist.remove(node)

        if draw: rect(node, "black")
        visited.append(node)
        closedlist.append(node)
    
        for child in graph[pos][1:]:
            if child in closedlist:
                continue

            if child in openlist:
                gNew = g + (14 if ((pos[0] - child[0]) + (pos[1] - child[1])) % 2 else 10)
                if child[2] > gNew:
                    child = tupAs(gNew, child, 2)
                    child = tupAs(node, child, 4)
            else:
                gNew = g + (14 if ((pos[0] - child[0]) + (pos[1] - child[1])) % 2 else 10)
                hNew = (abs(goal[0] - child[0]) + abs(goal[1] - child[1])) * 10
                
                child = tupAs(gNew, child, 2)
                child = tupAs(hNew, child, 3)

                child = tupAs(node, child, 4)

                openlist.append(child)

def custom(graph, node):
    if graph[node][0] == "G": return [node]
    
    if node not in visited:
        visited.append(node)
        if draw: rect(node)
        for neighbour in graph[node][1:]:
            if not (neighbour[0] - node[0] + neighbour[1] - node[1]) % 2:
                isType = custom(graph, neighbour)
                if isType:
                    return [node] + isType
        return []
    return []