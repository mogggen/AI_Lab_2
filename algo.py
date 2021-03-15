from turtle import Turtle, Screen

s = 10
screen = Screen()
screen.tracer(0, 0)

def tupAs(value, tup, index):
    return tup[:index] + (value,) + tup[index + 1:] if index >= 0 else tup[:len(tup) + index] + (value,) + tup[len(tup) + index + 1:]

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
    bestParent = {} # current: all parent (pos, f)
    goal = [goal for goal in graph if graph[goal][0] == "G"][0]

    node += 0, (abs(goal[0] - node[0]) + abs(goal[1] - node[1])) * 10
    openlist = [node]
    closedlist = []

    while openlist:
        for f in openlist:
            if node[2] + node[3] >= f[2] + f[3]:
                node = f
                openlist.remove(f)
                bestParent[node[:2]] = []
                if draw: rect(node, "turquoise")
                break

        pos = node[:2]
        g = node[2]

        if draw: rect(node, "pink")
        closedlist.append(node)

        for child in graph[pos][1:]:
            Found = False

            #never updated
            for c in range(len(closedlist)):
                if child == goal and goal in closedlist[c][:2]:
                    path = []
                    bestParent[child] = [(pos[0], pos[1], sum(pos[2:]))]
                    while bestParent[node[:2]]:
                        path.append(node[:2])
                        node = bestParent[node[:2]][0][:2]
                    path.append(node[:2])
                    return path[::-1]
                if closedlist[c][:2] == child:
                    Found = True
                    break
            if Found: continue

            #update in list
            for c in range(len(openlist)):
                t = openlist[c]
                diag = 10 if ((pos[0] - t[0]) + (pos[1] - t[1])) % 2 else 14
                
                if t[:2] == child:
                    if t[2] > g + diag:
                        openlist[c] = t[0], t[1], g + diag, t[3]
                        bestParent[node[:2]] += (t[0], t[1], g + diag + t[3])
                    Found = True
                    break
            if Found: continue

            #append to list
            t = child
            diag = 10 if ((pos[0] - t[0]) + (pos[1] - t[1])) % 2 else 14
            dist = (abs(goal[0] - t[0]) + abs(goal[1] - t[1])) * 10
            t += g + diag, dist
            openlist.append(t)
            rect(t, "turquoise")
            bestParent[node[:2]] += [(t[0], t[1], g + diag + dist)]
                    

def custom(graph, node):
    if graph[node][0] == "G": return [node]
    
    if node not in visited:
        visited.append(node)
        if draw: rect(node)
        for neighbour in graph[node][1:]:
            if ((neighbour[0] - node[0]) + (neighbour[1] - node[1])) % 2:
                isType = custom(graph, neighbour)
                if isType:
                    return [node] + isType
        return []
    return []
