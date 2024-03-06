from mcpi.minecraft import Minecraft
from mcpi import block
import random
import locationGen
from House import house
import RoomSplit

mc = Minecraft.create()

x, y, z = mc.player.getPos()


roof_type = [block.Block(44, 0), block.Block(44, 3), block.Block(44, 5)]
house_type = [block.Block(5, 0), block.Block(5, 1), block.Block(5, 2)]
beam_type = [block.Block(17, 0), block.Block(17, 1)]
foundation_type = [block.Block(4), block.Block(98)]

## Code ideas and helpful functions for village.py


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random




##function takes in a list of two x,y,z co-ordinates and returns a list of one x,y,z co-ordinate of the middle point
def middle(x):
    return [(x[0] + x[3])/2,x[1],(x[2] + x[5]) / 2]




#places wall horizontally in the middle of the house
##takes the middle point and width of the house as arguments 

def place_Horizontal(mid,w):
    
       
        mc.setBlocks(mid[0],mid[1],mid[2] - (w/2) + 1 ,mid[0],mid[1] + 4, mid[2] + (w/2) - 1,house_block)

        ##generates Random location for the hallway in the wall
        hallway_pos = random.randint(1, (int(w) - 2) - 1)

        ## check to make sure hallway doesn't spawn in the middle of the wall
        if hallway_pos == ((int(w) - 2) - 1 // 2) + 1 or hallway_pos == ((int(w) - 2) - 1 // 2) :
            hallway_pos += 1


        mc.setBlock(mid[0], mid[1] + 2, (mid[2] - (w/2) + 1)  + hallway_pos, 0)
        mc.setBlock(mid[0], mid[1] + 1, (mid[2] - (w/2) + 1) + hallway_pos, 0)


## places wall vertically in the middle of the house 
def place_vertical(mid,l):

    
    mc.setBlocks(mid[0] - (l/2) + 1,mid[1],mid[2],mid[0] + (l/2) - 1,mid[1] + 4, mid[2],house_block)



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
        
        ## update length of house after split
        l = l/2

        ## make sure resulatant room isnt too small 
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
# def houseTest(x,y,z):



    
#     # Creates a random size for the new house
#     l = random.randint(8, 12)
#     w = random.randint(8, 12)

#     levels = random.randint(1, 2)

#     # Creates a flat grass surface
#     mc.setBlocks(x - 3, y - 1, z - 3, x + 15, y - 1, z + 15, 2)
#     mc.setBlocks(x - 3, y, z - 3, x + 15, y + 20, z + 15, 0)

#     # Creates outline of house
#     mc.setBlocks(x, y - 1, z, x + l, y + 3, z + w, house_block)
#     mc.setBlocks(x, y, z, x + l, y, z + w, foundation_block)
#     mc.setBlocks(x - 1, y + 4, z - 1, x + l + 1, y + 4, z + w + 1, roof_block)

#     #Hollows out the inside
#     mc.setBlocks(x + 1, y, z + 1, x + (l - 1), y + 2, z + (w - 1), 0)

#     # Builds house foundation
#     mc.setBlocks(x - 1, y - 1, z - 1, x - 1, y + 3, z - 1, beam_block)
#     mc.setBlocks(x - 1, y - 1, z + w + 1, x - 1, y + 3, z + w + 1, beam_block)
#     mc.setBlocks(x + l + 1, y - 1, z - 1, x + l + 1, y + 3, z - 1, beam_block)
#     mc.setBlocks(x + l + 1, y - 1, z + w + 1, x + l + 1, y + 3, z + w + 1, beam_block)

#     if levels == 2:
#         mc.setBlocks(x, y + 3, z, x + l, y + 7, z + w, house_block)
#         mc.setBlocks(x, y + 4, z, x + l, y + 4, z + w, foundation_block)
#         mc.setBlocks(x - 1, y + 8, z - 1, x + l + 1, y + 8, z + w + 1, roof_block)


#     wall = random.randint(1,2)
#     house_Cordinates = [x, y - 1, z, x + l, y + 3, z + w]
#     mid = RoomSplit.middle(house_Cordinates)
#     RoomSplit.place_walls('right',mid,l,w,wall)
#     RoomSplit.place_walls('left',mid,l,w,wall)

#     # Creates random door position and places it
#     door_pos = random.randint(1, l - 2)
#     not_door_pos = [l-2//2,w-2//2,(l-2//2)//2,(w-2//2)//2,l-2//2 + 1,w-2//2 + 1,((l-2//2)//2) + 1,((w-2//2)//2) + 1]

#     while door_pos in not_door_pos:
#         door_pos = random.randint(1, l - 2)

#     mc.setBlock(x, y + 1, z + door_pos, 64, 8)
#     mc.setBlock(x, y, z + door_pos, 64, 0)

#     ## variable to store location of door 
#     doorLocation = (int(x),int(y),int(z + door_pos))

#     # Windows

#     #mc.setBlocks(x + 4, y + 1, z - 2, x + 4, y + 2, z - 3, 20)
#     #mc.setBlocks(x + 4, y + 1, z + 2, x + 4, y + 2, z + 3, 20)

#     return doorLocation

def genHouse(x,y,z,x1,z1):

    roof_type = [block.Block(44, 0), block.Block(44, 3), block.Block(44, 5)]
    house_type = [block.Block(5, 0), block.Block(5, 1), block.Block(5, 2)]
    beam_type = [block.Block(17, 0), block.Block(17, 1)]
    foundation_type = [block.Block(4), block.Block(98)]
    
    l = x1
    w = z1

    levels = random.randint(1, 2)

    # Chooses blocks from the block list for the new house, as well as how many levels the house will be
    roof_block = random.choice(roof_type)
    global house_block
    house_block  = random.choice(house_type)
    beam_block = random.choice(beam_type)
    foundation_block = random.choice(foundation_type)

    # Creates a flat grass surface
    mc.setBlocks(x - 2, y - 15, z - 2, x + (l+2), y - 1, z + (w+2), 2)
   ## mc.setBlocks(x - 3, y, z - 3, x + 15, y + 20, z + 15, 0)

    # Creates outline of house
    mc.setBlocks(x, y - 1, z, x + l, y + 3, z + w, house_block)
    mc.setBlocks(x, y, z, x + l, y, z + w, foundation_block)
    mc.setBlocks(x - 1, y + 4, z - 1, x + l + 1, y + 4, z + w + 1, roof_block)

    #Hollows out the inside
    mc.setBlocks(x + 1, y, z + 1, x + (l - 1), y + 2, z + (w - 1), 0)

    # Builds house foundation
    mc.setBlocks(x - 1, y - 1, z - 1, x - 1, y + 3, z - 1, beam_block)
    mc.setBlocks(x - 1, y - 1, z + w + 1, x - 1, y + 3, z + w + 1, beam_block)
    mc.setBlocks(x + l + 1, y - 1, z - 1, x + l + 1, y + 3, z - 1, beam_block)
    mc.setBlocks(x + l + 1, y - 1, z + w + 1, x + l + 1, y + 3, z + w + 1, beam_block)

    if levels == 2:
        mc.setBlocks(x, y + 3, z, x + l, y + 7, z + w, house_block)
        mc.setBlocks(x, y + 4, z, x + l, y + 4, z + w, foundation_block)
        mc.setBlocks(x - 1, y + 8, z - 1, x + l + 1, y + 8, z + w + 1, roof_block)
        mc.setBlocks(x + 1, y + 4, z + 1, x + (l - 1), y + 6, z + (w - 1), 0)

        mc.setBlocks(x - 1, y + 4, z - 1, x - 1, y + 7, z - 1, beam_block)
        mc.setBlocks(x - 1, y + 4, z + w + 1, x - 1, y + 7, z + w + 1, beam_block)
        mc.setBlocks(x + l + 1, y + 4, z - 1, x + l + 1, y + 7, z - 1, beam_block)
        mc.setBlocks(x + l + 1, y + 4, z + w + 1, x + l + 1, y + 7, z + w + 1, beam_block)

        mc.setBlocks(x + l - 2, y + 5, z, x + l - 3, y + 6, z, 20)
        mc.setBlocks(x + 2, y + 5, z, x + 3, y + 6, z, 20)
        mc.setBlocks(x + l - 2, y + 5, z + w, x + l - 3, y + 6, z + w, 20)
        mc.setBlocks(x + 2, y + 5, z + w, x + 3, y + 6, z + w, 20)

        mc.setBlocks(x, y + 5, z + 2, x, y + 6, z + 3, 20)
        mc.setBlocks(x, y + 5, z + w - 2, x, y + 6, z + w - 3, 20)
    
    wall = random.randint(1,2)
    house_Cordinates = [x, y-1, z, x + l, y, z + w]
    mid = middle(house_Cordinates)
    place_walls('right',mid,l,w,wall)
    place_walls('left',mid,l,w,wall)

    # Creates random door position and places it
    door_pos = random.randint(2, l - 2)
    not_door_pos = [l-2//2,w-2//2,(l-2//2)//2,(w-2//2)//2,l-2//2 + 1,w-2//2 + 1,((l-2//2)//2) + 1,((w-2//2)//2) + 1]
    
    while door_pos in not_door_pos:
        door_pos = random.randint(1, w - 2)

    mc.setBlock(x, y + 1, z + door_pos, 64, 8)
    mc.setBlock(x, y, z + door_pos, 64, 0)

    mc.setBlocks(x + l - 2, y + 1, z, x + l - 3, y + 2, z, 20)
    mc.setBlocks(x + 2, y + 1, z, x + 3, y + 2, z, 20)
    mc.setBlocks(x + l - 2, y + 1, z + w, x + l - 3, y + 2, z + w, 20)
    mc.setBlocks(x + 2, y + 1, z + w, x + 3, y + 2, z + w, 20)
    mc.setBlocks(x, y + 1, z + w - door_pos, x, y + 1, z + w - door_pos, 20)
    
    ## variable to store location of door 
    doorLocation = (int(x),int(y),int(z + door_pos))


    return doorLocation


def placeHouses(locations):
    
    houseLocations = []

    # loops through plots and places houses on each

    for plot in locations:
        
        print(f'{plot.x},{plot.z},{plot.dx},{plot.dz}')

        
        mc.setBlocks(plot.x - 2, plot.height, plot.z - 2,\
            (plot.x + plot.dx) + 2, plot.height + 30, (plot.z + plot.dz) + 2, 0)



        House = house(plot.x,plot.height,plot.z,plot.dx,plot.dz)
        House.build()
        houseLocations.append(House)

    return houseLocations