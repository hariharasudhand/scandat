

a = 5
b = 6

try:
    print(a/b)

    k = int(input("enter the number"))
    print(k)
except ZeroDivisionError as e:
    print("the number is not divisible", e)

except ValueError as e:
    print("the value was error", e)

except Exception as m :
    print(m)