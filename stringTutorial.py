str = "RahulShettyAccademy.com"
str1 = "Consultingfirm"
str2 = "RahulShetty"

print(str[1])
print(str[0:5])

print(str+ " " +str1) #concatenation
print(str2 in str) #substring check

var = str.split(".") #split string
print(var)
print(var[0])

#strip whitespace
str3 = "good morning"
print(str3.strip())

#READ AND WRITE FILE
file = open('text.txt')
#Read all the contents of file
#print(file.read())

#read n number of characters by passing parameter
#print(file.read(3))

#read one single line
#print(file.readline())


# print line by line
#line = file.readline()
#while line!="":
#    print(line)
#   line = file.readline()

#values = [a, b, c, d, e
#for line in file.readlines():
#   print(line)


#file.close()

#read the file and store all the line in list
#reverse the list
#write the list back to the file

with open('TEXT.txt', 'r') as reader:
    content = reader.readlines() #content of the text convert into list
    reversed(content)
    with open('TEXT.txt' , 'w') as writer:
        for line  in reversed(content):
            writer.write(line)

