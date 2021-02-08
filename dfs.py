import turtle

s = 10

def rect(p, place="", size = s):
    tur = turtle.Turtle()
    
    #setters
    tur.ht()
    tur.up()
    tur.speed(0)
    for i in p:
        x = i[0] * s + s
        y = i[1] * -s
        c = i[2]
        
        #continue
        tur.fillcolor("gray")

        #position
        tur.goto(x - size / 2, y - size / 2)

        #fill rec
        tur.begin_fill()
        
        tur.setx(x + size / 2)
        tur.sety(y + size / 2)
        tur.setx(x - size / 2)
        tur.sety(y - size / 2)
        tur.end_fill()

#flags


def dfs(visited, graph, node, first = True, Found = False, counter = 0):
    if first:
        Found = False
        counter = 0
        first = False

    counter += 1
    if graph[node][0] == "G": Found = True
    if graph[node][0] == "X" or Found: return
    rect([(node[0], node[1], "Dummy")])
    if node not in visited:
        visited.add(node)
        
        for neighbour in graph[node][1:]:
            dfs(visited, graph, neighbour, first, Found, counter)
    return counter

queue = []

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    h = queue.pop(0) 

    for neighbour in graph[h][1:]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
