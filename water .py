# Agar water filter mein paani 1L se kam hai to aur paani bharna hai. 
# Agar paani 1L se 10L ke beech mein hai to aur nahi bharna.
#  Aur agar 10L se jyada hai to paani overflow kar jata hai. 
#  Neeche diye flowchart ko iss information ka use karke complete karo. 
#  Paani ke level ke liye aap user se ek water naam ke variable mein input lo,
#  aur fir usko integer mein convert kar lo.



 mas=int(input("enter the mesuremenline"))
if mas<=1:
    print("need to fill water")
elif mas>1 and mas<=10:
    print("dont need to fill water")
else:
    print("overflow")

