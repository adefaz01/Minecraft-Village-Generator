from mcpi.minecraft import Minecraft, Block, Entity, Vec3
from mcpi import minecraft, block, entity, vec3
import random


# testing location: -6, 82, 1

mc = Minecraft.create()

Px, Py, Pz = mc.player.getTilePos()

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

    def setHeight(self, height):
        self.height = height



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

# Checks average height of a given plot
def heightCheck(Plot):

    avgHeight = 0
    counter = 0

    # loops through each block in plot and finds average height to place plot
    for i in range(Plot.x, Plot.x + Plot.dx):
        for j in range(Plot.z, Plot.z + Plot.dz):

            avgHeight += mc.getHeight(i, j)
            counter += 1

    return (avgHeight // counter)


def genLocations():

    # generates number of houses in village
    NUM_HOUSES = random.randint(5, 9)
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


    for plot in plots:
        plot.setHeight(heightCheck(plot) + 1)

    return plots

#genLocations()





# # loops through plots and places blocks on location
# for plot in plots:

#     print(f'{plot.x},{plot.z},{plot.dx},{plot.dz}')

    

#     mc.setBlocks(plot.x, plot.height, plot.z,\
#         plot.x + plot.dx, plot.height + 30, plot.z + plot.dz, 0)

#     mc.setBlocks(plot.x, plot.height, plot.z,\
#         plot.x + plot.dx, plot.height, plot.z + plot.dz, 57)

