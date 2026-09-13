a = 100
b = 100 

print(a)
print(b)

print("Memory Address of a:", id(a))
print("Memory Address of b:", id(b))

# a → object in memory
# b → object in memory

# id(a) → memory address of the object referenced by a
# id(b) → memory address of the object referenced by b

a = 100
b = 200
print("After reassigning values:")
print("Memory Address of a:", id(a))
print("Memory Address of b:", id(b))