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
    for _ in graph:
        if graph[_][0] == 'G': goal = _

    node += None, 0, abs(goal[0] - node[0]) + abs(goal[1] - node[1])
    openlist = []
    closedlist = []

    openlist.append(node)

    while openlist:
        current = min(openlist, key=lambda d:d[-2]+d[-1])
        pos = current[:2]
        par = current[2]
        g, h = current[-2:]

        if pos == goal:
            path = []
            while par:
                path.append(pos)
                current = par
            path.append(pos)
            return path[::-1]
        
        openlist.remove(current)
        closedlist.append(current)
    
        for g in graph[x, y][1:]:
            if pos in closedlist: continue
            if pos in openlist:
                gNew = g + s14 if (pos[0] - node[0] + pos[1] - node[1]) % 2 else 10
                gNeigbhbour = g[-2]
                gNew = gCurr + gNeigbhbour
            else:




    
    if node in openlist:
        visited.append(node)
        if draw: rect(node)
        improved = {}
        for neighbour in graph[node][1:]:
            if not (neighbour[0] - node[0] + neighbour[1] - node[1]) % 2:
                improved[g + 10 + abs(neighbour[0] - end[0]) + abs((neighbour[1] - end[1])) * 10] = neighbour
            else: improved[g + 14 + abs(neighbour[0] - end[0]) + abs((neighbour[1] - end[1])) * 10] = neighbour
        ud = improved
        improved = dict(sorted(ud.items()))
        
        for best in improved:
            isType = astar(graph, improved[best], end)
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
            if not (neighbour[0] - node[0] + neighbour[1] - node[1]) % 2:
                isType = custom(graph, neighbour)
                if isType:
                    return [node] + isType
        return []
    return []