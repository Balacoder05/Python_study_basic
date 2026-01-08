
number=int(input("Enter the number........"))
if number>0:
    print(f"{number}Positive")
elif number<0:
    print(f"{number}Negative")
else:
    print(f"{number}zero")


number=int(input("Enter your number...."))
if number%2==0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")



age=int(input("Enter your age...."))
if  age>=18:
    print(f"{age} eligible for voter")
else:
    print(f"{age}is not eligible for voter")



n=int(input("Enter the first number...."))
m=int(input("Enter the second number...."))
if n>m:
    print(f"{n} is grather then m")
else:
    print(f"{m}is grather then n")


marks=int(input("Enter your mark..."))
if marks>=35:
    print(f"{marks} is pass")
else:
    print(f"{marks} is not pass")



n=int(input("Enter the first number.."))
m=int(input("enter the second number.."))
o=int(input("Enter the third number.."))

if n>m and o:
    print(n, "is largest number" )
elif m>n and o:
    print(m, " is largest numbe")
else:
    print(o,"is largerst number")





marks=int(input("Enter your marks.."))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B ")
elif marks>=60:
    print("Grade C")
else:
    print("Fail")




year=int(input("Enter the year..."))
if  year%400==0:
    print("leap year")
elif year%4==0 and year%100!=0:
    print("leap year")
else:
    print("Not a leap year")


n=int(input("Enter the first number.."))
if n>=0:
    print("number is positive")


    n=int(input("Enter the first number.."))
    if n>0:
        print("number is positive")
    elif n<0:
        print("number is negative")
    else:
        print("number is 0")


n=int(input("Enter the first number.."))
if n%2==0:
    if n>2 and n<10:
        print("number is below 10")
    else:
        print("number is above 10")
else:
    print("Not an even number")


a=5
b=10

if a>b:print("a is big number")


c=100
d=20

print("c id grater then d ") if c>d else print("c is less then d")







# match case

language =input("Enter the language you want....")
match language:
    case "html" | "xhtml":  # use | one or more posibilities
        print("html language code")
    case "css":
        print("css language code")
    case "python":
        print("python language code")
    case _:
        print("other language code")