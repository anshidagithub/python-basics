# COLLECTION DATA TYPES

# LIST
list1= [ "onion","tomato","chilli"]
print(len(list1))
print(list1[1])
#assigning
list1[0]= "carrot"
print(list1)

#for loop
for x in list1:
    print(x)

list2=[ 10,20,30,40]

#sum
sum= list2[0] + list2[3]
print(sum)

#append
list2.append("50")
print(list2)

#insert
list2.insert( 1, "5")
print(list2)

#remove
list2.remove("5")
print(list2)

#extend()
list2.extend((5,15,25))
print(list2, 'a')

#pop()
list2.pop()
print(list2)
list2.pop(0)
print(list2)

#sort()
list1.sort()
print(list1,'b')

#index() return index no
print(list2.index(5),'c')

#clear
list2.clear()


#list comprehension

l1= ["apple","orange","pinapple","grape","kiwi"]

l2=[x for x in l1 if "p" in x ]
print(l2)

c=[5,10,15,20]
d=[x**2 for x in c  ]
print(d)


#continue keyword, break keyword 

for i in range (10,30):
    if i == 20:
        continue

    if i >26:
        break
    print(i)
