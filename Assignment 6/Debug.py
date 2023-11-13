class Dog:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Employee:
    def __init__(self, name, idNumber, department):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        
class Cake:
    def __init__(self, flavor, frosting):
        self.flavor = flavor
        self.frosting = frosting
    #can you fill out the rest of this for me? im dumb
    #the cake needs to have the cake flavor and cake frosting stored

class Cat:
    def __init__(self, name, age, fur_length):
        self.name = name
        self.age = age
        self.fur_length = fur_length
        
        
    def breedGuess(self):
        if self.fur_length == "long":
            return("Domestic Longhair")
        else:
            return("Domestic Shorthair")
            
class Car:
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    #create your own function! what do you want it to do?
    def isNew(self):
        if self.year == 2023:
            return("Is a new car")
        else:
            return("Is an old car")

   #i didn't realize it was for the car so i'll just leave two functions :)
def main():
    def idCheck(newEmployee):
        if newEmployee.idNumber == 42:
            return True
        else:
            return False
    #fill this one out with a dog's name and age.. can be your dog, friend's dog, etc
    dog1 = Dog("Skippy" , 12)
    print(dog1.name, dog1.age)
    
    #and what about a new employee
    newEmployee = Employee("Joe", 42, "Human Resources")
    #how would we print out each of the variables from newEmployee?
    print(newEmployee.name, newEmployee.idNumber, newEmployee.department)
    result = idCheck(newEmployee)
    print("ID check result: ", result)

    #now create and print out a cake you make
    cake1 = Cake("chocolate", "chocolate")
    print(cake1.flavor, cake1.frosting)

    #and now create another cake and print it out
    cake2 = Cake("strawberry", "vanilla")
    print(cake2.flavor, cake2.frosting)
    
    
    #create a cat!
    cat1 = Cat("Tony", 13, "short")
    #create another cat!
    cat2 = Cat("Montana", 7, "long" )
    #What would we put here to print out the result of breedGuess for cat1?
    print(cat1.breedGuess())
    
    #create a car!
    car1 = Car("Mini Cooper Coupe", 2018, "Ice Blue")
    #Now print out the function you made for car :)
    print(car1.isNew())

main()
