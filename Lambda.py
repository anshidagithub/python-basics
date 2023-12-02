def recursion(n):
    if n <= 1:
        return n
    else:
        return n + recursion(n-1)
a= recursion(10)
print(a) 

# LAMBDA FUNCTION

l= lambda x: x * x
print(l(10))

a= lambda x: x / 5
print(a(30))

b= lambda x:x**2
print(b(6))




list1 = [1, 2, 3, 4, 5, 6, 7, 8]

f = filter(lambda x: x % 2 ==0, list1)
print(list(f))

f = filter(lambda x: x % 2 ==1, list1)
print(list(f))



