import algo
import turtle
import time

s = 10

#destination
def rect(p):
    tur = turtle.Turtle()
    
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
        
    rect(nodes)
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
            graph[(x, y)] = [k]
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
    tur = turtle.Turtle()
    tur.screen.clear()
    drawMap(karta)
    g = makeGraph(karta)
    g = connectGraph(g)

    algo.showSearch(True)
    algo.resetFlags()

    #find S
    for v in g:
        if g[v][0] == "S":
            if func == "dfs":
                algo.dfs(g, v)
            elif func == "bfs":
                algo.bfs(g, v)
            elif func == "A*":
                for vv in g:
                    if g[vv][0] == "G":
                        algo.astar(g, v, vv)
            elif func == "custom":
                algo.custom(g, v)

def timefunc(karta, func):
    g = makeGraph(karta)
    g = connectGraph(g)
    
    algo.showSearch(False)
    algo.resetFlags()
    
    #find S
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
                #find G
                for vv in g:
                    if g[vv][0] == "G":
                        start = time.time()
                        algo.astar(g, v, vv)
                        return time.time() - start
            elif func == "custom":
                start = time.time()
                algo.custom(g, v)
                return time.time() - start
#driver code
itr = 100
for i in enumerate(kartor):
    print("Map" + str(i[0] + 1))
    drawfunc(i[1], "dfs")
    drawfunc(i[1], "bfs")
    drawfunc(i[1], "A*")
    drawfunc(i[1], "custom")
    
    dfsTime = 0
    bfsTime = 0
    AstarTime = 0
    customTime = 0

    for it in range(itr):
        dfsTime += timefunc(i[1], "dfs")
        bfsTime += timefunc(i[1], "bfs")
        AstarTime += timefunc(i[1], "A*")
        customTime += timefunc(i[1], "custom")

    print(dfsTime / itr)
    print(bfsTime / itr)
    print(AstarTime / itr)
    print(customTime / itr)
