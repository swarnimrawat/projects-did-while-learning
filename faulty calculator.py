#exercise 2 - faulty calculator
#45 * 3 = 55, 56+9=77, 56/6 = 4
# desin a faulty calculator which print the following given question according to the given conditions and after that does all the operation correctly

n1=int(input("Enter your first number\n"))
n2=int(input("Enter your second number\n"))
opp=input("Choose operator (+ - * /)\n")
if opp=='+':
    if n1==56 and n2==9:
        print('77')
    else:
        print(n1+n2)
elif opp=='-':
    print(n1-n2)
elif opp=='*':
    if n1==45 and n2==3:
        print('555')
    else:
        print(n1*n2)
elif opp=='/':
    if n1==56 and n2==6:
        print('4')
    else:
        print(n1/n2)

