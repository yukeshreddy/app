user={'user1':{'password':'u1','wallet':500,'cart':{}},'user2':{'password':'u2','wallet':500,'cart':{}}}
merl={"Mer1":{"password":"1111","products":{}}}
things={'search':{'categories':{'Mobiles':{'redmi','realme','honor','oppo','vivo','samsung'},
                  'chocolates':{'1':'fivestar','2.':'dairymilk'},'food products':{'1':'rice','2.':'maida','3.':'salt'}}}}
apmer={}
rejmer={}
def rem_cart():
    print(user[us][uspass]['cart'])

def add_cart():
    print('select the products to add to cart')
    print(*things['search']['categories'].keys(),sep=" or ")
    ann=input('Enter the products:')
    if ann in things['search']['categories'].keys():
        print(things['search']['categories'][ann].keys(),sep=' or ')
        an=input('select the products:')
        if an in things['search']['categories'][ann]:
            user[us][uspass]['cart'].update(an)
            print('\t***your products are added to cart***')

def newuser():
    print('Enter user name:')
    co=input()
    print('Enter the password:')
    coo=input()
    if co not in user:
        nus={'co':{'password':coo,'wallet':0,'cart':{}}}
        user.update(nus)
        print(co,'is sucessfully added to user')
        input('\tPress enter to continue')
    else:
        print('**pls change the user name**')
def exiuser():
    print('Enter user name:')
    us=input()
    print('Enter the password:')
    uspas=input()
    if user[us]['password']==uspas:
        print('\tSucessfully looged in into user')
        while True:
            print('1.Add cart','\n2.wallet','\n3.remove cart','\n4.Exit')
            ch=int(input('Enter your choice:'))
            if ch==1:
                add_cart()
            elif ch==2:
                print(user[inu]['wallet'])
            elif ch==3:
                rem_cart()
            elif ch==4:
                break
            else:
                print('Invalid option')
    else:
        print('Invalid user')

        
def users():
    while True:
        print('1.New user','\n2.Existing user','\n3.Exit')
        imp=int(input('Enter your choice'))
        if imp==1:
            newuser()
        elif imp==2:
            exiuser()
        elif imp==3:
            break
     

def eximer():
    mlog=input("Enter the merchant Name:")
    mpass=input("Enter your password:")
    if merl[mlog]['password']==mpass:
        print('Sucessfully logged in')
    else:
        print("invalid login")
        input("\tpress Enter to continue")
def aprmer():
    if len(apmer)!=0:
        print('select merchant')
        print(*apmer.keys())
        B=input()
        if B in apmer.keys():
            print("Enter 1 to approve and 0 to raject:")
            adc=input()
            if adc=="1":
                aprmer.update(e,g)
            elif adc=="0":
                rejmer.update(e,g)
            else:
                print("Invalid Input")
        else:
            print("invalid name")
            input("\tpress Enter to continue")
    else:
        print("No new requests")
        input("\tpress Enter to continue")
def remmer():
    print("select merchant to remove",end=":")
    print(*merl.keys())
    rem=input()
    if rem in merl:
        merl.pop(rem)
        print("sucessfully removed")
        input("\tpress Enter to continue")
    else:
        print("invalid merchant")
        input("\tpress Enter to continue")
    
def merchant():
    print("welcome to merchant login")
    while True:
        print("1.New Merchant","\n2.Existing merchant","\n3.Exit")
        me=input("Enter your choice:")
        if me=='1':
            newmerchant()
        elif me=='2':
            eximer()
        elif me=='3':
            break
        else:
            print('invalid option')
            
        
def newmerchant():
    while True:
        e=input("Enter your name:")
        f=input('Enter the password:')
        g=input("confirm the pasword")
        if f==g:
            if e not in merl:
                A={e:{'password':g}}
                apmer.update(A)
                print("Requested approval")
                input("\tpress Enter to continue")
                break
            else:
                print("pls change the merchant name and try again")
                input("\tpress Enter to continue")
        else:
            print("\tThe two passwords are not matching try again")

            
def admin():
    name="admin"
    pin="1234"
    b=input("Enter the name:")
    c=input("Enter the pin:")
    if b==name and c==pin:
        while True:
            print("Sucessfully logged in Admin")
            print("1.approve Merchant","\n2.Remove merchant","\n3.Exit")
            d=int(input("Enter your option:"))
            if d==1:
                aprmer()
            elif d==2:
                remmer()
            elif d==3:
                break
            else:
                print("invalid option")
    else:
        print("\twrong entry pls try again")

                
        
while True:
    print("\t**WELCOME TO AMAZON**")
    print("1.ADMIN","\n2.MERCHANT","\n3.USER","\n4.EXIT")
    a=int(input("Enter your option:"))
    if a==1:
        admin()
        
    elif a==2:
        print("Sucessfully logged in Merchant")
        merchant()
    elif a==3:
        users()
    elif a==4:
        break
    else:
        print("\txxx  invalid option  xxx")
