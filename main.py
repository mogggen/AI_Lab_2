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
        #print(i)
        if i[2] in (" ", "0"): continue
        x = i[0]
        y = i[1]
        c = i[2]
        w = i[3]
        h = i[4]
        
        #continue
        tur.fillcolor(getColor(c))

        #position
        tur.goto(x - h / 2, y - h / 2)

        #fill rec
        tur.begin_fill()
        
        tur.setx(x + w / 2)
        tur.sety(y + h / 2)
        tur.setx(x - w / 2)
        tur.sety(y - h / 2)
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
    elif c == ' ' or c == '0':
        return "black"
    else:
        return "Unknown token"

def drawMap(karta):
    global s
    nodes = []
    x = 0
    y = 0
    last = ''
    w = 0
    
    for c in karta:
        print(last,end='')
        if last != c:
            if c == '\n':
                nodes += [(x, y, last, w, s)]
                x = 0
                w = 0
                y -= s
                last = c
            else:
                nodes += [(x, y, c, w, s)]
                last = c
                x = x + w
                w = 0
        else:
            w += s       
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
    r = [(1, 1), (0, 1), (1, 0), (-1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1)]
    
    for g in graph:
        for n in r:
            try:
                if graph[g[0] + n[0], g[1] + n[1]][0] in ('0', ' ', 'S', 'G'):
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

    visited = []
    algo.resetFlags()

    #find S
    for v in g:
        if g[v][0] == "S":
            if func == "dfs":
                algo.dfs(visited, g, v)
            elif func == "bfs":
                algo.bfs(visited, g, v)
    tur.write("Press 'Enter' in console to contiue...")

def timefunc(karta, func, itr = 1000):    
    print(func)

#driver code
for i in kartor: #this needs to be an array, not a index
    drawfunc(i, "dfs")
    drawfunc(i, "bfs")
    
    #timefunc(i, "dfs")
    #timefunc(i, "bfs")
