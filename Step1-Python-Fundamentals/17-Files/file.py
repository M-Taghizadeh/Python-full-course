### File Handling:    
    # "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    # "a" - Append - Opens a file for appending, creates the file if it does not exist
    # "w" - Write  - Opens a file for writing, creates the file if it does not exist
    # "x" - Create - Creates the specified file, returns an error if the file exists
    # "b" - Binary - Binary mode (e.g. images)

# [READ]
f = open('C:/Users/Zanis/Desktop/Python Docs/Step1-Python/17-files/Files/content.txt', 'r') 

### read():
TEXT = f.read()
print(TEXT)

### readlines():
line_list = f.readlines()
print(line_list[2:10])

### readline():
print(f.readline())
print(f.readline())
print(f.readline())

for text in TEXT:
    if(text == '\n'):
        print('endline')
    print(text)


# [WRITE] 
f = open("C:/Users/Zanis/Desktop/Python Docs/Step1-Python/17-files/Files/test.txt", "w")
str_line = 'python'
f.write(str_line)
f.close()

# [APPEND]
f = open("C:/Users/Zanis/Desktop/Python Docs/Step1-Python/17-files/Files/test.txt", "a")
str_line = 'python'
f.write(str_line)
f.close()

# [DELETE]
# delete file --> os.remove()
import os
if os.path.exists("test.txt"):
    os.remove("test.txt")
else:
    print("The file does not exist")

# delete folder --> os.rmdir()
import os
os.rmdir("test")