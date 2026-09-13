import sys

number = 25
text = "Hello, World!"
numbers = [0,1,2,3,4,5]

print("Number:", sys.getsizeof(number), "bytes")
print("Text:", sys.getsizeof(text), "bytes")
print("List:", sys.getsizeof(numbers), "bytes")

# Print memory addresses of the objects
print("Memory Address of Number:", id(number))
print("Memory Address of Text:", id(text))
print("Memory Address of List:", id(numbers))
