#Create a text file and write sample data
with open('text.txt', 'w') as f:
    f.write("Calculus\n")
    f.write("English\n")
    f.write("PP2\n")
    f.write("And other subjects")

#Read and print file contents
with open('text.txt', 'r') as f:
    t = f.read()
    print(t)