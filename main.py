import algo
from turtle import Turtle, Screen
from time import time

s = 10
screen = Screen()
screen.tracer(0, 0)


# destination
def rect(p):
    tur = Turtle()

    # setters
    tur.ht()
    tur.up()
    tur.speed(0)
    for i in p:
        if i[2] in (" ", "0"): continue
        x = i[0]
        y = i[1]

        # continue
        tur.fillcolor(getColor(i[2]))

        # position
        tur.goto(x - s / 2, y - s / 2)

        # fill rec
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
fof = open("Map4.txt", 'r')
kartor = foo.read(), ofo.read(), oof.read(), fof.read()


def getColor(c):
    if c == 'X':
        return "blue"
    elif c == 'S':
        return "red"
    elif c == 'P':
        return "green"
    elif c == 'G':
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
    # create grid
    for k in karta:
        if k == '\n':
            x = 0
            y += 1
        else:
            graph[x, y] = [k]
            x += 1
    return graph


def connectGraph(graph):
    r = ((1, 1), (1, 0), (0, 1), (-1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1))

    for g in graph:
        for n in r:
            try:
                if graph[g[0] + n[0], g[1] + n[1]][0] != "X":
                    graph[g] += [(g[0] + n[0], g[1] + n[1])]
            except KeyError:
                pass
    return graph


def drawfunc(karta):
    screen.clear()
    screen.tracer(0, 0)
    rect(drawMap(karta))
    screen.update()

    g = makeGraph(karta)
    g = connectGraph(g)
    g = algo.convertGraphToNodes(g)

    path = []

    while True:
        outOfTime = time() + 5
        path = algo.astar(g, outOfTime)

        for ss in range(len(path)):
            path[ss] = (path[ss][0] * s, path[ss][1] * -s, 'P')
        rect(path)
        print(path)
        break


# driver code
for i in enumerate(kartor[:]):
    print("Map " + str(i[0] + 1))
    drawfunc(i[1])
    input()
