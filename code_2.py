new_file = open('new_file.txt','x')
new_file.close()

import os
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("the file does not exist")

my_file = open ("my_file.txt","w")
my_file.write("something something something")
my_file.close()
