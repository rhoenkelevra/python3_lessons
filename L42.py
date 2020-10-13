# Animal is-a object (yes, sort of confusing) looka at the extra credit

class Animal(obj):
    pass
    
## Dog is-a Animal

class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a name
        self.name = name
        
class Cat(Animal):
    def __init__(self, name):
        ## Cat has-a name
        self.name = name
        
## Person is-a Object
class Person (object):
    def __init__(self, name):
        ## Person has-a name
        self.name = name
        
        ## Person has-a pet of some kine
        self.pet = None
        
## Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary)
    ## ? hmm what is this strange magic?
    super(Employee, self).__init__(name)
    
    ## Employee has-a salary
    self.salary = salary
    
## Fish is-a Object
class Fish (object):
    pass
    
## Salmon is-a Fish
class Salmon(Fish):
    pass
## Hallibut is-a Fish
class Halibut(Fish):
    pass
    
## rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = cat("Satan")

## Mary is-a Person
mary = Person("Mary")

## mary has-a pet
mary.pet = satan

## frank is-a Employee
frank = Employee("Frank", 120000)

## frank has-a pet (rover)
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
