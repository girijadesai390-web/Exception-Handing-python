f=open("Circle.txt","a")
r=int(input("Enter radius"))
a=3.14*r*r
f.write(f"Radius:{r}\n")
f.write(f"Area:{a}\n")
f.close()