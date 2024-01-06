
#Decorator
def upper_decor(fun):
    def wrapper():
        result= fun()
        return result.upper()
    return wrapper


@upper_decor
def s():
    return "hello"

 
print(s())