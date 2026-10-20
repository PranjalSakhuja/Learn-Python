#CALCULATOR
print("CALCULATOR \nEnter any 2 numbers")

x=int(input())
y=int(input())
print("Enter operation(+,-,*,/)")
operator1=input()

if(operator1=='+'):
    r=x+y
    print("RESULT = ",r)

elif(operator1=='-'):
    r=x-y
    print("RESULT = ",r)

elif(operator1=='*'):
    r=x*y
    print("RESULT = ",r)

elif(operator1=='/'):
    if(y==0):
        print("DIVISION BY ZERO")
    else:
        r=x/y
        print("RESULT = ",r)

while(1):
    print("CONTINUE CALCULATOR(Y/N)")
    i=input()

    if(i=='y' or i=='Y'):
        print("Enter a number")
        z=int(input())
        print("Enter operation(+,-,*,/)")
        operator2=input()

        if(operator2=='+'):
            print("RESULT = ",z+r)

        elif(operator2=='-'):
            print("RESULT = ",z-r)

        elif(operator2=='*'):
            print("RESULT = ",z*r)

        elif(operator2=='/'):
            if(y==0):
                print("DIVISION BY ZERO")
            else:
                print("RESULT = ",r/z)

    elif(i=='n'or i=='N'):
        print("CALCULATOR CLOSED")
        break