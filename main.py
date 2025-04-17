with open('codingal1.txt','w') as file:
    file.write("this is a sentece to replace")
file.close()

with open('codingal1.txt','r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
file.close()
