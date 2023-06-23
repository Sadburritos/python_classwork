class Kettle():
    volume = 0
    woter = 0
    temperature = 0
    def __init__(self,volume):
        
        self.volume = volume
        

         
    def fill (self, liters):
        if self.woter + liters >= self.volume:
            spare = self.volume - self.woter
            print("Перелив = ", spare)
        else:
            self.woter += liters
        print ("Now at kettle", self.woter, "L")

    def draining (self, pour):
        drain = self.woter - pour
        print(drain)

    def boilig(self, heat = 0):
        heat = 100 - self.temperature
        print("Добавлнено градусов ",heat)

my_kettle = Kettle(10)




my_kettle.boilig()