print("--Program 1 palindrome of a number--")
char=input("enter a number : ")
char2=char[-1::-1]
if (char2==char) :
    print("the given number is a palindrome")
else :
    print("the number is not a palindrome")


print("\n\n\n\n--program 2 function for basic maths--")
def add(a,b):
    print("the result of addition is : ",a+b)
def sub(a,b):
    print("the result of subtraction is : ",a-b)
def mul(a,b):
    print("the result of multiplication is : ",a*b)
def div(a,b):
    if(b==0):
        print("division by zero not allowed")
    else:
        print("the result of division is : ",a/b)

print("1. for addition")
print("2. for subtraction")
print("3. for multiplication")
print("4. for division")
a=int(input("enter your choice : "))
b=float(input("enter number 1-"))
c=float(input("enter number 2-"))
if a==1:
    add(b,c)
elif a==2:
    sub(b,c)
elif a==3:
    mul(b,c)
elif a==4:
    div(b,c)
else:
    print("invalid choice")

