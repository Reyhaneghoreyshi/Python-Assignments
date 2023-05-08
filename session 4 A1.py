import random
pc_number= random.randint(1,20)
i= 1
while True :
    user_number=int(input("enter number:"))
    if user_number== pc_number:
        print("barande shodin")
        print("number of guess :",i)
        break
    if user_number < pc_number:
       print(" bro balater")
    if user_number > pc_number:
        print(" bro paeenter")
    else:
        print(" eshtebah bud:D")

    i=i+1

    