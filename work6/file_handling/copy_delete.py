#Copy and back up files using shutil
import shutil
shutil.copy('text.txt', 'text2.txt')

#Delete files safely
import os
if os.path.exists('text2.txt'):
    os.remove('text2.txt')