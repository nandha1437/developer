'''
number=int(input("enter a number:"))
if number%2==0:
    print("you entered even number")
else:
    print("you entered odd number")
'''

 
 
''' 
number1=int(input("enter a number:"))
number2=int(input("enter a number:"))
sum=(number1*number2)
print(sum)
'''

'''
a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))
cube=(a*b*c)
print(cube)
'''


'''
ch = input("Enter a character to check vowel or consonant:")

if ch in "aeiouAEIOU":
    print("Given character", ch, "is a vowel.")
else:
    print("Given character", ch, "is a consonant.")
    '''



'''
ch=input(“Enter a character to check vowel or consonant :”)
if ch in "aeiouAEIOU":
    print("Given character", ch, "is vowel")
else:
    print("Given character", ch, "is  consonant")
    '''






    
'''
str=input("Please enter a string as you wish: ");
vowels=0
consonants=0

for i in str:
    if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
       i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
           vowels=vowels+1
    else:
        consonants=consonants+1
       
          
print("The number of vowels:",vowels)
print("The number of consonant:",consonants)
'''




'''
num1=float(input("enter your first number:"))
num2=float(input("enter your second number:"))
num3=float(input("enter your third number:"))
maximum=(max(num1,num2,num3))
print("the largest number is",maximum)
'''

'''
totalsum=0
for i in range(2,51,2):
    totalsum=totalsum+i
print("total is:",totalsum)
'''

'''
mylist = [1, 2, 3]
mylist.append(4)
print(mylist)
'''



'''
mystr="python"
slice=mystr[0:1]
print(slice)
'''



'''
mylist=(1,2,3,4,5)
print(sum(mylist))

mytuple=(10,20,30,40,50)
print(mytuple[3])
'''
'''
number=7
if number<0:
    print("your number is negative")
elif number>0:
    print("your number is positive")
else:
    print("your number is zero")
    '''
'''   
set1={1,2,3,4,5}
set2={3,4,5,6,7}
print(set1.intersection(set2))
'''


'''
score=int(input("enter your score:"))
if score>90:
    print("you got A grade")
elif score>=80:
    print("you got B grade")
elif score>=70:
    print("you got C grade")
elif score>=60:
    print("you got D grade")
else:
    print("you failed")
    '''
    
    
'''    
count=1
while(count<=5):
    print(count)
    count=count+1
    '''
    
    
'''   
for i in range(1,5):
    print("*" *i)
print()
'''
'''
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end="\t")
    print()
'''
    
'''  
lower_limit = 0
upper_limit = 50
new=0
while new<=upper_limit:
    print(new,end="")
    lower_limit=upper_limit
    upper_limit=new
    new=upper_limit+lower_limit
print()
'''





for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        print(num)
'''

for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
        
        
'''
'''
evencount = 0
oddcount = 0

for number in range(10, 20):
    if number % 2 == 0:
        evencount = evencount + 1
    else:
        oddcount = oddcount + 1
        
print("Number of even numbers:", evencount)
print("Number of odd numbers:", oddcount)
'''
'''
lower_limit = 1
upper_limit = 50
new = 0

while new <= upper_limit:
    print(new)
    lower_limit, new = new, lower_limit + new
print()
'''



    



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
















































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
   
