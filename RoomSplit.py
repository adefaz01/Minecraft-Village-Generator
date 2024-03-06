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