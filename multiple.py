

class Person():
    def __init__(self, name, age, residence):
        self.name = name
        self.age = age
        self.residence = residence

    def description(self):
        print(f'Name: {self.name}, Age: {self.age}, residence: {self.residence}')


class Employment(Person):

    def __init__(self, salary, years, name, age, residence):
        super().__init__(name, age, residence)
        self.salary = salary
        self.years = years

    def description(self):
        super().description()
        print(f'Salary: {self.salary}, years: {self.years}')

daniel = Employment(1500,15,'Daniel',26,'Bogotá')
daniel.description()

print(isinstance(daniel, Employment))
print(isinstance(daniel, Person))