# itorator

#__itor__(), __next__()
 
fruits= ("apple","orange","mango")

ito_ob= iter(fruits)

print(next(ito_ob))
print(next(ito_ob))
print(next(ito_ob))



text = "Hi anshida"
ito_obj = iter(text)
print(next(ito_obj))
print(next(ito_obj))
print(next(ito_obj))
print(next(ito_obj))
print(next(ito_obj))


#operator overloading

class Product:
    def __init__(self,name,price) :
        self.name= name
        self.price= price

    def __add__(self,p2):
        
        final_price= self.price+p2.price
        print( final_price)
    
        



p1= Product("table",8000)  
p2= Product("chair", 2000)     
p1+p2 


    
