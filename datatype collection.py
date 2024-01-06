# COLLECTION DATA TYPES
#tuple

tuple1= ('rose','jasmin','jamandhi') 
print(tuple1)

print(tuple1[2])

for x in tuple1:
    print(x)

    print(len(tuple1))

    # del tuple1
    print(tuple1)

    tuple2= (1,2,3,4)

    tuple3= tuple1 + tuple2
print(tuple3)

#set

set1={"football", "cricket", "hokki"}
print(set1)

for x in set1:
   print(x)

   print("hokki"in set1)
print("shuttle"in set1)

print(len(set1))

set1.add("shuttle")
print(set1)


set1.update(["chess","ludo","carroms"])
print(set1)

set1.remove("football")
print(set1)

set1.discard("jump")
print(set1)

set2 ={ 1,2,3,4}
set3=set1.union(set2)
print(set3)
