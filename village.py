# Assignment 1 main file
# Feel free to add additional modules/files as you see fit.

from mcpi.minecraft import Minecraft
from RoadNetwork import placeRoads
from locationGen import genLocations
from houseGen import placeHouses



mc = Minecraft.create()

locations = genLocations()

houseLocations = placeHouses(locations)

placeRoads(houseLocations)


