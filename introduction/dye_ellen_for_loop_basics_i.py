#1. Basic - print all integers form 0 to 150

for i in range(151):
    print(i)

#Multipes of 5 - Print all the multiples of 5 from 5 to 1,000

for i in range (5,1001,5):
    print(i)

#Counting, the Dojo Way - Print integers from 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo"

for i in range (1,101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i%5 == 0:
        print("Coding")
    else:
        print(i)

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum
sum = 0
for i in range(500001):
    if i % 2 != 0:
        sum = i + sum
print (sum)

#Countdown by Fours - print positive numbers tarting at 2018 counting down by 4s
for i in range(2018,0,-4):
    print(i)

#Flexible Counter - set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2 and highNum=9 and mult=3, the loop should only print 3,6,9
highNum = 35
lowNum = 2
mult = 3
for i in range(lowNum, highNum+1):
    if i % mult == 0:
        print(i)








