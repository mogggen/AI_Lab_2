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
    node_list = {}
    for g in graph:
        if graph[g][0] == 'G':
            finish = g
            break

    for g in graph:
        node_list[g] = Node(round((((finish[0] - g[0]) ** 2 + (finish[1] - g[1]) ** 2) ** .5) * 10), graph[g][1:])
        if graph[g][0] == 'S':
            node_list[g].g = 0
            node_list[g].opened = True

    return node_list


def moveCost(parent, child):
    return 14 if ((parent[0] - child[0]) + (parent[1] - child[1])) % 2 == 0 else 10


def astar(graph, outOfTime, open_list=0):
    is_running = True
    node = 1, 1

    graph[node].opened = True

    while is_running:
        # set loop flag
        is_running = False
        for n in graph:
            if graph[n].opened and not graph[n].closed:
                if graph[node].g or graph[n].g + graph[n].h <= graph[node].g + graph[node].h:
                    node = n
                    graph[node].opened = True
                    open_list += 1
                    is_running = True
            if graph[n].closed and not graph[n].opened:
                open_list -= 1

        input(open_list)

        # return final path
        if graph[node].h == 0:
            is_running = False
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
