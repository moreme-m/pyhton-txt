#file => a document that contains data, store
#file handling => storing, organizing data, manipulation


#__MODE__
#reading(r) => reading the contents for the file
file = open("mariam.txt","r")
print(file.read())
file.close()


#write(w) =>write new content to file
file = open("mariam.txt", "w")
file.write("I love Javascript")
file.close()

#append(a) => adds more content to file
file = open("mariam.txt", "a")
file.write("I also like HTML and CSS")