from mcpi import minecraft
from mcpi import block
from mcpi import entity

from locationGen import *

mc = minecraft.Minecraft.create()

quit = False
while not quit:

    # Note: To chat in Minecraft, press 't'
    chatEvents = mc.events.pollChatPosts()
    for chatEvent in chatEvents:

        if chatEvent.message.upper() == "QUIT":
            quit = True

        elif chatEvent.message.upper() == "BUILD":
            # Build a stone monolith in front of the player
            pos = mc.player.getTilePos()
            mc.setBlocks(pos.x + 5, pos.y, pos.z,
                pos.x + 7, pos.y + 10, pos.z + 2,
                block.STONE)

        elif chatEvent.message.upper() == "CHICKEN":
            # Place a chicken front of the player
            pos = mc.player.getTilePos()
            mc.spawnEntity(pos.x + 1, pos.y, pos.z, entity.CHICKEN)

        elif chatEvent.message.upper() == "PLATBUILD":
            # places area platform
            #platBuild()
            mc.postToChat("Placing Platform")

        elif chatEvent.message.upper() == "Clear":
            # Clears plot areas
            mc.setBlocks(Px + 100, Py, Pz + 100, Px, Py, Pz, 0)
            mc.postToChat("Clearing!")
            
        else:
            print("Unrecognised command: " + chatEvent.message)
mc.postToChat("Exiting Python script.")