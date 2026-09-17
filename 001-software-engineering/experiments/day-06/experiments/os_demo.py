import os

print("Current process ID", os.getpid())
print("Current working directory:", os.getcwd())
print("Files in this directory:", os.listdir())
print("Environment variables:", os.environ)