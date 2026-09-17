import os

directory_name = "day6_test_folder"

if not os.path.exists(directory_name):
    os.mkdir(directory_name)
    print("Directory created.")
else:
    print("Directory already exists.")

print("Current working directory:", os.getcwd())
print("Files in this directory:", os.listdir())
print("Environment variables:", os.environ)