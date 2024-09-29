x=input("enter any number:")

match x:
    case 0:
        print("x is zero")
    case 1:
        print("x is one")
    case 2:
        print("x is two")
    case 3 | 4 | 5 :
        print("x is 3 , 4, 5")
    case _ if isinstance(x, str):
        print(x," is a string")

    case _:
        print ("value other than 1,2,3,4,5")
