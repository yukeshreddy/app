count=0
total_amt=40000
D={100:20,200:20,500:20,2000:20}
def admin():
    global total_amt
    name='yuk'
    pas=1234
    b=input("Enter the name:")
    c=int(input("Enter the password:"))
    if b==name and c==pas:
        print("sucessfully logged in into ADMIN")
        while True:
            print("1.LOAD","\n2.CHECK","\n3.EXIT")
            d=int(input("Enter your option:"))
            if d==1:
                for i in D:
                    print("enter no.of",i,"notes:")
                    e=int(input())
                    D[i]=D[i]+e
                    total_amt=total_amt+(e*i)
                print("amount is sucessfully added to your account","\nyour balance is:",total_amt)
            elif d==2:
                for i in D:
                    print(i,"'s are",D[i])
            elif d==3:
                break
            else:
                print("xxx invalid option xxx")
    else:
        print("sry try again")
    
            
              
def user():
    L={2000:0,500:0,200:0,100:0}
    K={2000:0,500:0,200:0,100:0}
    global total_amt,count
    name='red'
    pin=5555
    amt=30000
    while True:
        while count<3:
            k=input("Enter the name:")
            e=int(input("Enter your pin:"))
            if e==pin and k==name:
                print("Sucessfully logged in into USER")
                print("1.Withdraw","\n2.Balance check","\n3.Pin change","\n4.DEPOSIT","\n5.EXIT")
                f=int(input("Enter your option:"))
                if f==1:
                    g=int(input("Enter the amount:"))
                    if g<total_amt and g%100==0 and g<amt:
                        s=g
                        for i in L:
                            L[i]=s//i
                            s=s%i
                        count1=0
                        for i in L:
                            if D[i]>=L[i]:
                                count1+=1
                        if count1==4:
                            print("take your cash")
                            amt=amt-g
                            print("your account balance is:",amt)
                        else:
                            print("invalid amount in the ATM")
                    else:
                        print("***invalid amount***")
                            
                elif f==2:
                    print("Your account balance is:",amt)
                elif f==3:
                    h=int(input("Enter the old pin:"))
                    i=int(input("Enter your new pin:"))
                    print("Your pin has been changed sucessfully")
                    pin=i
                elif f==4:
                    print("Deposit your amount here")
                    while True:
                        ad=0
                        for i in K:
                            print("Enter no.of",i,"notes")
                            j=int(input())
                            K[i]=K[i]+j
                            ad=ad+j*i
                        cash=int(input("Enter the cash:"))
                        if cash==ad:
                            amt=amt+ad
                            print("\tYour amount",cash,"is sucessfully added to your account")
                            print("\tYour balance is",amt)
                            break
                        else:
                            print("\tyou have done a mistake pls do again")
                elif f==5:
                    print("Exited sucessfully")
                    return
                else:
                    print("invalid option")
                        
                    
                        
                   
            else:
                count+=1
                print("Wrong pin")
        print("\t***your account is blocked temporarly***","\n\t***Please vist near by Bank***")
                
while True:
    print("Welcome to ATM")
    print("1.ADMIN","\n2.USER","\n3.EXIT")
    a=int(input("Enter the option:"))
    if a==1:
        admin()
    elif a==2:
        user()
    elif a==3:
        break
    else:
        print("Invalid option")
