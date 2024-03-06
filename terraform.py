from mcpi.minecraft import Minecraft
import random

mc = Minecraft.create()

#x, y, z = mc.player.getTilePos()

#searches for wood and leaf blocks and replaces them with air
#can't remove acacia wood
def removeTree(x, y, z, d, w, h):
    
    for i in range(d):
        for j in range(w):
            for k in range(h):
                block = mc.getBlock(x+i, y+k, z+j)
                if block == 17 or block == 18:
                    mc.setBlock(x+i, y+k, z+j, 0)
                
                block = mc.getBlock(x+i, y+k, z-j)
                if block == 17 or block == 18:
                    mc.setBlock(x+i, y+k, z-j, 0)
                
                block = mc.getBlock(x-i, y+k, z+j)
                if block == 17 or block == 18:
                    mc.setBlock(x-i, y+k, z+j, 0)
                
                block = mc.getBlock(x-i, y+k, z-j)
                if block == 17 or block == 18:
                    mc.setBlock(x-i, y+k, z-j, 0)


#will cover holes on a wall after clearing an area
def coverWall(x, y, z):
    block = mc.getHeight(x, z)

    mc.setBlocks(x, y, z, x, mc.getHeight(x, z)-1, z, block)
    

#will cover holes on the ground after clearing an area
def coverHole(x, y, z):
    blocks = [0, 6, 18, 31, 37, 38, 39, 40]

    #searches for a block to replace the empty space with
    if mc.getBlock(x-1, y, z) not in blocks:
        block = mc.getBlock(x-1, y, z)
        mc.setBlock(x, y, z, block)
    elif mc.getBlock(x+1, y, z) not in blocks:
        block = mc.getBlock(x+1, y, z)
        mc.setBlock(x, y, z, block)
    elif mc.getBlock(x, y, z-1) not in blocks:
        block = mc.getBlock(x, y, z-1)
        mc.setBlock(x, y, z, block)
    elif mc.getBlock(x, y, z+1) not in blocks:
        block = mc.getBlock(x, y, z+1)
        mc.setBlock(x, y, z, block)
    

#first removes blocks in specified area and then starts covering any holes that may have been created by them
def flat(x, y, z, d, w, h):
    #contains items such as space, grass, flowers, leaves
    blocks = [0, 6, 18, 31, 37, 38, 39, 40]

    mc.setBlocks(x+d, y, z+w, x-d, y+h, z-w, 0)

    #covers walls
    for i in range(d+1):
        for k in range(h):
            if mc.getBlock(x+i, y+k, z+w+1) not in blocks:
                coverWall(x+i, y, z+w+1)
            if mc.getBlock(x-i, y+k, z+w+1) not in blocks:
                coverWall(x-i, y, z+w+1)
            if mc.getBlock(x+i, y+k, z-w-1) not in blocks:
                coverWall(x+i, y, z-w-1)
            if mc.getBlock(x-i, y+k, z-w-1) not in blocks:
                coverWall(x-i, y, z-w-1)
    for j in range(w+1):
        for k in range(h):
            if mc.getBlock(x+d+1, y+k, z+j) not in blocks:
                coverWall(x+d+1, y, z+j)
            if mc.getBlock(x+d+1, y+k, z-j) not in blocks:
                coverWall(x+d+1, y, z-j)
            if mc.getBlock(x-d-1, y+k, z+j) not in blocks:
                coverWall(x-d-1, y, z+j)
            if mc.getBlock(x-d-1, y+k, z-j) not in blocks:
                coverWall(x-d-1, y, z-j)

    #covers holes
    for i in range(d+1):
        for j in range(w+1):
            if mc.getBlock(x+i, y-1, z+j) in blocks:
                coverHole(x+i, y-1, z+j)
            if mc.getBlock(x+i, y-1, z-j) in blocks:
                coverHole(x+i, y-1, z-j)
            if mc.getBlock(x-i, y-1, z+j) in blocks:
                coverHole(x-i, y-1, z+j)
            if mc.getBlock(x-i, y-1, z-j) in blocks:
                coverHole(x-i, y-1, z-j)

#creates blocks that expand outwards as height decreases
def area(x, y, z, d, w, h):
    height = mc.getHeight(x, z)
    block = mc.getBlock(x, height, z)
    i = 0
    
    while i != h:
        if i != h:
            for j in range(d):
                mc.setBlocks(x-d-random.randrange(i, i+2), height-i, z-j-i, x+d+random.randrange(i, i+2), height-i, z-j-i, block)
                mc.setBlocks(x-d-random.randrange(i, i+2), height-i, z-j, x+d+random.randrange(i, i+2), height-i, z-j, block)
                mc.setBlocks(x-d-random.randrange(i, i+2), height-i, z+j+i, x+d+random.randrange(i, i+2), height-i, z+j+i, block)
                mc.setBlocks(x-d-random.randrange(i, i+2), height-i, z+j, x+d+random.randrange(i, i+2), height-i, z+j, block)
            for j in range(w):
                mc.setBlocks(x-j-i, height-i, z-w-random.randrange(i, i+2), x-j-i, height-i, z+w+random.randrange(i, i+2), block)
                mc.setBlocks(x-j, height-i, z-w-random.randrange(i, i+2), x-j, height-i, z+w+random.randrange(i, i+2), block)
                mc.setBlocks(x+j+i, height-i, z-w-random.randrange(i, i+2), x+j+i, height-i, z+w+random.randrange(i, i+2), block)
                mc.setBlocks(x+j, height-i, z-w-random.randrange(i, i+2), x+j, height-i, z+w+random.randrange(i, i+2), block)
            i += 1


    