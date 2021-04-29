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



#from 1 to 100 determine each number if its divisble by 3 or 5 also 
#if it is divisible by 3 and 5 
for x in range(1,101):
    
    if (x%3 == 0 and x%5 == 0):
        print(f'3 & 5: {x}')
    elif (x%5 == 0):
        print(f'5: {x}')
    elif (x%3 == 0):
        print(f'3: {x}')


#input number tas result ng index nila 
for i in range(int(input())):
    print(i, end=' ')


#input 3 number tas itottotal
total = 0
for i in range(3):
    number = int(input())
    total += number
print(f'total: {total}')




#*
#**
#***
#****
#*****

#Simple half pyramid pattern
rows = 5
for i in range(0, rows):
    for j in range(0, i+1):
        print('*', end= ' ')
    print('\r')
       
#*****
#****
#***
#**
#*
#        
#Downward half-Pyramid Pattern of Star
rows = 5
for i in range(rows + 1, 0,-1):
    
    for j in range(0 , i-1):
        print('*',end=' ')
    print('\r')    

#*
#**
#***
#****
#*****
    
#Simple half pyramid pattern(mine)
i=6
for y in range(1,i):
    
    if y <= 5:
        print('*' * y)
        y = y+1


#*
#**
#***
#****
#*****
#Simplest half pyramid pattern(mine)
for i in range(6):
    print('*' * i)

#*****
#****
#***
#**
#*
#Downward half-Pyramid Pattern of Star(mine)
for i in range(5,0,-1):
    print('*' * i)


#*
#**
#***
#****
#*****
#****
#***
#**
#*
#downward and upward pyramid(mine)  
for i in range(6):
    print('*' * i)
for i in range(4,0,-1):
    print('*' * i)



#1  
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5

rows = 6
# if you want user to enter a number, uncomment the below line
# rows = int(input('Enter the number of rows'))
# outer loop
for i in range(rows): #012345
        # nested loop
    for j in range(i):#012345
        # display number
        print(i, end=' ')
    # new line after each row
    print('')


#1  
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5

rows = 6 
for i in range(1, rows): # 1 2 3 4 5 
    for j in range(1, i+1): #1,2+1      1,2,3      
        print(i, end=" ")
    print(' ')

#1  
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5

rows = 6 
for i in range(1, rows): #1, 2, 3, 4, 5
    for j in range(1, i+1):  #(1,2+1)   1 ,2 ,3 
        print(j, end=" ")
    print(' ')

#input number and its highest number
lst = []
for i in range(5):
    number = int(input('Number: '))
    lst.append(number) #.append para kunin nya yung number tas isama sa list

print("largest number: ", max(lst))



#4. Write a Python program which accepts the radius of a circle from the user and compute the area.
import math
radius = float(input("Radius: "))
area = math.pi * (radius)**2
print(area)
    
 

#5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
first_name = input("First name: ")
last_name = input("Last name: ")
first = last_name
last = first_name
print(f"Name:{first} {last}")

#6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. 
values = input("Input some comma seprated numbers : ")
list = values.split(",") #.split is to split a string into a list where each word is a list item
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)

#write 5 numbers and generate to list
lst = []
for i in range(5):
    number = int(input("Number: "))
    lst.append(number)
print(lst)

#write 5 numbers and generate to tuple
lst = []
for i in range(5):
    number = int(input("Number: "))
    lst.append(number)
tuple = tuple(lst)
print(tuple)


#input and return name using function
def name(first, last):
    return first +" "+ last


nem = name(first = input(), last=input())
print(f'Your name is {nem}')