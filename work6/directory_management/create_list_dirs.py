#Create nested directories
import os
os.makedirs(r"folder1/folder2/folder3", exist_ok=True)

# List files and folders
print(os.listdir(r'folder1'))


# Find files by extension
for file in os.listdir("folder1"):
    if file.endswith(".txt"):
        print(file)