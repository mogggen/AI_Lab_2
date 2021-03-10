import algo
from turtle import Turtle, Screen
import time

s = 10
screen = Screen()
screen.tracer(0, 0)

#destination
def rect(p):
    tur = Turtle()
    
    #setters
    tur.ht()
    tur.up()
    tur.speed(0)
    for i in p:        
        if i[2] in (" ", "0"): continue
        x = i[0]
        y = i[1]
        
        #continue
        tur.fillcolor(getColor(i[2]))

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

foo = open("Map1.txt", 'r')

ofo = open("Map2.txt", 'r')
oof = open("Map3.txt", 'r')
kartor = foo.read(), ofo.read(), oof.read()

def getColor(c):
    if c == 'X':
        return "blue"
    elif c == 'S':
        return "red"
    elif c == 'G':
        return "green"
    elif c == 'P':
        return "yellow"
    else:
        return "Unknown token"

def drawMap(karta):
    global s
    nodes = []
    x = 0
    y = 0
    
    for c in karta:
        if c == '\n':
            x = 0
            y -= s
        else:
            nodes += [(x, y, c)]
            x += s
    return nodes

def makeGraph(karta):
    graph = {}
    x = 0
    y = 0
    #create grid
    for k in karta:
        if k == '\n':
            x = 0
            y += 1
        else:
            graph[x, y] = [k]
            x += 1
    return graph

def connectGraph(graph):
    r = ((1, 1), (0, 1), (1, 0), (-1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1))
    
    for g in graph:
        for n in r:
            try:
                if "X" not in (graph[g[0] + n[0], g[1]][0], graph[g[0], g[1] + n[1]][0], graph[g[0] + n[0], g[1] + n[1]][0]):
                    graph[g] += [(g[0] + n[0], g[1] + n[1])]
            except KeyError:
                continue
    return graph

def drawfunc(karta, func):
    global screen
    screen.clear()
    screen.tracer(0, 0)
    rect(drawMap(karta))
    screen.update()

    g = makeGraph(karta)
    g = connectGraph(g)
    algo.drawSearch(True)
    algo.resetFlags()
    
    path = []
    for v in g:
        if g[v][0] == "S":
            if func == "dfs":
                path = algo.dfs(g, v)
                
            elif func == "bfs":
                path = algo.bfs(g, v)
            elif func == "A*":
                path = algo.astar(g, v)
            elif func == "custom":
                path = algo.custom(g, v)
            break

    for ss in range(len(path)):
        path[ss] = (path[ss][0] * s, path[ss][1] * -s, 'P')
    rect(path)
    print(path)
    return path

def timefunc(karta, func):
    g = makeGraph(karta)
    g = connectGraph(g)
    algo.drawSearch(False)
    algo.resetFlags()
    
    for v in g:
        if g[v][0] == "S":
            if func == "dfs":
                start = time.time()
                algo.dfs(g, v)
                return time.time() - start
            elif func == "bfs":
                start = time.time()
                algo.bfs(g, v)
                return time.time() - start
            elif func == "A*":
                start = time.time()
                algo.astar(g, v)
                return time.time() - start
            elif func == "custom":
                start = time.time()
                algo.custom(g, v)
                return time.time() - start

#driver code
itr = 1000
for i in enumerate(kartor[1:]):
    print("Map " + str(i[0] + 1))

    #print("Depth-First-Search")
    #drawfunc(i[1], "dfs")
    #input()
    
    #print("Bredth-First-Search")
    #drawfunc(i[1], "bfs")
    #input()
    
    print("A*")
    drawfunc(i[1], "A*")
    #input()
    
    #print("custom Algorithm")
    #drawfunc(i[1], "custom")
    #input()

    dfsTime = 0
    bfsTime = 0
    AstarTime = 0
    customTime = 0

    for it in range(itr):
        break
        dfsTime += timefunc(i[1], "dfs")
        bfsTime += timefunc(i[1], "bfs")
        AstarTime += timefunc(i[1], "A*")
        customTime += timefunc(i[1], "custom")
    
    #print(dfsTime / itr)
    #print(bfsTime / itr)
    #print(AstarTime / itr)
    #print(customTime / itr)
    #input()