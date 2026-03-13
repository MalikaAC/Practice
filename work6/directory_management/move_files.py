#Move/copy files between directories
import shutil
# Move file
shutil.move("folder1/test.txt", "folder1/folder2/test.txt")

# Copy file
shutil.copy("folder1/folder2/test.txt", "folder1/folder3/test.txt")