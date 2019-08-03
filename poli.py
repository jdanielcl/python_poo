class Car():

    def movement(self):
        print('Moving using four wheels')
        

class MotorBike():
    
    def movement(self):
        print('Moving using two wheels')

class Truck():

    def movement(self):
        print('Moving using six wheels')


def vehicleMovement(vehicle):
    vehicle.movement()

miVehicle = Truck()
vehicleMovement(miVehicle)
miVehicle = MotorBike()
vehicleMovement(miVehicle)
miVehicle = Car()
vehicleMovement(miVehicle)