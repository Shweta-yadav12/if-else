



sub=input("enter the number")
per=int(input("enter the number"))
if sub=="physies":
    print("grade E") 
    if per>=90:
        print("grade A")
elif sub=="chemistry":
    if per>=80:
        print("grade B") 
elif sub=="biology":
    if per>=70:
        print("grade C")            
elif sub=="mathematics":
    if per>=60:
        print("grade D")
elif sub=="computer":
    if per>=40:    
        print("grade E") 
else:
    print("grade F")
