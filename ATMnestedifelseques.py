

prosece=input("enter the proesce")
if prosece=="card insert":
    print("except")
    bank=input("enter your choose")
    if bank=="banking" or bank=="service":
        print("bank except")
        language=input("enter your language")
        if language=="english" or language=="hindi":
            print("except language")
            pincode=input("enter your pincode")
            if pincode=="pu1234":
                print("pincode except")
                account=input("type of account")
                if account=="saving"or account=="current":
                    print("account accept")
                    amout=int(input("enter your amount"))
                    if amount<10000:
                        print("amoant preped")
                        recipt=input("i want recipt")
                        if recipt=="yes":
                            print("except")
                        else:
                            print("not except recip")
                    else:
                        print("not preped amount")    
                else:
                    print("not except account")
            else:
                print("not except pincode")
        else:
            print("other language")
    else:
        print("other bank")
else:
    print("insert again")
