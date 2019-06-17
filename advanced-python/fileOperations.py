file = open("samplefile.txt", "r")
#print(file.read())  #once read u cannot read again
contents = file.read()
print(contents)

#copying contents of file
writeFile = open("writeFile.txt", "w")
writeFile.write(contents)
