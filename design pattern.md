## First, append the starting node to the open list.
## Repeat the following:
1. Look for the lowest F cost node on the open list. We refer to this as the current node.
2. Move it to the closed list.
3. For each of the nodes adjacent to this current node.
    * If it is not walkable or if it is on the closed list, ignore it. Otherwise do the following.
    * If it isn’t on the open list, add it to the open list. Make the current node the parent of this node. Record the F, G, and H costs of the node.
    * If it is on the open list already, check to see if this path to that node is better, using G cost as the measure. A lower G cost means that this is a better path.
    * If so, change the parent of the node to the current node, and recalculate the G and F scores of the node.
    * If you are keeping your open list sorted by F score, you may need to resort the list to account for the change.
## Stop when you:
Add the target node to the closed list, in which case the path has been found.
Save the path. Working backwards from the target node, go from each node to its parent node until you reach the starting node. That is your path.