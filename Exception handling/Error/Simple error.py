try:
    a=10
    b=0
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print(f"Error:Don't divide by zero.Details:{e}")
    print("Next program")
    