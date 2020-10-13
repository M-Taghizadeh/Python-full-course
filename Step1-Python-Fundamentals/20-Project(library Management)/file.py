PATH = 'C:/Users/Zanis/Desktop/content.txt'

import os
# delete file ---> os.remove()

if os.path.exists(PATH):
    print("yes")
else:
    print("no")
# delete folder --> os.rmdir()