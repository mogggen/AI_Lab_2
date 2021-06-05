from turtle import Turtle, Screen
from time import time

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


class Node:
    def __init__(self, h=None, neighbours=None):
        self.g = None
        self.h = h
        self.opened = False
        self.closed = False
        self.neighbours = neighbours
        self.parent = None


def convertGraphToNodes(graph):
    if not graph:
        return
    finish = None
    nodeList = {}
    for g in graph:
        if graph[g][0] == 'G':
            nodeList[g] = Node(0, graph[g][1:])
            finish = g
            break

    for g in graph:
        if graph[g][0] == 'S':
            nodeList[g] = Node(round((((finish[0] - g[0]) ** 2 + (finish[1] - g[1]) ** 2) ** .5) * 10), graph[g][1:])
            nodeList[g].g = 0
            nodeList[g].opened = True

        if graph[g][0] == ' ':
            nodeList[g] = Node(round((((finish[0] - g[0]) ** 2 + (finish[1] - g[1]) ** 2) ** .5) * 10), graph[g][1:])

    return nodeList


def moveCost(parent, child):
    return 14 if ((parent[0] - child[0]) + (parent[1] - child[1])) % 2 == 0 else 10


def astar(graph, outOfTime, openList=[]):
    isRunning = True
    node = 1, 1
    print(id(graph))
    graph[node].opened = True

    while isRunning:
        # set loop flag
        isRunning = False
        # openList = []
        for n in graph:
            if graph[n].opened:
                if graph[node].g or graph[n].g + graph[n].h <= graph[node].g + graph[node].h:
                    node = n
                    graph[node].opened = True
                # openList.append(n)
                isRunning = True

        # return final path
        if graph[node].h == 0 or time() > outOfTime:
            path = [node]
            while graph[node].parent:
                path.append(graph[node].parent)
                node = graph[node].parent
            return path

        graph[node].opened = False

        graph[node].closed = True

        for n in graph[node].neighbours:
            if graph[n].closed:
                rect(n, "black")
                continue

            if graph[n].opened:
                if graph[n].g < graph[node].g + moveCost(node, n):
                    graph[n].g = graph[node].g + moveCost(node, n)
                    graph[n].parent = node

            else:
                rect(n)
                graph[n].g = graph[node].g + moveCost(node, n)
                graph[n].parent = node
                graph[n].opened = True
