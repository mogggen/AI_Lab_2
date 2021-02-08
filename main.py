import node
import dfs
import turtle

s = 10

#destination
def rect(p, place="", size = s):
    tur = turtle.Turtle()
    
    #setters
    tur.ht()
    tur.up()
    tur.speed(0)
    for i in p:
        if i[2] in (" ", "0"): continue
        x = i[0]
        y = i[1]
        c = i[2]
        
        #continue
        tur.fillcolor(getColor(c))

        #position
        tur.goto(x - size / 2, y - size / 2)

        #fill rec
        tur.begin_fill()
        
        tur.setx(x + size / 2)
        tur.sety(y + size / 2)
        tur.setx(x - size / 2)
        tur.sety(y - size / 2)
        tur.end_fill()
        
    if place:
        tur.write(place)

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
        return "unknown token"

def drawMap(karta):
    global s
    nodes = []
    x = 0
    y = 0
    
    for c in karta:
        x += s
        if c == '\n':
            x = 0
            y -= s
        else:
            nodes += [(x, y, c)]
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
    r = [(1, 1), (1, 0), (0, 1), (-1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1)]
    
    for g in graph:
        for n in r:
            try:
                if graph[g[0] + n[0], g[1] + n[1]][0] in ('0', ' ', 'S', 'G'):
                    graph[g] += [(g[0] + n[0], g[1] + n[1])]
            except KeyError:
                continue
    return graph

def drawDFS(karta):
    tur = turtle.Turtle()
    tur.screen.clear()    
    drawMap(karta)
    g = makeGraph(karta)
    g = connectGraph(g)
    visited = set()

    #find S
    for v in g:
        if g[v][0] == "S":
            print("DFS: ", dfs.dfs(visited, g, v), "function calls")
            break

def drawBFS(karta):
    tur = turtle.Turtle()
    tur.screen.clear()    
    drawMap(karta)
    g = makeGraph(karta)
    g = connectGraph(g)
    
    #find S
    for v in g:
        if g[v][0] == "S":
            print("BFS: ", dfs.bfs([], g, v), "function calls")
            break

#driver code
for i in kartor[:-2]: #this needs to be an array, not a index
    input(drawDFS(i))
