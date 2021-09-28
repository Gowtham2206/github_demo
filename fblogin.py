name=input("Create your username")
phno=int(input("Enter your phone number"))
newpass=input("Create your new password")
def login():
    username=input("Enter your username")
    password=input("Enter your password")
    if(username==name and password==newpass):
        print("login successfull")
    else:
        for n in username:
            for m in password:
                if(username!=name and password!=newpass):
                    print("login failed")
                    print("Enter correct username and password")
                    username=input("Enter your username")
                    password=input("Enter your password")
                    if(username==name and password==newpass):
                        print("login successfull")
login()
                    
                    
