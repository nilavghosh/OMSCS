# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    visited = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    cellstovisit = [];
    cellstovisit.append([0,goal[0],goal[1]])
    value[goal[0]][goal[1]] = 0;
    visited[goal[0]][goal[1]] = 1
    

    while(len(cellstovisit) > 0):
        cellstovisit.sort()
        cellstovisit.reverse()
        currentcell = cellstovisit.pop()
        

        for idx,movement in enumerate(delta):
            position = [currentcell[0] + 1, currentcell[1] + movement[0], currentcell[2] + movement[1]]
            if(position[1] < len(grid) and position[1] >= 0 and position[2] < len(grid[0]) and position[2] >= 0 and grid[position[1]][position[2]] == 0 and visited[position[1]][position[2]] == 0):
                cellstovisit.append(position)
                visited[position[1]][position[2]] = 1
                value[position[1]][position[2]] = position[0]
                policy[position[1]][position[2]] = delta_name[idx]

    
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    policy[goal[0]][goal[1]] = '*'
    #for i in range(len(value)):
    #    print(value[i])
    for i in range(len(policy)):
        print(policy[i])

if __name__ == "__main__":
    compute_value(grid,goal,cost)
   