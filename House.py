import houseGen

class house:
    def __init__(self,x,y,z, length, width):
        self.x = x
        self.y = y
        self.z = z
        self.doorLocation = None
        self.length = length
        self.width = width

    def build(self):
        self.doorLocation = houseGen.genHouse(self.x,self.y,self.z,self.length,self.width)
    
    def getDoorLocation(self):
        return self.doorLocation
    
    def getLength(self):
        return self.length
    
    def getWidth(self):
        return self.width



        







        
    



