#file => a document that contains data, store
#file handling => storing, organizing data, manipulation


#__MODE__
#reading(r) => reading the contents for the file
mariam = open("main.txt","r")
#print(file.read(9))
mariam.close()

mariam = open("main.txt","r")
print(mariam.readline())
print(mariam.readline())
print(mariam.readline())
print(mariam.readline())
mariam.close

mariam = open("main.txt","r")
print(mariam.readlines())
mariam.close()

print("I love fish \nI hate beans")

mariam = open("main.txt", "r")
for line in mariam:
    print(line)


