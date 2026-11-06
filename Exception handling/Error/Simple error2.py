l1=[1,2,3,4,5]
print(l1,[8])
IndexError
try:
    l1=[1,2,3,4,5]
    print(l1,[8])
except IndexError as e:
    print(f"Error:{e}")
print("Next code")        