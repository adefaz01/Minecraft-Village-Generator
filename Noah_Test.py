from mcpi.minecraft import Minecraft
import random

mc = Minecraft.create()

x, y, z = mc.player.getTilePos()

# build a stone house with a door
#x, y, z = mc.player.getPos()
#mc.setBlocks(x+1, y+0, z+1, x+11, y+5, z+11, 1)
#mc.setBlocks(x+2, y+1, z+2, x+10, y+4, z+10, 0)
#mc.setBlock(x+6, y+1, z+1, x+6, y+2, z+1, 0)
#mc.setBlock(x+6, y+2, z+1, 64, 8)
#mc.setBlock(x+6, y+1, z+1, 64, 0)

#create a door with both halves
#x, y, z = mc.player.getPos()
#mc.setBlock(x, y+1, z-1, 64, 8)
#mc.setBlock(x, y, z-1, 64, 0)

#create a brick staircase
#x, y, z = mc.player.getTilePos()
#height = mc.getHeight(x, z)
#w = 5
#d = 10
#for i in range(d):
#    mc.setBlocks(x, height+i, z+i, x+w, height+i, z+d, 45)

#remove trees
def removeTree(x, y, z):
    d = 10
    w = 10
    h = 10
    
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

#removeTree(x, y, z)

#flatten ground beneath player
def flatGround(x, y, z):
    height = mc.getHeight(x, z)
    block = mc.getBlock(x, height, z)

    #sets blocks in a 10x10 radius to the one directly beneath the player
    mc.setBlocks(x-5, height, z-5, x+5, height, z+5, block)

#flatGround(x, y, z)
    
#place blocks randomly up to the height of the player    
def generateRandom(x, y, z):
    height = mc.getHeight(x, z)
    block = mc.getBlock(x, height, z)
    
    while height != y:
        height += 1
        mc.setBlocks(x-random.randrange(1,9), height, z-random.randrange(3,6), x+random.randrange(2,6), height, z+random.randrange(1,7), block)

#generateRandom(x, y, z)

#build squares that get large further below the player
def build(x, y, z):
    d = 4
    w = 4
    h = 3
    i = 0
    
    while i != h:
        mc.setBlocks(x-d-i, y-i, z-w-i, x+d+i, y-i, z+w+i, 1)
        i += 1

#build(x, y, z)

#build squares sort of randomly that get larger further below the player
def build2(x, y, z):
    d = 4
    w = 4
    h = 3
    i = 0
    
    while i != h:
        mc.setBlocks(x-d-random.randrange(i, i+2), y-i, z-w-random.randrange(0, i+2), x+d+random.randrange(i, i+2), y-i, z+w+random.randrange(0, i+2), 1)
        mc.setBlocks(x-d-random.randrange(0, i+2), y-i, z-w-random.randrange(i, i+2), x+d+random.randrange(0, i+2), y-i, z+w+random.randrange(i, i+2), 1)
        i += 1

#build2(x, y, z)

#build squares row by row to make it more random
def build3(x, y, z):
    d = 4
    w = 4
    h = 3
    i = 0
    j = -d

    while j != d:
        mc.setBlocks(x-d-random.randrange(0,2), y-i, z-w-j, x+d+random.randrange(0,2), y-i, z-w-j, 1)
        j += 1

#build3(x, y, z)

def build4(x, y, z):
    d = 4
    w = 4
    h = 10
    i = 0
    
    while i != h:
        if i != h:
            for j in range(d):
                mc.setBlocks(x-d-random.randrange(i, i+2), y-i, z-j-i, x+d+random.randrange(i, i+2), y-i, z-j-i, 1)
                mc.setBlocks(x-d-random.randrange(i, i+2), y-i, z-j, x+d+random.randrange(i, i+2), y-i, z-j, 1)
                mc.setBlocks(x-d-random.randrange(i, i+2), y-i, z+j+i, x+d+random.randrange(i, i+2), y-i, z+j+i, 1)
                mc.setBlocks(x-d-random.randrange(i, i+2), y-i, z+j, x+d+random.randrange(i, i+2), y-i, z+j, 1)
            for j in range(w):
                mc.setBlocks(x-j-i, y-i, z-w-random.randrange(i, i+2), x-j-i, y-i, z+w+random.randrange(i, i+2), 1)
                mc.setBlocks(x-j, y-i, z-w-random.randrange(i, i+2), x-j, y-i, z+w+random.randrange(i, i+2), 1)
                mc.setBlocks(x+j+i, y-i, z-w-random.randrange(i, i+2), x+j+i, y-i, z+w+random.randrange(i, i+2), 1)
                mc.setBlocks(x+j, y-i, z-w-random.randrange(i, i+2), x+j, y-i, z+w+random.randrange(i, i+2), 1)
            i += 1

#build4(x, y, z)


def area(x, y, z):
    height = mc.getHeight(x, z)
    block = mc.getBlock(x, height, z)
    d = 4
    w = 4
    h = 5
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

#area(x, y, z)

def removeSand(x, y, z):
    d = 10
    w = 10
    h = 1
    
    for i in range(d):
        for j in range(w):
            for k in range(h):
                block = mc.getBlock(x+i, y+k, z+j)
                if block == 12:
                    mc.setBlock(x+i, y+k, z+j, 0)
                
                block = mc.getBlock(x+i, y+k, z-j)
                if block == 12:
                    mc.setBlock(x+i, y+k, z-j, 0)
                
                block = mc.getBlock(x-i, y+k, z+j)
                if block == 12:
                    mc.setBlock(x-i, y+k, z+j, 0)
                
                block = mc.getBlock(x-i, y+k, z-j)
                if block == 12:
                    mc.setBlock(x-i, y+k, z-j, 0)

#removeSand(x, y, z)

#removes blocks in a square area and places blocks in spaces that are empty
def flat(x, y, z):
    d = 6
    w = 6
    h = 10
    blocks = [0, 6, 31, 37, 38, 39, 40]

    mc.setBlocks(x+d, y, z+w, x-d, y+h, z-w, 0)
    for i in range(w):
        for j in range(h):
            if mc.getBlock(x+d+1, y+j, z+i) in blocks:
                mc.setBlock(x+d+1, y+j, z+i, 57)
            if mc.getBlock(x+d+1, y+j, z-i) in blocks:
                mc.setBlock(x+d+1, y+j, z-i, 57)

#flat(x, y, z)

#removes blocks in a square area and places blocks in spaces that are empty and do not have a block under it
def flat2(x, y, z):
    d = 6
    w = 6
    h = 10
    blocks = [0, 6, 31, 37, 38, 39, 40]

    mc.setBlocks(x+d, y, z+w, x-d, y+h, z-w, 0)
    for i in range(d):
        for j in range(w):
            if mc.getBlock(x+i, y-1, z+j) in blocks and mc.getBlock(x+i, y-2, z+j) not in blocks:
                mc.setBlock(x+i, y-1, z+j, 57)
            if mc.getBlock(x+i, y-1, z-j) in blocks and mc.getBlock(x+i, y-2, z-j) not in blocks:
                mc.setBlock(x+i, y-1, z-j, 57)
            if mc.getBlock(x-i, y-1, z+j) in blocks and mc.getBlock(x-i, y-2, z+j) not in blocks:
                mc.setBlock(x-i, y-1, z+j, 57)
            if mc.getBlock(x-i, y-1, z-j) in blocks and mc.getBlock(x-i, y-2, z-j) not in blocks:
                mc.setBlock(x-i, y-1, z-j, 57)

#flat2(x, y, z)

#same as flat 1 for all sides but very slow
def flat3(x, y, z):
    d = 6
    w = 6
    h = 10
    blocks = [0, 6, 31, 37, 38, 39, 40]
    
    mc.setBlocks(x+d, y, z+w, x-d, y+h, z-w, 0)
    for i in range(d):
        for j in range(h):
            for k in range(w):
                if mc.getBlock(x+d+1, y+j, z+k) not in blocks:
                    mc.setBlocks(x+d+1, y, z+k, x+d+1, y+j-1, z+k, 57)
                if mc.getBlock(x+d+1, y+j, z-k) not in blocks:
                    mc.setBlocks(x+d+1, y, z-k, x+d+1, y+j-1, z-k, 57)
                
                if mc.getBlock(x-d-1, y+j, z+k) not in blocks:
                    mc.setBlocks(x-d-1, y, z+k, x-d-1, y+j-1, z+k, 57)
                if mc.getBlock(x-d-1, y+j, z-k) not in blocks:
                    mc.setBlocks(x-d-1, y, z-k, x-d-1, y+j-1, z-k, 57)

                if mc.getBlock(x+i, y+j, z+w+1) not in blocks:
                    mc.setBlocks(x+i, y, z+w+1, x+i, y+j-1, z+w+1, 57)
                if mc.getBlock(x-i, y+j, z+w+1) not in blocks:
                    mc.setBlocks(x-i, y, z+w+1, x-i, y+j-1, z+w+1, 57)

                if mc.getBlock(x+i, y+j, z-w-1) not in blocks:
                    mc.setBlocks(x+i, y, z-w-1, x+i, y+j-1, z-w-1, 57)
                if mc.getBlock(x-i, y+j, z-w-1) not in blocks:
                    mc.setBlocks(x-i, y, z-w-1, x-i, y+j-1, z-w-1, 57)

#flat3(x, y, z)

def flat4(x, y, z):
    d = 6
    w = 6
    h = 10
    blocks = [0, 6, 31, 37, 38, 39, 40]

    mc.setBlocks(x+d, y, z+w, x-d, y+h, z-w, 0)
    for i in range(d):
        for j in range(h):
            for k in range(w):
                mc.setBlocks(x+d+1, y, z+k, x+d+1, mc.getHeight(x+d+1, z+k)-1, z+k, 57)
                mc.setBlocks(x+d+1, y, z-k, x+d+1, mc.getHeight(x+d+1, z-k)-1, z-k, 57)
                mc.setBlocks(x-d-1, y, z+k, x-d-1, mc.getHeight(x-d-1, z+k)-1, z+k, 57)
                mc.setBlocks(x-d-1, y, z-k, x-d-1, mc.getHeight(x-d-1, z-k)-1, z-k, 57)

#flat4(x, y, z)

def path(x, y, z):
    blocks = [0, 6, 31, 37, 38, 39, 40]

    temp = mc.getHeight(x, z)

    if mc.getBlock(x, temp-1, z):
        return
