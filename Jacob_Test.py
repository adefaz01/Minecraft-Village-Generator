from mcpi.minecraft import Minecraft
from mcpi import block, entity, vec3
import random

mc = Minecraft.create()

# TODO: Add windows and doors on all 4 sides, add recursion for rooms, get rid of risk of windows and doors
#       coliding with the walls for each room, staircase to second floor if its a 2 story house

# Makes lists of different blocks for each type of block needed for house
roof_type = [block.Block(44, 0), block.Block(44, 3), block.Block(44, 5)]
house_type = [block.Block(5, 0), block.Block(5, 1), block.Block(5, 2)]
beam_type = [block.Block(17, 0), block.Block(17, 1)]
foundation_type = [block.Block(4), block.Block(45), block.Block(98)]


def houseTest(x,y,z):

    # Creates a random size for the new house
    l = random.randint(8, 12)
    w = random.randint(8, 12)

    levels = random.randint(1, 2)

    # Chooses blocks from the block list for the new house, as well as how many levels the house will be
    roof_block = random.choice(roof_type)
    house_block = random.choice(house_type)
    beam_block = random.choice(beam_type)
    foundation_block = random.choice(foundation_type)

    # Creates a flat grass surface
    mc.setBlocks(x - 3, y - 1, z - 3, x + 15, y - 1, z + 15, 2)
    mc.setBlocks(x - 3, y, z - 3, x + 15, y + 20, z + 15, 0)

    # Creates outline of house
    mc.setBlocks(x, y - 1, z, x + l, y + 3, z + w, house_block)
    mc.setBlocks(x, y, z, x + l, y, z + w, foundation_block)
    mc.setBlocks(x - 1, y + 4, z - 1, x + l + 1, y + 4, z + w + 1, roof_block)
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

    # Creates random door position and places it
    # door_pos = random.randint(1, w - 2)
    # mc.setBlock(x, y + 1, z + door_pos, 64, 8)
    # mc.setBlock(x, y, z + door_pos, 64, 0)

    ## variable to store location of door 
    #doorLocation = (int(x),int(y),int(z + door_pos))

    # Windows

    #mc.setBlocks(x + 4, y + 1, z - 2, x + 4, y + 2, z - 3, 20)
    #mc.setBlocks(x + 4, y + 1, z + 2, x + 4, y + 2, z + 3, 20)

x, y, z = mc.player.getPos()

houseTest(x, y, z)


