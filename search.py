# Class for each node in the grid
class Node:
    def __init__(self, row, col, is_obs, h):
        self.row = row        # coordinate
        self.col = col        # coordinate
        self.is_obs = is_obs  # obstacle?
        self.g = None         # total cost to come here (previous g + move cost)
        self.h = h            # heuristic
        self.cost = None      # total cost (depend on the algorithm)
        self.parent = None    # previous node


# Search function in general
def search(grid, start, goal, queue_method):
    # Create a new grid to store nodes
    size_row = len(grid)
    size_col = len(grid[0])
    grid_node = [[None for i in range(size_col)] for j in range(size_row)]
    for row in range(size_row):
        for col in range(size_col):
            # manhattan distance from the goal
            h = abs(goal[0] - row) + abs(goal[1] - col) 
            # initialize a node instance and store in the grid
            if grid[row][col]:
                a=0
            else:
                a=1
            grid_node[row][col] = Node(row, col, a, h)
    
    # Start dealing with nodes
    grid_node[start[0]][start[1]].g = 0
    queue = [grid_node[start[0]][start[1]]]
    found = False
    checked = []
    exlore_list = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    # Keep exploding before there is no more nodes
    while queue != []:
        # pop up the next node and put it in the checked list
        cur_node = queue.pop(0)  
        checked.append(cur_node) 
        # check if reach the goal
        if cur_node.row == goal[0] and cur_node.col == goal[1]: 
            found = True
            break

        # explore potential neighbor nodes
        neighbor_nodes = []
        for move_step in exlore_list:
            # move 1 unit manhattan distance
            new_row = cur_node.row + move_step[0]
            new_col = cur_node.col + move_step[1]
            # if inside the boundary and
            # is not obstacle and
            # not visited
            if 0 <= new_row < size_row and \
               0 <= new_col < size_col and \
               not grid_node[new_row][new_col].is_obs and \
               not grid_node[new_row][new_col] in checked:
                neighbor_nodes.append(grid_node[new_row][new_col])

        ######
        # order the queue based on different algorithms
        # the key difference of these algorithms
        queue = queue_method(cur_node, neighbor_nodes, queue)
        ######

    # Get and return the result
    path = []
    steps = 0
    if found:
        steps = len(checked)
        # keep tracing back to get the path
        cur_row, cur_col = goal[0], goal[1]  
        while True:
            # add to path
            path.insert(0, [cur_row, cur_col])
            # check if reach the start
            if cur_row == start[0] and cur_col == start[1]:
                break
            # trace back
            parent_node = grid_node[cur_row][cur_col].parent
            cur_row = parent_node.row
            cur_col = parent_node.col
            
    return found, path, steps

def cost_queue(cur_node, neighbor_nodes, queue, cost_function):
    # Function to order queue based on a cost function
    # used by A* and Dijkstra
    for new_node in neighbor_nodes:
        # new cost
        new_cost = cost_function(cur_node, new_node)
        # if already existed in queue
        if new_node in queue:      
            if new_cost < new_node.cost: # remove existed one if new one is less costly
                queue.remove(new_node)
            else:                        # skip this one if not
                continue
        # append new node
        new_node.g = cur_node.g + 1
        new_node.cost = new_cost
        new_node.parent = cur_node
        queue.append(new_node)
        # sort according to total cost
        queue.sort(key = lambda x:x.cost)
    return queue

def astar(grid, start, goal):
    ### YOUR CODE HERE ###
    # Cost function for Dijkstra
    def astar_cost(cur_node, new_node):
        # cost to move is set to 1 per step
        new_g = cur_node.g + 1 
        # f = g + h
        new_cost = new_g + new_node.h 
        return new_cost
    
    # Function to order queue based on Dijkstra
    def astar_queue(cur_node, neighbor_nodes, queue):
        return cost_queue(cur_node, neighbor_nodes, queue, astar_cost)

    # Search
    found, path, steps = search(grid, start, goal, astar_queue)

    if (found==False):
        print("No path found")
    return path, steps

