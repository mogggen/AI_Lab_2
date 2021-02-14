import turtle

s = 10

def rect(p):
    tur = turtle.Turtle()
    
    #setters
    tur.ht()
    tur.up()
    tur.speed(0)
    for i in p:
        if i[2] in (" ", "0"): continue
        x = i[0] * s
        y = i[1] * -s
        c = i[2]
        
        #continue
        tur.fillcolor("gray")

        #position
        tur.goto(x - s / 2, y - s / 2)

        #fill rec
        tur.begin_fill()
        
        tur.setx(x + s / 2)
        tur.sety(y + s / 2)
        tur.setx(x - s / 2)
        tur.sety(y - s / 2)
        tur.end_fill()    



#flags
Found = False

visited = []

queue = []

opened = []
closed = []

def resetFlags():
    global Found
    global visited
    global queue
    global opened
    global closed
    
    Found = False

    visited = []
    queue = []
    opened = []
    closed = []
    
    

def dfs(graph, node):
    global Found
    if graph[node][0] == "G": Found = True
    if graph[node][0] == "X" or Found: return
    #rect([(node[0], node[1], "T")])
    if node not in visited:
        visited.append(node)
        
        for neighbour in graph[node][1:]:
            dfs(graph, neighbour)
    return

def bfs(graph, node):

    visited.append(node)
    queue.append(node)

    while queue:
        h = queue.pop(0) 
        for neighbour in graph[h][1:]:
            if neighbour not in visited:
                visited.append(neighbour)
                if graph[neighbour][0] != "X":
                    queue.append(neighbour)
                if graph[neighbour][0] == "G": return
                #rect([(neighbour[0], neighbour[1], "T")])

def astar(graph, node, fin):
    opened.append(node)

    # Loop until you find the end
    while len(opened) > 0:
        
        for item in opened:
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        opened.pop(current_index)
        closed.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        children = []
        for new_position in [(1, 1), (0, 1), (1, 0), (-1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1)]: # Adjacent squares

            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if maze[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(current_node, node_position)

            children.append(new_node)

        for child in children:

            # Child is on the closed list
            for closed_child in closed:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = (child.position[0] - end_node.position[0]) ** 2 + (child.position[1] - end_node.position[1]) ** 2
            child.f = child.g + child.h

            # A better child is already in the open list
            for open_node in opened:
                if child == open_node and child.g > open_node.g:
                    continue

            opened.append(child)

def custom(graph, node):
    global Found
    if node not in ((0, -1), (0, 1), (-1, 0), (1, 0)): return
    if graph[node][0] == "G": Found = True
    if graph[node][0] == "X" or Found: return
    rect([(node[0], node[1], "T")])
    if node not in visited:
        visited.append(node)
        
        for neighbour in graph[node][1:]:
            if node not in ((node[0], node[1] - 1), (node[0], node[1] + 1), (node[0] - 1, node[1]), (node[0] + 1, node[1])):
            dfs(graph, neighbour)
    return
