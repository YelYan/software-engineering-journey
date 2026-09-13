import sys

small_list = [0,1,2,3]
large_list = list(range(100))
# large_list = list(range(1000000))

print("Memory Address of Small List:", id(small_list))
print("Memory Address of Large List:", id(large_list))
print("Memory Size of Small List:", sys.getsizeof(small_list), "bytes")
print("Memory Size of Large List:", sys.getsizeof(large_list), "bytes")