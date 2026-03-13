#Append new lines and verify content
with open('text.txt', 'a') as f:
     f.write("\nSuch: Discrete structure, History and Physics")
with open('text.txt', 'r') as f:
     print(f.read())