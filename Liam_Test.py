from mcpi.minecraft import Minecraft

mc = Minecraft.create()


mc.player.setPos(60, 63, -18)
x, y, z = mc.player.getPos()

#x, y, z = mc.player.getPos()

#mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, 1)

def CreateWindow(x1, y1, z1, x2, y2, z2):
        mc.setBlocks(x1, y1, z1, x2, y2, z2, 20)

def houseTest(x, y, z):
    # current Location : 
    
    # Creates inital block of house
    mc.setBlocks(x + 4, y - 1, z - 4, x + 9, y + 3, z + 4, 1)

    #Hollows out the inside
    mc.setBlocks(x + 5, y, z - 3, x + 8, y + 2, z + 3, 0)

    #Creates door and windows



    mc.setBlock(x + 4, y + 1, z, 64, 8)
    mc.setBlock(x + 4, y, z, 64, 0) 

    #If you want doors placed from the other side, replace 8, 0 with 13, 2
    

    # Windows
    CreateWindow(x + 4, y, z - 2, x + 4, y + 2, z - 3)
    CreateWindow(x + 7, y, z - 4, x + 8, y + 2, z - 4)
    CreateWindow(x + 9, y, z - 4, x + 9, y + 2, z + 1)

    #flat rooftop
    mc.setBlocks(x + 3, y + 4, z - 5, x + 10, y + 4, z + 5, 126)


houseTest(x, y, z)
