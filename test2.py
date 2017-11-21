print("Helloworld")

name = input("name?")
age = int(input("Enter age?: "))

print("hello", name, age)

#has to be converted into a string first
print("hello" + name + str(age))

print('hello {0} you are {1} years old'.format(name, age))