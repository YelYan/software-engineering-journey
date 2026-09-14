import os
import time


print("Application started!")
print("Process ID:", os.getpid())

for i in range(10):
    print("Working...", i)
    time.sleep(2)

print("Process finished")

# The operating system uses process IDs to identify running processes.