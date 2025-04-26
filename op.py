#file => a document that contains data, store
#file handling => storing, organizing data, manipulating,
# __MODE__
#reading (r) => reading the contents of a file
#write (w) => replaces everything in the doc

#append(a) => adds more
#create(X) => creates a new file

#file = open("example.py", "r")
#file = open("gcd.txt", "a")




# file = open("test.txt", "x")

with open("abc.txt", "a") as f:
    f.write("\nI like swimming")

with open("abc.txt", "r") as f:
    f.read()

with open("abc.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        word = line.split()
        print(word)

import os
os.remove("test.txt")        