class AgeError(Exception):
    def __init__(self,msg):
        super().__init__(msg)
try:
    age=int(input("Enter a age"))
    if age>18 and age<45:
        err=AgeError("Age must be within range")
        raise err 
    else:
        print(f"Number={n}")
except AgeError as e:
    print(f"Error:{e}")

print("Next code")