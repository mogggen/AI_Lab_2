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
Found = False
counter = 0

def resetFlags():
    global Found
    global counter
    Found = False
    counter = 0
    

def dfs(visited, graph, node):
    global Found
    global counter
    counter += 1
    if graph[node][0] == "G": Found = True
    if graph[node][0] == "X" or Found: return
    rect([(node[0], node[1], "T")])
    if node not in visited:
        visited.append(node)
        
        for neighbour in graph[node][1:]:
            dfs(visited, graph, neighbour)
    return counter

queue = []

def bfs(visited, graph, node):
    global Found
    global counter
    counter += 1
    if graph[node][0] == "G": Found = True
    if graph[node][0] == "X" or Found: return
    rect([(node[0], node[1], "T")])
    visited.append(node)
    queue.append(node)

    while queue:
        print(queue)
        h = queue.pop(0) 

    for neighbour in graph[h][1:]:
        #print(graph[h])
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)
    return counter
