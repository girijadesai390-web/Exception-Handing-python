try:
    l1=[1,2,3,4,5]
    a=10
    b=0
    c=a/b
    print(c)
    print(l1,[8])
except ZeroDivisionError as e:
    print(f"Error:Don't divide by zero.Details:{e}")
except IndexError as e2:
    print(f"Error:Incorrect Index")
print("Next Program")            