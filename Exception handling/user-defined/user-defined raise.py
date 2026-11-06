
class NegativeError(Exception):
    def __init__(self,msg):
        super().__init__(msg)
try:
    n=int(input("Enter a no."))
    if n<0:
        err=NegativeError("No. must be postive")
        raise err 
    else:
        print(f"Number={n}")
except NegativeError as e:
    print(f"Error:{e}")

print("Next code")