# a very bad pathfinding library

class PathfindingError(Exception)

def findPath(start:tuple,end:tuple,*blocked:list): # uses an *args decorator to accept an unlimited number of non-positional arguments
  blockedCoords = [] # create a list with all the blocked coords
  for blockedList in blocked:
    blockedCoords.extend(blockedList)

  movementVector = [end[0]-start[0], end[1]-start[1]] # define a movementVector based on a move right, up strategy directly between the points
  pathFound = False # then create a variable to track if we have found a path yet

  while not pathFound:
    movementCoords = [start]
    movementCoordsItem = 0
    for x in range(1,movementVector[0]+1):
      movementCoords.append(tuple(movementCoords[movementCoordsItem][0]+1,movementCoords[movementCoordsItem][1]))
      movementCoordsItem += 1
    for y in range(1,movementVector[1]+1):
      movementCoords.append(tuple(movementCoords[movementCoordsItem][0],movementCoords[movementCoordsItem][1]+1))

    # now we should have a list of the coords the player will traverse using the movementVector

    # check if it works
    pathWorks = True
    
    for coord in movementCoords:
      if coord in blockedCoords:
        pathWorks = False
        # fix the error
        coordIndex = movementCoords.index(coord)
        movementCoords.pop(coordIndex)
        movementCoords.insert(tuple(coord[0]-1,coord[1]-1))
        break

    if pathWorks:
      pathFound = True
      break

  if pathFound:
    return movementVector
  else:
    raise PathfindingError('Vector was not verified')
    

    
  
