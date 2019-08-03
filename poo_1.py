class Car():

    def __init__(self):
        # Private attributes 'encapsulation'
        self.__l = 250
        self.__w = 120
        self.__tires = 4
        self.__state = False
        self.__gas = True
        self.__oil = True
        self.__closed_doors = True

    def start(self):
        if self.__check():
            self.__state = True

    def stop(self):
        self.__state = False
    
    # private method 'encapsulation'
    def __check(self):
        print('checking status')
        return self.__gas and self.__oil and self.__closed_doors
            
    
    def car_state(self):
        state = 'off'
        if self.__state:
            state = 'on'            
        print(f'The car is ({self.__l}x{self.__w}) with {self.__tires} tires and is {state}')


car = Car()
car.car_state()
car.start()
car.car_state()