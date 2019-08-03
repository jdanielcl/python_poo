

class Vehicle():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.status = False
        self.__start = False
        self.__stop = False
    
    def turn_on(self):
        self.status = True
    
    def speed_up(self):
        self.start = True

    def brake(self):
        self.stop = False

class EVehicle(Vehicle):

    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.autonomy=100
    
    def charge_energy(self):
        self.chargin = True

class Motorcyle(Vehicle):
    stunt = False

    def make_stunt(self):
        self.stunt = True
    
    def description(self):
        status = 'off'
        if self.status:
            status = 'on'
        stunt = 'no'
        if self.stunt:
            stunt = 'yes'
        print(f'Brand: {self.brand}\nModel: {self.model}\nStatus: {status}\nStunt: {stunt}')

class ElectricBike(EVehicle):
    pass

bike = Motorcyle("Honda","CBR")
bike.description()
bike.make_stunt()
bike.description()

e_bike = ElectricBike('Obson','a5s5q')