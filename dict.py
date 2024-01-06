
#dictionary
dict1= { 
"name" :"anshi",
"email": "anshi@gmail.com",
"phon": 456789
}
print(dict1)

a= dict1["email"]
print(a)

a= dict1.get("phon")
print(a)

#keys()

y= dict1.keys()
print(y)


#value()

u= dict1.values()
print(u)

#item()

p= dict1.items()
print(p)

#popitems

k= dict1.popitem()
print(k,'q')

print(dict1)



dict1["name"]="sabeel"
print(dict1)

for x in dict1:
    print(x)

for x in dict1:
    print(dict1[x])

    for x,y in dict1.items():
        print(x,y)

dict1["age"] = 38
print(dict1)

dict1.pop("email")
print(dict1)

del dict1["phon"]
print(dict1)



 


# dict comprehension

dic_com={x: x*3 for x in range(5) }
print(dic_com)