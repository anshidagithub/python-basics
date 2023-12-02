# COLLECTION DATA TYPES

# LIST
list1= [ "onion","tomato","chilli"]
print(len(list1))
print(list1[1])
list1[0]= "carrot"
print(list1)

for x in list1:
    print(x)

list2=[ 10,20,30,40]
sum= list2[0] + list2[3]
print(sum)

list2.append("50")
print(list2)

list2.insert( 1, "5")
print(list2)

# del list2

list2.remove("5")
print(list2)

list2.clear()
