from turtle import Turtle, Screen

s = 10
screen = Screen()
screen.tracer(0, 0)


def rect(p, c="gray"):
    tur = Turtle()

    # setters
    tur.ht()
    tur.up()
    tur.speed(0)

    x = p[0] * s
    y = p[1] * -s

    # continue
    tur.fillcolor(c)

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
    return x, y


# flags
draw = False
visited = []
closed = []


def resetFlags():
    global visited
    visited = []


def drawSearch(boolean):
    global draw
    draw = boolean


class Node:
    def __init__(self, pos):
        self.pos = pos

        self.g = 0
        self.h = 0
        self.opened = False
        self.closed = False
        self.parent = None


def astar(graph, node):
    if not graph or node not in graph:
        return []

    isRunning = True
    node.opened = True
    best = node

    while isRunning:
        # set loop flag
        isRunning = False
        for n in graph:
            if n.opened:
                isRunning = True
                if n.g + n.h <= best.g + best.h:
                    best = n

        # return final path
        if node.h == 0:
            path = [node]
            while node.parent:
                path.append(node.parent)
                node = node.parent
            return path

        # if closed


    rect((child.x, child.y), "turquoise")
