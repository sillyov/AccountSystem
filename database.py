accs = []
dbase = open('accountdb.txt','r')

class Account:
    
    def __init__(self,login,password,status,uid):
        self.login = login
        self.password = password
        self.status = status
        self.uid = int(uid)
for ln in dbase:
    data = ln.rstrip().split(' ; ')
    nwa = Account(data[0],data[1],data[2],data[3])  #  0 is for login, 1 is for password, 2 is for status, 3 is for uid
    accs.append(nwa)
