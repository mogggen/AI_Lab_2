
def aStar(node, goal):
    openset = set()
    closedset = set()

    openset.add(node)

    while openset:
        node = min(openset, key=lambda o:o.G + o.H)

        if node == goal:
            path = []
            while node.parent:
                path.append(node)
                node = node.parent
            path.append(node)
            return path[::-1]

        openset.remove(node)

        closedset.add(node)

        for child in range(None):
            if child in closedset:
                continue

            if child in openset:
                new_g = node.G + node.move_cost(child)
                if child.G > new_g:
                    child.G = new_g
                    child.parent = node
            else:
                child.G = node.G + node.move_cost(child)
                child.H = len(None)

                child.parent = node

                openset.add(child)