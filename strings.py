# a = "Hello, World!"
# print(len(a))

# slicing
b = "Hello, World!"
print(b[2:5])

# remove whitespace
a = " Hello, World! "
print(a.strip())

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))
