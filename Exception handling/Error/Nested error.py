try:
    l1=[1,2,3,4,5]
    print(l1[10])
    try:
        a=10
        b=0
        c=a/b
        print(c)
    except ZeroDivisionError as e:
        print(f"Error:{e}")
except IndexError as e2:
    print(f"Error:{e2}")
finally:
    print("Finally Executed")
print("Next Code")    
