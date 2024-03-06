from mcpi.minecraft import Minecraft
from mcpi import block
import random
import houseGen



mc = Minecraft.create() 
x, y, z = mc.player.getPos()

road_type = [block.Block(13), block.Block(48), block.Block(4)]

## check to see if the x point is in the bounds of the house
def checkX(x,z):

    if mc.getBlock(x+1,mc.getHeight(x+1,z),z) == 44 or  mc.getBlock(x-1,mc.getHeight(x-1,z),z) == 44:
        return False

    return True
    
## check to see if the z point is in the bounds of the house

def checkZ(x,z):

    if mc.getBlock(x,mc.getHeight(x,z+1),z+1) == 44 or  mc.getBlock(x,mc.getHeight(x,z-1),z-1) == 44:
        return False

    return True

##place road block
def placeblock(x,z):
     y = mc.getHeight(x,z)
     if mc.getBlock(x,y,z) != 4 or 13 or 48:
        mc.setBlock(x,y,z,random.choice(road_type))
           



## finds the middle point between all the doors 
def midPoint(loc):
    totalx = 0
    totalz = 0

    for doors in loc:
        totalx += doors[0]
        totalz += doors[2]
    
    
    y  = mc.getHeight(totalx/len(loc),totalz/len(loc))
    return [totalx//len(loc), y-10, totalz//len(loc)]



##connect two points with a road function


def roadConnect(x,y,z,mid):
    

    mc.setBlocks(x,y-1,z,x+2,y-1,z,random.choice(road_type))
    ##mc.setBlocks(x-2,y,z,x-2,y,(z+w) + 2,1)
    ##mc.setBlocks(x-2,y,(z+w)+2,(x+l) + 1,y,z,1)

    #connect to midpoint 
    print(mid[0])
    print(mid[2])
    lastz = 0
    lastx = 0

    ## while the x and z value are not equal keep looping
    while x != mid[0] or z != mid[2] :

        print('x = ',x)
        print('z = ',z)

        
        goX = 1
        goZ = 1
        
        if x < mid[0]:
            goX = 1
            if checkX(x+1,z):
                x += 1
                lastx = 1
                placeblock(x,z)
        elif x > mid[0]:
            goX = -1
            if checkX(x-1,z):
                x -= 1
                lastx = -1
                placeblock(x,z)
        
        print(goX)

        if z == mid[2] and ( (goX == 1 and (checkX(x+1,z)==False)) or (goX == -1 and (checkX(x-1,z)==False))):
            if goX == 1:
                while checkX(x+1,z) == False:
                    if lastz == 1:
                        z += 1 
                    elif lastz == -1:
                        z -= 1
                    
                    placeblock(x,z)

                
            if goX == -1:
                while checkX(x-1,z) == False:
                    if lastz == 1:
                        z += 1 
                    elif lastz == -1:
                        z -= 1
                    placeblock(x,z)

            if x > mid[0]:
                x -= 1
                placeblock(x,z)
                x -= 1
                placeblock(x,z)
            elif x < mid[0]:
                x += 1
                placeblock(x,z)
                x += 1
                placeblock(x,z)
                        
           
        
            
        if z < mid[2]:
            goZ = 1
            lastz = 1
            if checkZ(x,z+1):
                z += 1
                placeblock(x,z)
        elif z > mid[2]:
            goZ = -1
            lastz = -1
            if checkZ(x,z-1):
                z -= 1  
                placeblock(x,z)
        
        
        if x == mid[0] and ( (goZ == 1 and (checkZ(x,z+1)==False)) or (goZ == -1 and (checkZ(x,z-1)==False))):
            if goZ == 1:
                while checkZ(x,z+1) == False:
                    if lastx == 1:
                        x += 1 
                    elif lastx == -1:
                        x -= 1
                    
                    placeblock(x,z)

                
            if goZ == -1:
                while checkZ(x,z-1) == False:
                    if lastx == 1:
                        x += 1 
                    elif lastx == -1:
                        x -= 1
                    placeblock(x,z)
            
            if z < mid[2]:
                z +=1
            elif z > mid[2]:
                z-=1 

            placeblock(x,z)

        if checkX(x+1,z) == False and checkX(x-1,z) == False and checkZ(x,z+1) == False and checkZ(x,z-1) == False:
            break


def placeRoads(houseLocations):
    doors = []


    
    for houses in houseLocations:
        doorloc = houses.getDoorLocation()
        doors.append(doorloc)

    pPos = midPoint(doors)
    print(pPos)

    mc.setBlocks(pPos[0],pPos[1]-5,pPos[2],pPos[0],pPos[1],pPos[2],random.choice(road_type))


    while checkX(pPos[0],pPos[2]) == False:
        print('!! in middle !!!')
        pPos[0] += 1 
        


    for door in doors:
        roadConnect(door[0]-2,door[1],door[2],pPos)