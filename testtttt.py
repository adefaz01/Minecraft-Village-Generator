from re import X
from tabnanny import check
from mcpi.minecraft import Minecraft
import random

from queue import PriorityQueue


from mcpi.minecraft import Minecraft, Block, Entity, Vec3
from mcpi import minecraft, block, entity, vec3
import random





# testing location: -6, 82, 1

mc = Minecraft.create()

Px, Py, Pz = mc.player.getTilePos()

mid = [Px,Py,Pz,Px+60,Py,Pz+60]

plots = set()

MIN_OFFSET = 6

# creates platform for testing
#mc.setBlocks(Px + 60, Py - 1, Pz + 60, Px, Py - 1, Pz, 1)

# Clears previous test
#mc.setBlocks(Px + 100, Py, Pz + 100, Px, Py, Pz, 0)

# Plot object 
class Plot:

    def __init__ (self, x, z, dx, dz):
        self.x = x
        self.z = z
        self.dx = dx
        self.dz = dz


# Checks if a new plot overlaps with any existing plots
def Overlap(Plot, plots):

    overlaps = False

    for oldPlot in plots:

        if (oldPlot.x + oldPlot.dx + MIN_OFFSET) < Plot.x:
            continue # continue leaves if statement but not for loop

        elif oldPlot.x > (Plot.x + Plot.dx + MIN_OFFSET):
            continue

        elif (oldPlot.z + oldPlot.dz + MIN_OFFSET) < Plot.z:
            continue
            
        elif oldPlot.z > (Plot.z + Plot.dz + MIN_OFFSET):
            continue
            
        else:
            overlaps = True # All were false meaning that new plot overlaps

    return overlaps


# generates number of houses in village
NUM_HOUSES = 5
for i in range(NUM_HOUSES):

    print('RUNNING!')

    # chooses random width and length for house
    randW = random.randint(8, 12)
    randL = random.randint(8, 12)
    
    # chooses random location in village area for house
    randX = random.randint(Px, Px + 60 - randW)
    randZ = random.randint(Pz, Pz + 60 - randL)

    # ensures first house is always added to list and all subsiquent ones are comapred
    if i > 1:

        overlaps = Overlap(Plot(randX, randZ, randW, randL), plots)
        counter = 0

        # overlaps is only true when plots overlap
        while overlaps == True:
            
            if counter < 1000:

                counter += 1
                print(f'OVERLAP! {NUM_HOUSES}, {counter}')
                
                # chooses random width and length for house
                randW = random.randint(8, 12)
                randL = random.randint(8, 12)
                
                # chooses random location in village area for house
                randX = random.randint(Px + 0, Px + 60 - randW)
                randZ = random.randint(Pz + 0, Pz + 60 - randL)

                # runs new overlap test with new values
                overlaps = Overlap(Plot(randX, randZ, randW, randL), plots)
            else:
                break

        else: # test passed and plot can be added

            plots.add(Plot(randX, randZ, randW, randL))   

    else: # first plot is always added
        plots.add(Plot(randX, randZ, randW, randL))



# Checks average height of a given plot
def heightCheck(Plot):

    avgHeight = 0
    counter = 0

    for i in range(Plot.x, Plot.x + Plot.dx):
        for j in range(Plot.z, Plot.z + Plot.dz):

            avgHeight += mc.getHeight(i, j)
            counter += 1

    return (avgHeight // counter)


# loops through plots and places blocks on location










##function takes in a list of two x,y,z co-ordinates and returns a list of one x,y,z co-ordinate of the middle point
def middle(x):
    return [(x[0] + x[3])/2,x[1],(x[2] + x[5]) / 2]

## code that places a wall in the middle of a house based on what the middle function returns
    ##   mid = middle(x,y,z,x,y,z)
    ##   mc.setBlocks(mid[0],mid[1],mid[2] - (w/2) + 1 ,mid[0],mid[1] + 5, mid[2] + (w/2),1)



##function takes in a list of two x,y,z co-ordinates and returns a list of one x,y,z co-ordinate of the middle point
def middle(x):
    return [(x[0] + x[3])/2,x[1],(x[2] + x[5]) / 2]




#places wall horizontally in the middle of the house
##takes the middle point and width of the house as arguments 

def place_Horizontal(mid,w):
    
       
        mc.setBlocks(mid[0],mid[1],mid[2] - (w/2) + 1 ,mid[0],mid[1] + 5, mid[2] + (w/2) - 1,1)

        ##generates Random location for the hallway in the wall
        hallway_pos = random.randint(1, (int(w) - 2) - 1)

        ## check to make sure hallway doesn't spawn in the middle of the wall
        if hallway_pos == ((int(w) - 2) - 1 // 2) + 1 or hallway_pos == ((int(w) - 2) - 1 // 2) :
            hallway_pos += 1


        mc.setBlock(mid[0], mid[1] + 2, (mid[2] - (w/2) + 1)  + hallway_pos, 0)
        mc.setBlock(mid[0], mid[1] + 1, (mid[2] - (w/2) + 1) + hallway_pos, 0)

## places wall vertically in the middle of the house 
def place_vertical(mid,l):

    
    mc.setBlocks(mid[0] - (l/2) + 1,mid[1],mid[2],mid[0] + (l/2) - 1,mid[1] + 5, mid[2],1)



    ##generates Random location for the hallway in the wall
    hallway_pos = random.randint(1, (int(l) - 2) - 1)



    ## check to make sure hallway doesn't spawn in the middle of the wall
    if hallway_pos == ((int(l) - 2) - 1 // 2) + 1 or hallway_pos == ((int(l) - 2) - 1 // 2) :
        hallway_pos += 1

    

    mc.setBlock(mid[0]  - (l/2) + 1  + hallway_pos, mid[1] + 2, mid[2], 0)
    mc.setBlock(mid[0]  - (l/2) + 1  + hallway_pos, mid[1] + 1, mid[2], 0)


    

## recursive function to build walls in the house
def place_walls(split,mid,l,w,wall):

    ## min length and width of the house to stop function 
    if l <= 4 or w <= 4:
        return 
    
    ## chance the function will stop splitting early 
    if random.random() < 0.2:
        return

   
    if wall == 1:
        place_Horizontal(mid,w)

        if split == 'right':
            mid = middle([mid[0],mid[1],mid[2],mid[0] + l//2,mid[1],mid[2]])    
        elif split == 'left':
            mid = middle([mid[0],mid[1],mid[2],mid[0] - l//2,mid[1],mid[2]])    
        
        l = l/2

        if w > 6:
            place_walls(split,mid,l,w,2)


    elif wall == 2:
        place_vertical(mid,l)

        if split == 'right':
            mid = middle([mid[0],mid[1],mid[2],mid[0],mid[1],mid[2] + w//2])
        elif split == 'left':
            mid = middle([mid[0],mid[1],mid[2],mid[0],mid[1],mid[2] - w//2])
    
        w = w/2

        if l > 6:
            place_walls(split,mid,l,w,1)
    

        


def houseTest(x,y,z,x1,z1):

    roof_type = [0, 1, 3, 4, 5]
    
    l = x1
    w = z1

    # Creates a flat grass surface
    ##mc.setBlocks(x - 3, y - 1, z - 3, x + 15, y - 1, z + 15, 2)
   ## mc.setBlocks(x - 3, y, z - 3, x + 15, y + 20, z + 15, 0)

    # Chooses a random block and builds structure of house
    levels = random.randint(1, 3)
    plank_type = random.randint(0, 6)
    mc.postToChat(levels)
    mc.setBlocks(x, y - 1, z, x + l, y + 3, z + w, 5, plank_type)
    
    

    #Hollows out the inside
    mc.setBlocks(x + 1, y, z + 1, x + (l - 1), y + 2, z + (w - 1), 0)
    
    wall = random.randint(1,2)
    house_Cordinates = [x, y - 1, z, x + l, y + 3, z + w]
    mid = middle(house_Cordinates)
    place_walls('right',mid,l,w,wall)
    place_walls('left',mid,l,w,wall)



    






    



    # Randomly choose IDs for Log Beams
    log_type = random.randint(5, 6)
    
    if log_type == 5:
        log = 162
        log_type = 0
    elif log_type == 6:
        log = 162
        log_type = 1
    else:
        log = 17

    # Builds log beams
    mc.setBlocks(x - 1, y - 1, z - 1, x - 1, y + 3, z - 1, log, log_type)
    mc.setBlocks(x - 1, y - 1, z + (w + 1), x - 1, y + 3, z + (w + 1), log, log_type)
    mc.setBlocks(x + (l + 1), y - 1, z - 1, x + (l + 1), y + 3, z - 1, log, log_type)
    mc.setBlocks(x + (l + 1), y - 1, z + (w + 1), x + (l + 1), y + 3, z + (w + 1), log, log_type)

    # Builds roof from a random block chosen from the roof type list
    mc.setBlocks(x - 1, y + 4, z - 1, x + (l + 1), y + 4, z + (w + 1), 44, roof_type[random.randint(0, 4)])

    # Creates random door position and places it
    door_pos = random.randint(2, l - 2)
    not_door_pos = [l-2//2,w-2//2,(l-2//2)//2,(w-2//2)//2,l-2//2 + 1,w-2//2 + 1,((l-2//2)//2) + 1,((w-2//2)//2) + 1]


    
    while door_pos in not_door_pos:
        door_pos = random.randint(1, l - 2)



    mc.setBlock(x, y + 1, z + door_pos, 64, 8)
    mc.setBlock(x, y, z + door_pos, 64, 0)

    ## variable to store location of door 
    doorLocation = (int(x),int(y),int(z + door_pos))

    # Windows

    #mc.setBlocks(x + 4, y + 1, z - 2, x + 4, y + 2, z - 3, 20)
    #mc.setBlocks(x + 4, y + 1, z + 2, x + 4, y + 2, z + 3, 20)


    return doorLocation
    
class house:
    def __init__(self,x,y,z,length,width):
        self.x = x
        self.y = y
        self.z = z
        self.doorLocation = None

        ## can add if needed 
        self.length = length
        self.width = width

    def build(self):
        self.doorLocation = houseTest(self.x,self.y,self.z,self.length,self.width)
    
    def getDoorLocation(self):
        return self.doorLocation
    
    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

        
houseLoc = []


for plot in plots:
    
    print(f'{plot.x},{plot.z},{plot.dx},{plot.dz}')

    height = heightCheck(plot)

    mc.setBlocks(plot.x - 2, height, plot.z - 2,\
         (plot.x + plot.dx) + 2, height + 30, (plot.z + plot.dz) + 2, 0)



    House = house(plot.x,height,plot.z,plot.dx,plot.dz)
    House.build()
    houseLoc.append(House)



    ##mc.setBlocks(plot.x, height, plot.z,\
        ##plot.x + plot.dx, height, plot.z + plot.dz, 57)


def checkX(x,z):

    if mc.getBlock(x+1,mc.getHeight(x+1,z),z) == 44 or  mc.getBlock(x-1,mc.getHeight(x-1,z),z) == 44:
        return False

    return True
    

def checkZ(x,z):

    if mc.getBlock(x,mc.getHeight(x,z+1),z+1) == 44 or  mc.getBlock(x,mc.getHeight(x,z-1),z-1) == 44:
        return False

    return True
def placeblock(x,z):
     y = mc.getHeight(x,z)
     mc.setBlock(x,y,z,57)


## finds the middle point between all the doors 
def midPoint(loc):
    totalx = 0
    totalz = 0

    for doors in loc:
        totalx += doors[0]
        totalz += doors[2]
    
    
    y  = mc.getHeight(totalx/len(loc),totalz/len(loc))
    return [totalx//len(loc), y-10, totalz//len(loc)]
        
    



def roadConnect(x,y,z,mid):
    

    mc.setBlocks(x,y-1,z,x+2,y-1,z,57)
    ##mc.setBlocks(x-2,y,z,x-2,y,(z+w) + 2,1)
    ##mc.setBlocks(x-2,y,(z+w)+2,(x+l) + 1,y,z,1)

    #connect to midpoint 
    print(mid[0])
    print(mid[2])
    lastz = 0
    lastx = 0

    ## while the x and z value are not equal keep looping
    while x != mid[0] or z != mid[2]:

        print('x = ',x)
        print('z = ',z)

        
        goX = 0
        goZ = 0
        
        if x < mid[0]:
            goX = 1
            if checkX(x+1,z):
                x += 1
                placeblock(x,z)
        elif x > mid[0]:
            goX = -1
            if checkX(x-1,z):
                x -= 1
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
                        placeblock(x,y)

                x +=1 
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
                        placeblock(x,y)

                z +=1 
                placeblock(x,z)

        

        

    return
            
    



            
      
        


doors = []


    
for houses in houseLoc:
    doorloc = houses.getDoorLocation()
    doors.append(doorloc)

pPos = midPoint(doors)
print(pPos)

mc.setBlocks(pPos[0],pPos[1]-5,pPos[2],pPos[0],pPos[1],pPos[2],57)


while checkX(pPos[0],pPos[2]) == False:
    print('!! in middle !!!')
    pPos[0] += 1 
    


for door in doors:
    roadConnect(door[0]-2,door[1],door[2],pPos)



