num1 = 42 #variable declaration, initialize Number
num2 = 2.3 #variable declaration, initialize Number
boolean = True #variable declaration, initialize Boolean
string = 'Hello World' #variable declaration, initialize String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initialize Dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, initialize Tuples
print(type(fruit)) #Type Check, log statement
print(pizza_toppings[1]) #Access value in list, log statment
pizza_toppings.append('Mushrooms') #Add value in list
print(person['name']) #Access value in dictionary, log statement
person['name'] = 'George' #Change value in dictionary
person['eye_color'] = 'blue' #Add value in dictionary
print(fruit[2]) #Access value in tuple, log statement

if num1 > 45: #If statment
    print("It's greater") #log statement
else: # Else statement
    print("It's lower") #log statement

if len(string) < 5: #If statment, length check
    print("It's a short word!") #log statement
elif len(string) > 15: #Else if statment, length check
    print("It's a long word!") #log statement
else: #Else statment
    print("Just right!") #log statement

for x in range(5): #For loop, Stop (stops before 5)
    print(x) #log statement
for x in range(2,5): #For loop, Start, Stop (starts at 2, stops before 5)
    print(x) #log statement
for x in range(2,10,3): #For loop, Start, Stop, Increment (starts at 2, stops before 10, incrememnts by +3)
    print(x) #log statement
x = 0 #Variable declaration, start for while loop
while(x < 5): #While loop, stop (stops before 5, starts at 0)
    print(x) #log statement
    x += 1 #Increment for while loop

pizza_toppings.pop() #Delete Value from list
pizza_toppings.pop(1) #Delete value from index of list

print(person) #log statement
person.pop('eye_color') #delete value from Dictionary
print(person) #log statement

for topping in pizza_toppings: #For loop, start, stop (starts at first index of pizza_toppings and stops at the end)
    if topping == 'Pepperoni': #if statement
        continue #for loop continue
    print('After 1st if statement') #log statement
    if topping == 'Olives': #if statment
        break #for loop break

def print_hello_ten_times(): #function
    for num in range(10): #for loop, stop, increment
        print('Hello') #log statement

print_hello_ten_times()

def print_hello_x_times(x): #function, parameter
    for num in range(x): #for loop, stop, increment
        print('Hello') #log statement

print_hello_x_times(4) #function, argument

def print_hello_x_or_ten_times(x = 10): #function, parameter
    for num in range(x): #for loop, stop, increment
        print('Hello') #log statement

print_hello_x_or_ten_times() #function call 
print_hello_x_or_ten_times(4) #argument


"""
Bonus section #Multi line comment
"""
#Single line comment (all below)
# print(num3) #NameError:name <variable name> is not defined
# num3 = 72
# fruit[0] = 'cranberry' #TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) #KeyError: 'favorite_team'
# print(pizza_toppings[7]) #IndexError: list index out of range
#   print(boolean) #IndentationError: unexpected indent
# fruit.append('raspberry') #AttributeError: 'tuple' object has no attribute 'pop'
# fruit.pop(1) #AttributeError: 'tuple' object has no attribute 'append'


