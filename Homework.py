####### UNIT 1 ############

'''   1.Write a Python program to print "Hello, World!"
print("Hello World!")
'''

'''   2.Write a program to add two numbers.
a = int(input("Enter first Number: "))
b = int(input("Enter second Number: "))
print("Sum of two numbers:",a+b)
'''

'''   3.Write a program to find the area of a rectangle.
l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
print("Area of rectangle:", 2*(l+b))
'''

'''   4.Write a program to swap two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a,b = b,a
print(a,b)
'''

'''   5.Write a program to calculate simple interest.
p = int(input("Enter principal amouunut $: "))
r = int(input("Enter Annual rate: "))
t = int(input("Enter time: "))
si = p*r*t/100
print("Simple intrest:", si, "$")
'''

'''   6.Write a program to convert Celsius to Fahrenheit.
c = int(input("Enter temprature in celcuis: "))
f = c*1.8+32
print("Farenheit:",f,"°F")
'''

'''   7.Write a program to find the square and cube of a number.
num = int(input("Enter a Number: "))
print("Square:",num**2)
print("Cube:",num**3)
'''

'''   8.Write a program to check the data type of a variable.
age = 25
price = 19.99
name = "Python"
is_active = True 
print(type(age))
print(type(price))
print(type(name))
print(type(is_active))
'''

'''   9.Write a program to calculate the average of three numbers.
a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))
c = int(input("Enter Number 3: "))
print("Average:",(a+b+c)/3)
'''

'''   10.Write a program using different arithmetic operators.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum = num1 + num2
sub  = num1 - num2
mult  = num1 * num2
div  = num1 / num2
floor  = num1 // num2
mod  = num1 % num2
exp  = num1 ** num2
print("\n--- Arithmetic Results ---")
print("Addition =", sum)
print("Subtraction = ", sub )
print("Multiplication = ", mult )
print("Division = ", div )
print("Floor Division = ", floor )
print("Modulus/Remainder = ", mod )
print("Exponentiation = ", exp )
'''
    

####### UNIT 2 ########

# what are python variables.? Give an example of diclaring numeric datatype.

''' Explain python basic operators and datatypes.WAP to check number is EVEN or ODD using if else.
try:
    num = int(input("Enter a mumber: "))
    if num%2 == 0:
        print(num,"is EVEN Number.")
    else:
        print(num,"is ODD Number.")
except ValueError:
    print("Invalid input...")
'''

'''   Explain python blocks and conditional statements.WAP to grade student's based on marks using elif statement.
try:
    math = int(input("Enter marks obtained in Maths: "))
    phy = int(input("Enter marks obtained in Maths: "))
    chem = int(input("Enter marks obtained in Maths: "))
    total = math+phy+chem
    per = total/3
    print(f"Total: {total}\nPercentage: {per:.2f}%")
    if per >100:
        print("Invalid Marks..")
    elif per<=100 and per>90:
        print("Grade: A")
    elif per<=90 and per>80:
        print("Grade: B")
    elif per<=80 and per>70:
        print("Grade: C")
    elif per<=100 and per>60:
        print("Grade: D")
    elif per<=100 and per>50:
        print("Grade: E")
    else:
        print("Grade: F")
except ValueError:
    print("invalid input..")
'''

''' WAP to calculate area of circle.
try:
    radius = int(input("Enter radius: "))
    area = 22/7*(radius**2)
    print(f"Area of circle: {area:.2f} sq unit")
except ValueError:
    print("Invalid radius...")
'''

'''   create an empty dictionary...update elements....replace elements
d1 = {}                  
print(d1)
d1.update({
    'name':'Aryan',
    'branch':'CSE',
    'roll_no':20})
print(d1)
d1['name']='faijal'
d1['roll_no']=13
print(d1)
'''

'''   create an empty set...add elements....remove elements
s1 = set()
print(s1)
s1 = set([10,"Aryan",13.4,True])
print(s1)
s1.remove(10)
print(s1)
'''

'''   ODD and EVEN
try:
    num = int(input("Enter a number: "))
    if num%2 != 0:
        print(f"Number {num} is ODD")
    else:
        print(f"Number {num} is EVEN")
except:
    print("Invalid Number")
'''

''' WAP to check Number is positive/Negative/Zero
try:
    num = int(input())
    if num > 0:
        print(f"Number {num} is Positive")
    elif num < 0:
        print(f"Number {num} is Negative")
    else:
        print(f"Number {num} is Zero")
except:
    print("Invalid Number...")
'''

'''   WAP to get the marks of five subjects from the user and calculate the average marks scored...and calculate the grade obtained based on the average marks scored.
m1 = float(input("Enter marks obtained in subject 1: "))
m2 = float(input("Enter marks obtained in subject 2: "))
m3 = float(input("Enter marks obtained in subject 3: "))
m4 = float(input("Enter marks obtained in subject 4: "))
m5 = float(input("Enter marks obtained in subject 5: "))

total = m1 + m2 + m3 + m4 + m5
per = total/5
print(f"Total: {total}\nPercentage: {per:.2f}%")

if per >100:
    print("Invalid Marks..")
elif per<=100 and per>90:
    print("Grade: A")
elif per<=90 and per>80:
    print("Grade: B")
elif per<=80 and per>70:
    print("Grade: C")
elif per<=100 and per>60:
    print("Grade: D")
elif per<=100 and per>50:
    print("Grade: E")
else:
    print("Grade: F")
'''

'''   Design a simple calculator that performs basic mathematical operation...it takes three inputs from user..at first the user is asked to enter two number (operands) and third will be the string (operent)
try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    op = input("Enter (+,-,*,/): ")
    if op == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif op == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif op == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif op == "/":
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Invalid Operator...")
except ValueError:
    print("Invalid input..")
'''

'''   WAP to find Vowels and consonent
char = input("Enter an Alphabet: ")
vowel = ("a","e","i","o","u","A","E","I","O","U")
if char in vowel:
    print(char ,"is Vowel")
else:
    print(char ,"is Consonent")
'''

'''   WAP to print table
num = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{num} x {i} = {num*i}")

num = int(input("Enter a number: "))
i = 1
while i<=10:
    print(num,"x",i,"=",num*i)
    i=i+1
'''

'''    find sum of N natural numbers
n = int(input("Enter the number: "))
i = 1
sum = 0
while i<=n:
    sum+=i
    i=+1
print(f"Sum of {n} Natural numbers: {sum}")
'''

'''   WAP to count the number of digits in a given number.
num = int(input("Enter a number: "))
i = 0
while num != 0:
    num//=10
    i+=1
print(i,"Digits")

num = input("Enter a number: ")
print(f"Digits of {num}: {len(num)}")
'''

'''   WAP to find the sum of digits of a given number.
num = int(input("Enter a number: "))
sum = 0
while num!=0:
    digit = num%10
    sum+=digit
    num//=10
print("Sum of digits: ",sum)
'''

'''   WAP to print reverse and check whether a number is a palindrome using a while loop.
num = int(input("Enter a number: "))
n = num
rev = 0
while n!=0:
    digit = n%10
    rev=rev*10+digit
    n//=10
print("Reverse: ",rev)
if rev == num:
    print(num,"is a Palindrome number")
else:
    print(num,"is not a Palindrome number")
'''

'''   WAP to check whether a number is an Armstrong number using a while loop.
num = int(input("Enter a number: "))
n = num
sum = 0
while n!=0:
    digit = n%10
    sum += digit**3
    n//=10
    print(sum)
if sum == num:
    print(num,"is a Armstrong number")
else:
    print(num,"is not a Armstrong number")
'''

'''  list comprehension
l1 = [1,2,3,4,5,6]
l2 = [x+1 for x in l1]
print(l2)
l3 = [x+2 for x in l1 if x%2==0]
print(l3)

cubes = [x**3 for x in range(20) if x%2==0]
print(cubes)
'''

'''  WAF 'makepairs' that takes as input two list of equal length and return a single list of same length where k^th element is the pair of k element from the input list
def makepairs(l1,l2):
    if len(l1)==len(l2):
        return [(l1[k],l2[k]) for k in range(len(l1))]
    else:
        print("Length is not same.")
l1 = [1,3,5,7]
l2 = [2,4,6]
print("Pairs are ->",makepairs(l1,l2))
'''

''' list L = [1,2,3,4,,5,6,7,8,9] 
    1. return a list of numbers starting from the second last element of numbers.
    2. return a list that start from third element to the second last element.
    3. return a list that has only even position element of list L.
    4. return a list that start from the middle of the list L.
    5. return a list that reverse all the elements starting from element at index '0' to middle only and return the entire list.
    6. divide each element of the list by 2 and replace it with the remainder.

L = [1,2,3,4,5,6,7,8,9]
print(L[len(L)-2::-1])
print(L[2:len(L)-2])
print(L[::2])
print(L[len(L)//2:])
print(L[len(L)//2::-1])
print([x%2 for x in L])
'''

# print("~".join(['M','O','N','E','Y']))

'''  WAP to replace character in string.
s,old_char,new_char = input("Enter string: "),input("Enter old character: "),input("Enter new character: ")
list1 = [new_char if char == old_char else char for char in s]  
print("".join(list1))

text,a,b = input("Enter string: "),input("Enter old character: "),input("Enter new character: ")
print(text.replace(a,b))
'''