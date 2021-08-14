#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())

# Prediction: will print out the number 5

#2
def number_of_military_branches():
    return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

# Prediction: will print out an error because the first function in the print statement has not been defined

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())

# Prediction: will only print out 5 and will skip the second return statement because it will have exited the function before that point

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

# Prediction: Will only print out 5 and will skip the print statement becuase it will have exited the function before that point

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)

# Prediction: Will print out 5 when function is called on variable declaration. Won't print anything out for final print statement because there is no returned value.
# outcome: printed 5 and then none

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))

# Prediction: 
# first function call add(1+2) will print out 3 and return 3 to the print statement outside of the function
# second function call add(2+3) will print out 5 and return 5 to the print statement outside of the function
# final print statement will become print(5+3) and will print 8 to the console

# outcome: I was wrong. The final print statement returned an error because the function becomes what it returns and it did not return any values

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

# Prediction: Will print out 25. Function turned b & c into strings and put them together

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

# Prediction: Function is called in print statement. Will print 100 and then return 10. Print statement outside of function wil print 10. Skips return statement outside of conditional bc it leaves function before then

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

# Prediction: 
# 1st print: 2 is less than 3 so it will return and print 7
# 2nd print: 5 is greater than 3 so it will return and print 14
# 3rd print: First part will return 7, second will return 14, will print 22 since 7+14 is 22
# Will never return 3 because of else statement

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))

# Prediction: second return statement will never run. Will return (3+5) 8 when called and print 8

#11
b = 500
print(b)
def foobar():
    b ="keyword operator from-rainbow">= 300
    print(b)
print(b)
foobar()
print(b)

# Prediction: Will print 500 2 times becauce 500 is printed 2x before function is called. Function is called and b is set to a boolean that is False. False will be printed After the function call, 500 will be printed again. b outside of the function has not changed

# outcome: I misread the function before. Since the function is comparing a str to an int it will print 500 2x and then display an erron when the function is called

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)

# Prediction: Will print out 500 2x. Then the function is called and it will print out 300 and return 300. Since the function is not set to a variable that is lost. 500 will be printed again in the last print statement since it's value hasn't changed

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)

# Prediction: prints 500 2x. Function is called and b is set equal to function. 300 is printed inside of function and then 300 is returned. Final print statement prints 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()

# Prediction: Will print 1 and then 3 and then 2 since the function bar is called during the function foo it will do that before printing the last line of foo

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)

# Prediction: Will print 1 3 5 10. Foo is set equal to y when called, it prints 1 and then bar is set equal to x and then called, when bar is called it prints 3 and returns 5. x is now equal to 5 and is printed. Foo returns 10, y is now equal to 10 and printed
