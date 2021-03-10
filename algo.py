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
    bestParent = {node: []} # current: all parent (pos, f)
    goal = [goal for goal in graph if graph[goal][0] == "G"][0]

    node += 0, (abs(goal[0] - node[0]) + abs(goal[1] - node[1])) * 10
    openlist = [node]
    closedlist = []

    while openlist:
        for f in openlist:
            if node[2] + node[3] >= f[2] + f[3]:
                node = f
                openlist.remove(f)
                break

        pos = node[:2]
        g = node[2]

        if pos == goal:
            path = []
            while bestParent[node[:2]]:
                path.append(node[:2])
                node = bestParent[node[:2]][0][:2]
            path.append(node[:2])
            return path[::-1]

        if draw: rect(node, "black")
        closedlist.append(node)


        for child in graph[pos][1:]:
            Found = False

            #never updated
            for c in range(len(closedlist)):
                if closedlist[c][:2] == child:
                    Found = True
                    break
            if Found: continue

            #update in list
            for c in range(len(openlist)):
                t = openlist[c]
                diag = 10#(14 if ((pos[0] - t[0]) + (pos[1] - t[1])) % 2 else 10)

                if t[:2] == child:
                    if t[2] > g + diag:
                        openlist[c] = t[0], t[1], g + diag, t[3]
                        bestParent[node[:2]] += (t[:2], g + diag + t[3])
                    Found = True
                    break
            if Found: continue

            #append to list
            t = child
            diag = 10#14 if ((pos[0] - t[0]) + (pos[1] - t[1])) % 2 else 10)
            dist = (abs(goal[0] - t[0]) + abs(goal[1] - t[1])) * 10
            t += g + diag, dist
            openlist.append(t)
                    

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