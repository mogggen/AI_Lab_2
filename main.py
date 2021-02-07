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
    #create grid
    for k in karta:
        if k == '\n':
            x = 0
            y += 1
        elif k == '0' or k == ' ':
            graph[(x, y)] = k
##            for i in range(9):
##                if i == 4: continue
##                x + i % 3 - 1, y + i / 3 - 1
            x += 1

    x = 0
    y = 0

#nodes = graph(kartor[0])
#for y in range(16):
    #for x in range(16):
        #print(nodes[(x, y)], end='')
#    print()
drawMap(kartor[0], (-300, -280))

##for y in range(16):
##        for x in range(16):
##            print(nodes[(x, y)], end='')
##        print()
drawMap(kartor[1], (200, -280))
drawMap(kartor[2], (0, 100))
