#1. File Handling


#open() Function
#Open a file and print the content:
f = open("demofile.txt", "r")
print(f.read())
#open(file, mode)
#"r" - Read - Default value. Opens a file for reading, error if the file does not exist
#"a" - Append - Opens a file for appending, creates the file if it does not exist
#"w" - Write - Opens a file for writing, creates the file if it does not exist
#"x" - Create - Creates the specified file, returns an error if the file exist
#Кроме того, вы можете указать, следует ли обрабатывать файл в двоичном или текстовом режиме.
#"t" - Text - Default value. Text mode
#"b" - Binary - Binary mode (e.g. images)


f = open("demofile.txt")
#same as
f = open("demofile.txt", "rt") #"r" for read, and "t" for text are the default values


#READ. If the file is located in a different location, you will have to specify the file path, like this:
f = open("D:\\myfiles\welcome.txt")
print(f.read())



#WITH автоматически закрывает файл
with open("demofile.txt") as f:
  print(f.read())


#CLOSE. If you are not using the with statement, you must write a close statement in order to close the file:
f = open("demofile.txt")
print(f.readline())
f.close()

#READ(NUMBER OF WORDS). By default the read() method returns the whole text, but you can also specify how many characters you want to return:
with open("demofile.txt") as f:
  print(f.read(5))


#READLINE. You can return one line by using the readline() method:
with open("demofile.txt") as f:
  print(f.readline())


#READLINES.Читает файл и возвращает список строк.
with open("demofile.txt") as f:
    lines = f.readlines()
    print(lines)



#By calling readline() two times, you can read the two first lines:
with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline())


#loop. By looping through the lines of the file, you can read the whole file, line by line:
with open("demofile.txt") as f:
  for x in f:
    print(x)


#APPEND. Write to an Existing File. To write to an existing file, you must add a parameter to the open() function:
#"a" - Append - will append to the end of the file
#"w" - Write - will overwrite any existing content
with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open("demofile.txt") as f:
  print(f.read())


#WRITE.Overwrite Existing Content.
with open("demofile.txt", "w") as f:
  f.write("Woops! I have deleted the content!")
#open and read the file after the overwriting:
with open("demofile.txt") as f:
  print(f.read())


#CREATE. Use one of the following parameters:
#"x" - Create - will create a file, returns an error if the file exists
#"a" - Append - will create a file if the specified file does not exists
#"w" - Write - will create a file if the specified file does not exists
f = open("myfile.txt", "x")
#Result: a new empty file is created.
#Note: If the file already exists, an error will be raised.


#DELETE.To delete a file, you must import the OS module, and run its os.remove() function:
import os
os.remove("demofile.txt")


#OS
#CHECK IF FILE EXISTS.
#To avoid getting an error, you might want to check if the file exists before you try to delete it:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")


#rmdir().DELETE FOLDER. RMDIR
os.rmdir("myfolder")
#Note: You can only remove empty folders.


#getcwd() = get current working directory. Узнать текущую папку
print(os.getcwd())


#listdir(). Список файлов в папке
print(os.listdir())


#mkdir(). Создать папку
os.mkdir("new_folder")


#os.chdir(). change directory, для смены текущей рабочей директории (папки)
os.chdir("путь_к_папке")

#os.makedirs()Создает несколько вложенных папок сразу.
os.makedirs("folder1/folder2/folder3")
#folder1
# └ folder2
#    └ folder3




#SHUTIL. Модуль shutil используют для копирования, перемещения и удаления папок.
#copy. Копирование файла
import shutil

shutil.copy("file.txt", "copy.txt")

#move.
shutil.move("file.txt", "folder/file.txt")

#rmtree.
shutil.rmtree("folder")


#PATHLIB. новый и удобный способ работы с файлами
#Создание пути
from pathlib import Path

p = Path("file.txt")
#Импортируем класс Path, который используется для работы с путями к файлам и папкам.
#Создаётся объект пути, который указывает на файл file.txt.
#Здесь файл не создаётся и не открывается.
#Мы просто создаём путь к файлу.

#EXIST.Проверить существование
from pathlib import Path
p = Path("file.txt")
print(p.exists())


#NAME.Узнать имя файла
print(p.name)

#SUFFIX.Узнать расширение
print(p.suffix)

#MKDIR.Создать папку.
Path("new_folder").mkdir()




#BUILT-IN FUNCTIONS
#1. len(). длина
a = [1, 2, 3, 4]
print(len(a))

#2. sum(). сумма
numbers = [1, 2, 3, 4]
print(sum(numbers))

#3. min(). минимум
numbers = [5, 2, 8, 1]
print(min(numbers))

#4. max()
numbers = [5, 2, 8, 1]
print(max(numbers))


#5. map(). Применяет функцию к каждому элементу.
numbers = [1, 2, 3]
result = map(lambda x: x*2, numbers)
print(list(result))

#6. filter(). Оставляет элементы, которые удовлетворяют условию.
numbers = [1, 2, 3, 4, 5]
result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))


#7. reduce(). Применяет функцию последовательно ко всем элементам.
from functools import reduce
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)