print("Loanne")
print('o----')
print(' ||||') #string
print('*' * 10) #expression produces a value 

price = 10
rating = 4.9
name = 'Loanne'
is_published = False
print(price)

full_name = 'John Smith'
age = 20
is_new = True
name = input('What is your name? ')
favorite_color = input('What is your favorite color? ')
print(name + ' likes ' + favorite_color)

birth_year = input('Birth year: ')
print(type(birth_year))
age = 2021 - int(birth_year)
print(type(age))
print(age)

weight = input('Weight(pounds) : ')
convert = float(weight) * 0.453592
print("Weight is " + str(convert)) # convert float to string

course = "Python's Course for Beginners" #apostrophe
course = 'Python Course for "Beginners"' #double quote 
course = ''' 
Hi loanne awitize 
palakas ka pa 
hahhaha
'''
course = 'Python for Beginners'
another = course[:]
print(another)

name = 'Jennifer'
print(name[1:-1])


first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder' #formatted string 
m= f'loanne cutie {last}'
print(m)
print(msg)
print(message)
#John [Smith] is a coder

course = 'Python for Beginners'
print(course.replace('Beginners', 'loanne'))
print('Piethon' in course) # bool

#             .methods
#print(course.find('for'))
#print(len(course))
#print(course.capitalize())
#print(course.upper())
#print(course.lower())
#print(course)

print(10 /3) #float
print(10 // 3) # integer rounds to nearest whole number
print(10 % 3) # modulo
print(10 **3) # exponent


x = 10
x += 3 # augmented assignment operator same as x = x+3
print(x)

x = 10 + 3 *(2**2)
print(x)

x = (2+3) * 10 -3 #47


import math 
print(math.ceil(2.9))
print(math.floor(2.9))

#https://docs.python.org/3/library/math.html
#math modules

x= 2.9
print(round(x))
print(abs(-2.9)) #absolute


#if else statement
is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("it's a lovely day")

print("Enjoy your day")

house = 1000000
good_credit= True
if good_credit:
    print("10 percent downpayment is : " + str(house * 0.1))
else:
    print("20 percent downpayment is: " + str(house * 0.2))

#or

price = 1000000
has_goood_credit = True

if has_goood_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Downpayment: ${down_payment}")



age = input("What is your age? ")
if int(age) >= 20 and int(age) <= 50:
    print("Pwede lumabas")
elif int(age) < 20:
    print("Baby ka pa bawal lumabas")
else:
    print("kahit ano ka pa bawal padin lumabas") 


has_high_income = False
has_good_credit = True
has_criminal_record =True
#if has_high_income or has_good_credit:
    #print("Eligible for loan")
if has_good_credit and not has_criminal_record:
    print("Eligible for loan")


temperature = 35
if temperature > 30:
    print("hot day")
else:
    print("not hot day")


name = input("What is your name? ")
count = len(name)
if count < 3:
    print("Name should be at least 3 characters")
elif count >50:
    print("Too long")
else:
    print("Good")


#or 

#if len(name) < 3:
    #print("Name should be at least 3 characters")
#elif len(name) >50:
    #print("Too long")
#else:
    #print("Good")


weight = input('Weight: ')
qs = input("(L)bs or (K)g: ")
if qs == str('L') or qs == str('l'):
    pounds = float(weight) * 2.20462
    print("You are " + str(pounds) + " pounds")
elif qs == str('K') or qs == str('k'):
    kilograms = float(weight) * 0.453592
    print("You are " + str(kilograms) + " kilograms")
else:
    print(f"Not in the choices")

#or

weight = int(input("Weight? "))
qs = input("(L)bs or (K)g: ")
if qs.upper() == 'L':
    pounds = weight * 2.20462
    print(f"You are {pounds} pounds")
elif qs.upper() == 'K':
    kilograms = weight * 0.453592
    print(f"You are {kilograms} pounds")
else:
    print(f"Not in the choices")



#while loop
i = 1
while i <=5:
    print('*' * i)
    i += 1 #or i = i + 1 
print("Done")



#while loop
i = 1
while i <=5:
    print('*' * i)
    i += 1 #or i = i + 1 
print("Done")


#guessing game
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("wow panalo")
        break
    elif guess_count >= guess_limit:
        print("Finish na talo ka ")
        break
#or
#else:
    #print("Finish na talo ka ")


#car game
command = ""
started = False
while True: #command != "quit"
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started")
        else:
            started = True
            print("Car starts...")
    elif command == "stop":
        if not started:
            print("Car already stopped")
        else:
            started = False
            print("Car stops...")
    elif command == "help":
        print("""
start - start the car
stop - stop the car 
quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Not in the choices")


#for loops
#for item in 'Python':
#for item in ['Nowel' ,'Selina', 'Loanne']:
#for item in range(10):
for item in range(5,10,2): #(5,10) #pass ng 2 
    print(item)


prices = [10,20,30]
total = 0
for price in prices:  #mapupunta value ng prices sa price
    print(price, end=' ') #horizontal
    total +=  price
print(f"\nTotal: {total}") #next line


for y in range(3):
    print(y, end=' ')

#nested loops
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

#challenge
numbers = [5,2,5,2,2]
#for num in numbers:
#    print('x' * num)
for x_count in numbers:
    output = ''
    for count in range(x_count): #x count [0,1,2,3,4]
        output += 'x'
    print(output)


#challenge
numbers = [5,2,5,2,2]
for num in numbers:
    print('x' * num)


#even numbers
for i in range(0, 101, 2): 
	print(i) 


for i in range(0, 5):  #[0, 1, 2, 3, 4] 
    print(i)

for i in range(5):  #Note that if you give only one number, python assumes that n = 0:
    print(i)



#lists

names = ['Janry', 'Lovely','mama','papa']
names[0] = 'johnrey'
print(names)
print(names[0:2])



numbers = [1,2,3,4,5]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)


#2d lists

matrix = [
    [1,2,3], 
    [4,5,6], 
    [7,8,9]  
    
     
]
#matrix[0][1] = 20
#print(matrix)
#print(matrix[0][1])

for row in matrix:
    #print(row)
    for item in row:
        print(item)
 

 
 
#list methods / list functions
numbers = [5,2,1,7,5,4]
numbers2 = numbers.copy()
numbers2.append(10)
print(numbers2)
#numbers.sort()
#numbers.reverse()

#print(numbers.count(5)) #ilang beses naulit
#print(50 in numbers) # True or false kung meron
#print(numbers.index(5))
#numbers.pop() #remove last item
#numbers.clear()
#numbers.remove(2)
#numbers.insert(0, 10)
#numbers.append(20)
print(numbers)



   
numbers = [5,2,1,7,5,4,10,1,1]
uniques = []
for number in numbers:
    if number not in uniques: # in perator is used to check if a value exists in sequence or not.
        uniques.append(number)
print(uniques)

#tuples
#Tuples are used to store multiple items in a single variable. 
# unchangeable immutable

numbers=(1,2,3)
print(numbers[0])


#Unpacking 
coordinates = (1,2,3) #can also be used in lists
"""x=coordinates[0]
y=coordinates[1]
z=coordinates[2]"""
x,y,z = coordinates
print(x)


#dictionaries
customer = {
    "name" : "loanne",
    "age": 20,
    "is verified": True
}
#customer["bday"] = "feb5"
#print(customer["name"])
#print(customer["bday"]) 
print(customer.get("bday","feb 5 "))



phone = (input("Phone:" )) #1234
translate = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output =""
for item in phone: #1234
    output += translate.get(item,"oops!") + " "
print(output)

#emoji converter
message = input(">")
words = message.split(' ')
emojis = {

}
output =""
for word in words: #1234
    output += emojis.get(word,word) + " "
print(output)

#functions 
#container of a specific task
def greet_user():
    print('hi there')
    print('Welcome aboard')


print("Start")
greet_user()
print("Finish")


#parameters 
#placeholder for receiving information
def greet_user(first_name, last_name):
    print(f'hi there {first_name} {last_name}')
    print('Welcome aboard')


print("Start")
greet_user("loanne", "deoduco") #papasa ung value sa parameter
 #loanne is an argument Argument is an actual piece of info
print("Finish")


#keyword arguments
def greet_user(first_name, last_name):
    print(f'hi there {first_name} {last_name}')
    print('Welcome aboard')


print("Start")
#greet_user("loanne", last_name="deoduco") #positional arguments dat mauna yung positional argument bago yung keyword argument
greet_user(last_name="deoduco",first_name="loanne")
#calc_cost(total =50, shipping= 5,discount=0.1)   #readability 
print("Finish")



#return statement
def square(number):
    return number * number #irereturn sa function
    #print(number*number) #9


result = square(3)
#print(square(3))
print(result)



"""
#emoji converter
message = input(">")
words = message.split(' ')
emojis = {

}
output =""
for word in words: #1234
    output += emojis.get(word,word) + " "
print(output)
"""

#creating reusable function 
def emoji_converter(message):
    words = message.split(' ')
    emojis = {

    }
    output =""
    for word in words: #1234
        output += emojis.get(word,word) + " "
    return output


message = input(">")
result = emoji_converter(message)
print(result)


#Exceptions
try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print('Invalid Input')


#classes
#Pascal naming convention  for class
#Summary:
#We use classes to define types and they can also have attributes that we can set anywhere in our programs
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

#objects or instances
point1 = Point()
point1.draw()

point1.x = 10
point1.y = 20
print(point1.x)



point2 = Point()
point2.x = 1
print(point2.x)


# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

# test code
print(car1.description())
print(car2.description())


#CS DOJO classes and objects
class Robot:
    def __init__(self, name, color, weight): #constructor
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)

# r1 = Robot()
# r1.name = "Tom"
# r1.color = "red"
# r1.weight = 30
#
# r2 = Robot()
# r2.name = "Jerry"
# r2.color = "blue"
# r2.weight = 40

r1 = Robot("Tom", "red", 30)
print(r1.name, r1.color, r1.weight)
r2 = Robot("Jerry", "blue", 40)

r1.introduce_self()
r2.introduce_self()

#constructors
#init initialize
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10,20)

print(point.x)


#execise
class Person:
    def __init__(self,name):
        self.name = name
    
    def talk(self):
        print(f"Hi, I am {self.name}")


loanne = Person("Loanne")
#print(person.name)
loanne.talk()

janry = Person("Janry")
janry.talk()



#inheritance
#dry - don't repeat yourself
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")
    #pass #pass means nothing so we don't have empty class


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")
   # pass

dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.be_annoying()


#modules
#file with some python code like section in supermarket


numbers = [10,3,6,2]
maximum = numbers[0]
def find_max(numbers):
    for number in numbers:
        if number > maximum:
            maximum = number
        return maximum
print(maximum)


#packages
#men   women   kids

#modules
#shoes
#shirt
#pants


#generating Random
import random

for i in range(3):
    #print(random.random())
    print(random.randint(10,20))

#picking members
import random
members = ['loanne','irish','redel','bill', 'otnek']
leader=random.choice(members)
print(leader)

#roll a die
import random
die =[1,2,3,4,5,6]
first = random.choice(die)
second = random.choice(die)
print(f'({first}, {second})')


for i in range(4):
    i= i+1
    print(i)

"""-----------------------------------------
pathlib"""



from pathlib import Path

#absolute path
#c:\Program File\Microsoft
#relative path #ecommerce package


path = Path()
for file in path.glob('*.py'):
    print(file) #get all the files in the directories ,.py directories
#path = Path("email")
#print(path.exists())

#(path.mkdir)make directory , (rmdir) remove directory

"""Pypi - Python Package index
https://pypi.org/
"""