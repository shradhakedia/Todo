print("Welcome to health management software")
name={1:"Harry",2:"Rohan",3:"Hammad"}
plan={1:"Diet",2:"Exercise"}
def getdate():
    import datetime
    return datetime.datetime.now()
def log_data():
    try:
        n=int(input(f"Enter 1 if you want to log in details for {name[1]}\nEnter 2 if you want to log in details for {name[2]}\nEnter 3 if you want to log in details for {name[3]}\nEnter you choice:"))
        if n==1:
            print(f"You can login {name[1]}'s details")
            k='y'
            while k=='y':
                choice=int(input(f"Enter 1 for {plan[1]} log in\nEnter 2 for {plan[2]} login\nEnter your choice:"))
                if choice==1:
                    f=open(name[1]+plan[1]+".txt","a")
                    f.write("["+str(getdate())+"]:"+input()+"\n")
                    f.close()
                elif choice==2:
                    f=open(name[1]+plan[2]+".txt","a")
                    f.write("["+str(getdate())+"]:"+input()+"\n")
                    f.close()
                k=input("Enter y to add more else Enter n:")
                if k=='n':
                    break
        elif n==2:
            print("You can login",name[2],"'s details")
            k='y'
            while k=='y':
                choice=int(input(f"Enter 1 for {plan[1]} log in\nEnter 2 for {plan[2]} login\nEnter your choice:"))
                if choice==1:
                    f=open(name[2]+plan[1]+".txt","a")
                    f.write("["+str(getdate())+"]:"+input()+"\n")
                    f.close()
                elif choice==2:
                    f=open(name[2]+plan[2]+".txt","a")
                    f.write("["+str(getdate())+"]:"+input()+"\n")
                    f.close() 
                k=input("Enter y to add more else Enter n:")
                if k=='n':
                    break
        elif n==3:
            print("You can login",name[3],"'s details")
            k='y'
            while k=='y':
                choice=int(input(f"Enter 1 for {plan[1]} log in\nEnter 2 for {plan[2]} login\nEnter your choice:"))
                if choice==1:
                    f=open(name[3]+plan[1]+".txt","a")
                    f.write("["+str(getdate())+"]:"+input()+"\n")
                    f.close()
                elif choice==2:
                    f=open(name[3]+plan[2]+".txt","a")
                    f.write("["+str(getdate())+"]:"+input()+"\n")
                    f.close()
                k=input("Enter y to add more else Enter n:")
                if k=='n':
                    break
        else:
            print("invalid choice")
    except Exception as e:
        print("invalid input")
def retrieve_data():
    n=int(input("Enter 1 if you want to see details of "+name[1]+"\nEnter 2 if you want to see details of "+name[2]+"\nEnter 3 if you want to see details of "+name[3]+"\nEnter your choice:"))
    if n==1:
        print(f"You can see {name[1]}'s details")
        choice=int(input(f"Enter 1 to see his {plan[1]} chart\nEnter 2 see his {plan[2]} chart\nEnter your choice:"))
        if choice==1:
            f=open(name[1]+plan[1]+".txt","r")
            print(f.read())
            f.close()
        elif choice==2:
            f=open(name[1]+plan[2]+".txt","r")
            print(f.read())
            f.close()
        else:
            print("invalid choice")
    elif n==2:
        print(f"You can see {name[2]}'s details")
        choice=int(input(f"Enter 1 to see his {plan[1]} chart\nEnter 2 for to see his {plan[2]} chart\nEnter your choice:"))
        if choice==1:
            f=open(name[2]+plan[1]+".txt","r")
            print(f.read())
            f.close()
        elif choice==2:
            f=open(name[2]+plan[2]+".txt","r")
            print(f.read())
            f.close()
        else:
            print("invalid input")
    elif n==3:
        print(f"You can see {name[3]}'s details")
        choice=int(input(f"Enter 1 to see his {plan[1]} chart\nEnter 2 to see his {plan[2]} plan\nEnter your choice:"))
        if choice==1:
            f=open(name[3]+plan[1]+".txt","r")
            print(f.read())
            f.close()
        elif choice==2:
            f=open(name[3]+plan[2]+".txt","r")
            print(f.read())
            f.close()
        else:
            print("invalid input")
    else:
        print("invalid input")
log_data()
retrieve_data()