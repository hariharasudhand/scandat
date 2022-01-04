"""
i = int(input("enter the number"))

r = i % 2

while r==1:
    print("you are good")
"""

i = 1

while (True):
    a = int(input("enter the number"))
    j = a % 2
    if j == 0:
        print("you are great")
    elif j==1:
        print("it is odd then it exit ")
        break
    i = i + 1


