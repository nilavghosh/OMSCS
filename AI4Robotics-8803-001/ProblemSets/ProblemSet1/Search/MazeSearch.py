# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0], # go up
         [0,-1], # go left
         [1, 0], # go down
         [0, 1]] # go right
delta_name = ['^', '<', 'v', '>']

def findopenspaces(openspace, grid, cost, visitedgrid):
    openspaces = []
    for movement in delta:
        position = [openspace[0] + 1, openspace[1] + movement[0], openspace[2] + movement[1]]
        if(position[1] < len(grid) and position[1] >= 0 and position[2] < len(grid[0]) and position[2] >= 0 and grid[position[1]][position[2]] == 0 and visitedgrid[position[1]][position[2]] == 0):
            openspaces.append(position)
            visitedgrid[position[1]][position[2]] = 1
   
    return openspaces


def search(grid,init,goal,cost):
    expandcount = 0
    visitedgrid = [[ 0 for j in range(len(grid[0]))] for i in range(len(grid))] 
    expansiongrid = [[ -1 for j in range(len(grid[0]))] for i in range(len(grid))] 
    openlist = [[0,init[0],init[1]]]
    visitedgrid[init[0]][init[1]] = 1
    path = None
    while(len(openlist) > 0 and path == None):
        refelement = openlist[0]
        leastgIndex = 0
        #for idx,element in enumerate(openlist):
        #    if element[0] < refelement[0]:
        #        refelement = element
        #        leastgIndex = idx
        openlist.sort()
        openlist.reverse()
        next = openlist.pop()
        expansiongrid[next[1]][next[2]] = expandcount
        if(next[1] == goal[0] and next[2] == goal[1]):
                path = space
                break
        openspaces = findopenspaces(next,grid, cost, visitedgrid)

        for space in openspaces:
            openlist.append(space)
            
        expandcount += 1
        #openlist.remove(next)
    if(path == None):
        path = "fail"
    for i in range(len(expansiongrid)):
        print(expansiongrid[i])
    #return expansiongrid

if __name__ == "__main__":
    search(grid,init,goal,cost)