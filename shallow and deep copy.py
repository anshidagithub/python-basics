import copy

# Original list
original_list = [[1, 3, 6], 5, 6, 7]
print(original_list,)

# Shallow copy
shallow_copy = copy.copy(original_list)
print(shallow_copy,)  

# Deep copy
deep_copy = copy.deepcopy(original_list)
print(deep_copy,) 

# Modify the nested list in shallow copy
shallow_copy[0][0] = 9
print(shallow_copy,)
print(original_list,)

# Modify the nested list in deep copy
deep_copy[1] = 10


print(deep_copy,)      
print(original_list,)       