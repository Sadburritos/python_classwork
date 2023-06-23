class Kettle():
    volume = 0
    woter = 0
    def __init__(self,volume, woter):
        
        self.volume = volume
        self.woter = woter

         
    def drain (self, liters):
        
        print ("Now at kettle", self.woter, "L")


my_kettle = Kettle(10, 6)

my_kettle.drain(3)
