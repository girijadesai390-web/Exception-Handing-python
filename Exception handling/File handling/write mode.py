f=open("Add.txt","w")
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
c=a+b
f.write(f"1st no:{a}\n")
f.write(f"2nd no:{b}\n")
f.write(f"Ans:{c}\n")
f.close()