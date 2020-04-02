import os

PATH = "C:\\Test"

# Using os.walk
for root, dirs, files in os.walk(PATH, topdown=False):
    for name in files:
        print(os.path.join(root, name))


# Custom Function
def print_directory_content(path):
    for _file in os.listdir(path):
        child_directory = os.path.join(path, _file)
        if os.path.isdir(child_directory):
            print_directory_content(child_directory)
        else:
            print(child_directory)


print_directory_content(PATH)
