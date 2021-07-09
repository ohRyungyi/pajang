# 251
# 클래스 = 
# 객체 = 
# 인스턴스 = 

# 252
class Human:
    pass

# 253
class Human:
    pass

areum = Human()

# 254
class Human:
    def __init__(self):
        print('응애응애')

areum = Human()

# 255
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
areum = Human("아름", 25, "여자")

256
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
areum = Human("아름", 25, "여자")
print(areum.name, areum.age, areum.gender)

# 257
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def who(self):
        print(self.name, self.age, self.gender)
areum = Human("아름", 25, "여자")
areum.who()

# 258
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def setInfo(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def who(self):
        print(f'이름 : {self.name} , 나이 : {self.age} , 성별 : {self.gender}')
areum = Human("모름", 0, "모름")
areum.who()
areum.setInfo("아름", 25, "여자")
areum.who()

# 259
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __del__(self):
        print('나의 죽음을 알리지 마라')
areum = Human("아름", 25, "여자")
# del areum
del(areum)

# 260
# class OMG : 
#     def print() :
#         print("Oh my god")
# OMG 객체 내의 메소드내에 self라는 매개 변수가 없어서 에러가 발생

class OMG : 
    def print(self) :
        print("Oh my god")
mystock = OMG()
mystock.print()

# 261
class Stock:
    pass

# 262
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
삼성 = Stock("삼성전자", "005930")
print(삼성.name)
print(삼성.code)

# 263
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    def set_name(self, name):
        self.name = name
a = Stock(None, None)
print(a.name)
a.set_name('samsung')
print(a.name)

# 264
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    def set_name(self, name):
        self.name = name
    
    def set_code(self, code):
        self.code = code
a = Stock(None, None)
print(a.code)
a.set_code("005930")
print(a.code)

# 265
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code
    
    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code
a = Stock('삼성', '005930')
print('종목명 :', a.get_name())
print('종목코드 :', a.get_code())

# 266
# 종목명, 종목코드, PER, PBR, 배당수익률
class Stock :
    def __init__(self, name, code, PER, PBR, 배당수익률):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.배당수익률 = 배당수익률

# 267
# 삼성전자, 0059430, 15.79, 1.33, 2.83
class Stock:
    def __init__(self, name, code, PER, PBR, ratio) :
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.ratio = ratio
stock = Stock('삼성전자', '0059430', 15.79, 1.33, 2.83)
print(stock.name, stock.code, stock.PER, stock.PBR, stock.ratio)

# 268
class Stock:
    def __init__(self, name, code, PER, PBR, dividend):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.dividend = dividend

    def set_per(self, PER) :
        self.PER = PER

    def set_pbr(self, PBR):
        self.PBR = PBR

    def set_dividend(self, dividend):
        self.dividend = dividend

# 269
class Stock:
    def __init__(self, name, code, PER, PBR, dividend):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.dividend = dividend

    def set_per(self, PER) :
        self.PER = PER

    def set_pbr(self, PBR):
        self.PBR = PBR

    def set_dividend(self, dividend):
        self.dividend = dividend
stock = Stock('삼성전자', '0059430', 15.79, 1.33, 2.83)
print(stock.PER)
stock.set_per(12.75)
print(stock.PER)

# 270
class Stock:
    def __init__(self, name, code, PER, PBR, dividend):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.dividend = dividend

    def set_per(self, PER) :
        self.PER = PER

    def set_pbr(self, PBR):
        self.PBR = PBR

    def set_dividend(self, dividend):
        self.dividend = dividend

    def get_per(self):
        return self.PER

    def get_pbr(self):
        return self.PBR
    
    def get_dividend(self):
        return self.dividend

# 삼성전자	005930	15.79	1.33	2.83
# 현대차	005380	8.70	0.35	4.27
# LG전자	066570	317.34	0.69	1.37
item = []
item.append(Stock('삼성전자', '005930', 15.79, 1.33, 2.83))
item.append(Stock('현대차', '00580', 8.70, 0.35, 4.27))
item.append(Stock('LG전자', '066570', 317.34, 0.69, 1.37))

for i in item:
    print(f'종목명 : {i.code} ,  PER : {i.PER}')
    
# 271
# 은행이름, 예금주, 계좌번호, 잔액
import random

class Account:
    def __init__(self, user, total):
        self.user = user
        self.total = total
        number = ''
        # _ _ _-_ _-_ _ _ _ _ _
        for i in range(11):
            now = str(random.randint(0, 10))
            number+=now
            if i==2:
                number+='-'
            elif i==4:
                number+='-'
        self.number = number
        self.bank = 'SC은행'

account = Account('user1', 1000)
print(account.user, account.total, account.number, account.bank)

# 272
import random

class Account:
    total_count = 0
    def __init__(self, user, total):
        self.user = user
        self.total = total
        number = ''
        # _ _ _-_ _-_ _ _ _ _ _
        for i in range(11):
            now = str(random.randint(0, 10))
            number+=now
            if i==2:
                number+='-'
            elif i==4:
                number+='-'
        self.number = number
        self.bank = 'SC은행'

        Account.total_count +=1

kim = Account("김민수", 100)
print(Account.total_count)
lee = Account("이민수", 100)
print(Account.total_count)

# 273
import random

class Account:
    total_count = 0
    def __init__(self, user, total):
        self.user = user
        self.total = total
        number = ''
        # _ _ _-_ _-_ _ _ _ _ _
        for i in range(11):
            now = str(random.randint(0, 10))
            number+=now
            if i==2:
                number+='-'
            elif i==4:
                number+='-'
        self.number = number
        self.bank = 'SC은행'

        Account.total_count +=1

    @classmethod
    def get_account_num(cls):
        print(cls.total_count)

kim = Account("김민수", 100)
lee = Account("이민수", 100)
kim.get_account_num()

# 274
import random

class Account:
    total_count = 0
    def __init__(self, user, total):
        self.user = user
        self.total = total
        number = ''
        # _ _ _-_ _-_ _ _ _ _ _
        for i in range(11):
            now = str(random.randint(0, 10))
            number+=now
            if i==2:
                number+='-'
            elif i==4:
                number+='-'
        self.number = number
        self.bank = 'SC은행'

        Account.total_count +=1

    @classmethod
    def get_account_num(cls):
        print(cls.total_count)

    def deposit(self, amount):
        if amount>=1:
            self.total += amount

kim = Account("김민수", 100)
print(kim.total)
kim.deposit(200)
print(kim.total)

# 275
import random

class Account:
    total_count = 0
    def __init__(self, user, total):
        self.user = user
        self.total = total
        number = ''
        # _ _ _-_ _-_ _ _ _ _ _
        for i in range(11):
            now = str(random.randint(0, 10))
            number+=now
            if i==2:
                number+='-'
            elif i==4:
                number+='-'
        self.number = number
        self.bank = 'SC은행'

        Account.total_count +=1

    @classmethod
    def get_account_num(cls):
        print(cls.total_count)

    def deposit(self, amount):
        if amount>=1:
            self.total += amount

    def withdraw(self, ammount):
        if self.total>=ammount:
            self.total -=ammount

kim = Account("김민수", 300)
print(kim.total)
kim.withdraw(200)
print(kim.total)

# 276
# 은행이름: SC은행
# 예금주: 파이썬
# 계좌번호: 111-11-111111
# 잔고: 10,000원
import random

class Account:
    account_num = 0
    def __init__(self, user, balance):
        self.user = user
        self.bank = 'SC은행'
        self.balance = balance
        
        first = random.randint(1, 999)
        mid = random.randint(1, 99)
        last = random.randint(1, 999999)

        first = str(first).zfill(3)
        mid = str(mid).zfill(2)
        last = str(last).zfill(6)
        self.bank_account = first+'-'+mid+'-'+last

        Account.account_num += 1
    
    def display_info(self):
        print(f'은행이름: {self.bank}')
        print(f'예금주: {self.user}')
        print(f'계좌번호: {self.bank_account}')
        print(f'잔고: {self.balance}원')

kim = Account("김민수", 300)
kim.display_info()

# 277
import random

class Account:
    account_num = 0

    def __init__(self, user, balance):
        self.bank = 'SC은행'
        self.user = user
        self.balance = balance

        first  = random.randint(1, 999)
        mid = random.randint(1, 99)
        last = random.randint(1, 999999)

        first = str(first).zfill(3)
        mid = str(mid).zfill(2)
        last = str(last).zfill(6)

        self.bank_account = first+'-'+mid+'-'+last

        self.deposit_num = 0
    
    def deposit(self, amount):
        self.deposit_num += 1

        if amount>=1:
            self.balance += amount

            if self.deposit_num >= 5:
                self.balance += int(self.balance*0.1)

p = Account("파이썬", 10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(5000)
p.deposit(5000)
print(p.balance)

# 278
import random

class Account:

    def __init__(self, user, balance):
        self.user = user
        self.bank_name = 'SC은행'
        self.balance = balance

        first = random.randint(1, 999)
        mid = random.randint(1, 99)
        last = random.randint(1, 999999)

        first = str(first).zfill(3)
        mid = str(mid).zfill(2)
        last = str(last).zfill(6)

        self.bank_account = first+'-'+mid+'-'+last

account = []

account.append(Account('Kim', 10000000))
account.append(Account('Lee', 10000))
account.append(Account('park', 10000))

for i in account:
    print(i.user)

# 279
import random

class Account:

    def __init__(self, user, balance):
        self.user = user
        self.bank_name = 'SC은행'
        self.balance = balance

        first = random.randint(1, 999)
        mid = random.randint(1, 99)
        last = random.randint(1, 999999)

        first = str(first).zfill(3)
        mid = str(mid).zfill(2)
        last = str(last).zfill(6)

        self.bank_account = first+'-'+mid+'-'+last

    def display_info(self):
        print(f'은행이름: {self.bank_name}')
        print(f'예금주: {self.user}')
        print(f'계좌번호: {self.bank_account}')
        print(f'잔고: {self.balance}원')

account = []

account.append(Account('Kim', 10000000))
account.append(Account('Lee', 10000))
account.append(Account('park', 10000))

for i in account:
    if i.balance >= 1000000:
        i.display_info()

# 280
import random

class Account:

    def __init__(self, user, balance):
        self.user = user
        self.bank_name = 'SC은행'
        self.balance = balance

        first = random.randint(1, 999)
        mid = random.randint(1, 99)
        last = random.randint(1, 999999)

        first = str(first).zfill(3)
        mid = str(mid).zfill(2)
        last = str(last).zfill(6)

        self.bank_account = first+'-'+mid+'-'+last

        self.deposit_log = []
        self.deposit_num = 0
        self.withdraw_log = []

    def display_info(self):
        print(f'은행이름: {self.bank_name}')
        print(f'예금주: {self.user}')
        print(f'계좌번호: {self.bank_account}')
        print(f'잔고: {self.balance}원')

    def deposit(self, amount):
        self.deposit_num += 1
        if amount>=1:
            self.balance += amount
            self.deposit_log.append(amount)

            if self.deposit_num >= 5:
                self.balance += int(self.balance*0.1)
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance += amount

            self.withdraw_log.append(amount)

    def deposit_history(self):
        for amount in self.deposit_log:
            print(f'deposit : {amount}')

    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(f'widthraw : {amount}')

k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()

k.withdraw(100)
k.withdraw(200)
k.withdraw_history()