class Bikes:
    def __init__(self,name,price,colour) :
        self.name = name
        self.price = price
        self.colour = colour

    def start(self):
        print(self.name + "  just started")

bike1= Bikes("Himalaya",500000,"red") 
bike2= Bikes("Royal enfield",300000,"black") 


bike2.price = 400000
bike1.colour = "orange"
#del bike1.colour
 #   del bike2

print(bike1.name,bike1.price,bike1.colour)
print(bike2.name,bike2.price,bike2.colour)



# bike1.start()
# bike2.start()

        # inheritance
 #parent class       
class Person:
    def __init__(self,name,no) :
        self.name = name
        self.no   = no 

    def address(self): 
        print(self.name,self.no) 

 #child class 

class Doctor(Person):
    pass
class Patient(Person): 
    pass

doct1= Doctor(" sebi", 9087654)
pat1= Patient("ashu",123458)

doct1.address()
pat1.address()

