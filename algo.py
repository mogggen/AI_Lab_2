from turtle import Turtle, Screen

s = 10
screen = Screen()
screen.tracer(0, 0)

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

class Node:
    
    def __init__(self, pos):
        self.x, self.y = pos
        self.parent = None
        self.g = 0
        self.h = 0

        self.Neighbours = []

    def __eq__(self, o):
        return (self.x, self.y) == (o.x, o.y)

    def __ne__(self, o):
        return (self.x, self.y) != (o.x, o.y)

    def setNeighbours(self, graph):
        if self.Neighbours: return
        for n in graph[self.x, self.y][1:]:
            self.Neighbours += [Node(n)]

    
def astar(graph, node):
    goal = Node([goal for goal in graph if graph[goal][0] == "G"][0])
    node = Node(node)
    node.g, Node.h = 0, -1
    openlist = [node]
    closedlist = []

    while openlist:
        node = min(openlist, key=lambda o: o.g + o.h)
        if node == goal:
            path = []
            while node.parent:
                path.append((node.x, node.y))
                node = node.parent
            path.append((node.x, node.y))
            return path[::-1]

        openlist.remove(node)
        closedlist.append(node)
        
        if draw: rect((node.x, node.y), "pink")
        node.setNeighbours(graph)
        
        for child in node.Neighbours:
            Found = False


            #append to list
            for other in closedlist:
                if child == other:
                    continue
                else: 
                    Found += 1
                    if Found > 1: print("dö")
                    break
            if Found: continue

            #update in list
            for other in openlist:
                if child == other:
                    diag = 10 if ((node.x - child.x) + (node.y - child.y)) % 2 else 14
                    if child.g < node.g + diag:
                        child.g = node.g + diag
                        other.g = node.g + diag
                        child.parent = node
                        other.parent = node
                    Found = True
                    break
            if Found: continue
            
            
            
            if not Found:
                diag = 10 if ((node.x - child.x) + (node.y - child.y)) % 2 else 14
                dist = ((goal.x - node.x)**2 + (goal.y - node.y)**2)
                child.g, child.h, child.parent = node.g + diag, dist, node
                
                openlist.append(child)
                if draw: rect((child.x, child.y), "turquoise")
                    

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
