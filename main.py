import node
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
        if i[2] == " " or i[2] == "0": continue
        x = i[0]
        y = i[1]
        c = i[2]
        
        print(x, y, getColor(c), sep=',')
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
    return 0

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

def drawMap(karta, at):
    global s
    nodes = []
    x = at[0]
    y = at[1]
    
    for c in karta:
        x += s
        if c == '\n':
            x = at[0]
            y -= s
        else:
            nodes += [(x, y, c)]
    rect(nodes)
    return nodes

def graph(karta):
    graph = {}
    x = 0
    y = 0
    for k in karta:
        x += 1
        if k == '\n':
            x = 0
            y += 1
        else:
            graph[(x, y)] = k
    return graph

print(graph(kartor[0]))
nodes = graph(kartor[0])
drawMap(kartor[0], (-300, -280))

found = False
def DFS(pos, nodes):
    global found
    if nodes[pos] == "G": found = True
    if nodes[pos] == "X" or found:
        return
    DFS((x + 1, y - 1), nodes) # 3
    DFS((x + 1, y), nodes) # 6
    DFS((x, y - 1), nodes) # 2
    DFS((x - 1, y - 1), nodes) # 1
    DFS((x + 1, y + 1), nodes) # 9
    DFS((x, y + 1), nodes) # 8
    DFS((x - 1, y), nodes) # 4
    DFS((x - 1, y + 1), nodes) # 7
        
DFS((1, 1), nodes)
#drawMap(kartor[1], (200, -280))
#drawMap(kartor[2], (0, 100))
