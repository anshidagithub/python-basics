# positional argument

def add(name,age):
    print("hello",name, "you are",age)

add("geetha",18)

#end

#key word argument

def add(name,age):
    print("hello",name, "you are",age)

add(age=13 ,name="geetha")

#end

#Default argument

def add(name,age=12):
    print("hello",name, "you are",age)

add(name="geetha") # use default age
add("geetha",20) 
add(age=13 ,name="geetha")

#end

# variable length argument

# one * for array

def add(*name):
    print("hello",name)

add("geetha","aswin","arun","binoy")

# ** two star for key value


def add(** name):
    print("hello",name)

add(name="geetha", age= 29,subject= "python" )

#end
