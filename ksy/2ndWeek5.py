#271
import random
class Account :
    def __init__(self, name, rest) :
        self.name = name
        self.rest = rest
        
        num1= random.randrange(100,999)
        num2= random.randrange(10,99)
        num3= random.randrange(100000,999999)
        
        self.account = "{}-{}-{}".format(num1,num2,num3)
        self.bank = "SC은행"

#272
class Account :
    account_count = 0
    def __init__(self, name, rest) :
        self.name = name
        self.rest = rest
        
        num1= random.randrange(100,999)
        num2= random.randrange(10,99)
        num3= random.randrange(100000,999999)
        
        self.account = "{}-{}-{}".format(num1,num2,num3)
        self.bank = "SC은행"

        Account.account_count +=1

Kim = Account("김소연", 100)
print(Account.account_count)
Lee = Account("리", 100)
print(Account.account_count)

#273
class Account :
    account_count = 0
    
    def __init__(self, name, rest) :
        self.name = name
        self.rest = rest
        
        num1= random.randrange(100,999)
        num2= random.randrange(10,99)
        num3= random.randrange(100000,999999)
        
        self.account = "{}-{}-{}".format(num1,num2,num3)
        self.bank = "SC은행"

        Account.account_count +=1
    
    def get_account_num(self) :
        print(Account.account_count)

    @classmethod #클래스메서드
    def get_account_num2(cls) :
        print(cls.account_count)

Kim = Account("김소연", 100)
print(Account.account_count)
Lee = Account("리", 100)
print(Account.account_count)
Kim.get_account_num()
Lee.get_account_num()
Account.get_account_num2()

#274
class Account :
    account_count = 0
    
    def __init__(self, name, rest) :
        self.name = name
        self.rest = rest
        
        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6) 
        
        self.account = "{}-{}-{}".format(num1,num2,num3)
        self.bank = "SC은행"

        Account.account_count +=1
    
    @classmethod #클래스메서드
    def get_account_num(cls) :
        print(cls.account_count)
    
    def deposit(self, deposit) :
        if deposit >=1 :
           self.rest += deposit

#275
class Account :
    account_count = 0
    
    def __init__(self, name, rest) :
        self.name = name
        self.rest = rest
        
        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6) 
        
        self.account = "{}-{}-{}".format(num1,num2,num3)
        self.bank = "SC은행"

        Account.account_count +=1
    
    @classmethod #클래스메서드
    def get_account_num(cls) :
        print(cls.account_count)
    

    def deposit(self, amount) :    
        if amount >=1 :
           self.rest += amount        
    
    def withdraw(self, amount) :
        if amount < self.rest :
            self.rest -= amount

#276

class Account :
    account_count = 0
    
    def __init__(self, name, rest) :
        self.name = name
        self.rest = rest
        
        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6) 
        
        self.account = "{}-{}-{}".format(num1,num2,num3)
        self.bank = "SC은행"

        Account.account_count +=1
    
    @classmethod #클래스메서드
    def get_account_num(cls) :
        print(cls.account_count)
    
    def deposit(self, amount) :
        if amount >=1 :
           self.rest += amount
    
    def withdraw(self, amount) :
        if amount < self.rest :
            self.rest -= amount
    
    def display_info(self) :
        self.rest = format(self.rest, ',')
        print("""
        은행이름 : {}
        예금주 : {}
        계좌번호 : {}
        잔고 : {}
        """ .format(self.bank, self.name, self.account, self.rest))

#277
class Account :
    account_count = 0
    
    def __init__(self, name, rest) :
        self.name = name
        self.rest = rest
        
        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6) 
        
        self.account = "{}-{}-{}".format(num1,num2,num3)
        self.bank = "SC은행"
        
        self.deposit_count = 0

        Account.account_count +=1 #객체가 아니라 전체 클래스의 account_count변수를 증가시키는 거임
    
    @classmethod #클래스메서드
    def get_account_num(cls) :
        print(cls.account_count)
    
    def deposit(self, amount) :
        if amount >=1 :
           self.rest += amount
           
           self.deposit_count +=1
           if self.deposit_count %5 ==0 :
               self.rest = self.rest*1.01

    
    def withdraw(self, amount) :
        if amount < self.rest :
            self.rest -= amount
    
    def display_info(self) :
        self.rest = format(self.rest, ',')
        print("""
        은행이름 : {}
        예금주 : {}
        계좌번호 : {}
        잔고 : {}
        """ .format(self.bank, self.name, self.account, self.rest))

#278
kim = Account("kim", 100)
lee = Account("lee'", 50)
park = Account("park", 25)

holder = [kim, lee, park] 

#279
for i in holder :
    if i.rest >=100 :
        i.display_info()

#280
class Account :
    account_count = 0
    
    def __init__(self, name, rest) :
        #해당 객체의 이름, 잔고
        self.name = name
        self.rest = rest
        
        #해당 객체의 계좌번호
        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6) 
        
        self.account = "{}-{}-{}".format(num1,num2,num3)
        self.bank = "SC은행"
        
        #해당 객체의 입금 횟수
        self.deposit_count = 0

        #해당 객체의 입금내역리스트
        self.deposit_list = []

        #해당 객체의 출금내역리스트
        self.withdraw_list = [] 

        #이 클래스의 생성횟수
        Account.account_count +=1 #객체가 아니라 전체 클래스의 account_count변수를 증가시키는 거임
    
    @classmethod #클래스메서드
    def get_account_num(cls) :
        print(cls.account_count)
    
    def deposit(self, amount) :
        if amount >=1 :
           self.rest += amount
           self.deposit_list.append(amount)
           
           self.deposit_count +=1
           if self.deposit_count %5 ==0 :
               self.rest = self.rest*1.01

    
    def withdraw(self, amount) :
        if amount < self.rest :
            self.rest -= amount
            self.withdraw_list.append(amount)
    
    def display_info(self) :
        self.rest = format(self.rest, ',')
        print("""
        은행이름 : {}
        예금주 : {}
        계좌번호 : {}
        잔고 : {}
        """ .format(self.bank, self.name, self.account, self.rest))

    def deposit_history(self) :
        print(self.deposit_list)
        for i in self.deposit_list :
            print(i)
    
    def withdraw_history(self) :
        print(self.withdraw_list)
        for i in self.withdraw_list :
            print(i)


k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()

k.withdraw(100)
k.withdraw(200)
k.withdraw_history()

