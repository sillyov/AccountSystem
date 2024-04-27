import database as db
luid = None
maxacc = len(db.accs) - 1
while True:
    userInput = input("> ")
    if userInput == 'help':
        print('''
> help - to get help
> login - to login
> reg - to register
        ''')
        userInput = input("> ")
    elif userInput == 'login':
        userInput = input("Login: ")
        login = userInput
        userInput = input("Password: ")
        password = userInput
        for i in range(0,len(db.accs)):
            if not(login != db.accs[i].login or password != db.accs[i].password):
                luid = i
                print(f"Welcome, {db.accs[luid].login}! You are {db.accs[luid].status}. Your UID is {db.accs[luid].uid}.")
                break
        if luid == None:
            print("Incorrect login or password")
    elif userInput == 'reg':
        userInput = input("Enter Your login: ")
        login = userInput
        userInput = input("Enter Your password: ")
        pass1 = userInput
        userInput = input("Confirm Your password: ")
        pass2 = userInput
        if pass1 != pass2:
            print("passwords does not match")
        else:
            with open('accountdb.txt','a+') as f:
                f.write(f'{login} ; {pass1} ; user ; {db.accs[maxacc].uid + 1}\n')
            print("Here we go! Now you can login using your data")
            userInput = input("> ") 
