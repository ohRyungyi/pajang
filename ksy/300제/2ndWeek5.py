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


#281
class Car :
    def __init__(self, wheel, price) :
        self.wheel = wheel
        self.price = price

car = Car(2,1000)
print(car.wheel)
print(car.price)

#282
class Bike(Car) :
    pass

#283
bicycle = Bike(2,100) 
print(bicycle.price)
#Bike 클래스에 별도로 __init__ 설정 안 해도 작동하는데...?

#284
class Bicycle(Car) :
    def __init__(self, wheel,price, div) :
        self.wheel = wheel
        self.price = price
        self.div = div

class Bicycle(Car) :
    def __init__(self, wheel, price, div) :
        super().__init__(wheel,price) #부모의 __init__을 불러옴
        self.div = div

bicycle = Bicycle(2,100,"시마노")
print(bicycle.div)

#285
class Car :
    def __init__(self, wheel, price) :
        self.wheel = wheel
        self.price = price
    
    def info(self) :
        print("바퀴수", self.wheel)
        print("가격", self.price)
    
car = Car(4, 1000)
car.info()

#286
class Car :
    def __init__(self, wheel, price) :
        self.wheel = wheel
        self.price = price
    
    def info(self) :
        print("바퀴수", self.wheel)
        print("가격", self.price)

class Bicycle(Car) :
    def __init__(self, wheel, price, div) :
        super().__init__(wheel, price)
        self.div = div
    
    def info(self) :
        super().info()
        print("구동계", self.div)

bicycle = Bicycle(2,100, "시마노")
bicycle.info()

#288
class 부모:
    def 호출(self):
        print("부모호출")

class 자식(부모):
    def 호출(self):
        print("자식호출")


나 = 자식()
나.호출() #오버라이딩

#289
class 부모:
      def __init__(self):
           print("부모생성")

class 자식(부모):
    def __init__(self) :
        print("자식생성")

나 = 자식()
#생성자 함수에 있는 것들은 생성하면 바로 실행됨

#290
class 부모:
      def __init__(self):
            print("부모생성")

class 자식(부모):
  def __init__(self):
        print("자식생성")
        super().__init__()

나 = 자식()

#부모클래스에 있는 함수(생성자를 포함해서)를 쓰고 싶으면 super().~~~

#291
f = open("asd.txt" , "w")
f.write("005930 삼성전자\n")
f.write("005380 현대차\n")
f.write("035420 NAVER")
f.close()

#292

#295
print("295번")
f = open("asd.txt", "r")
lines = f.readlines()
print("파일 읽어오기 : ", lines)
data = {}
for line in lines:
    print("lines에서 하나씩 : ", line)
    line = line.strip()
    print("strip() : ", line)
    k, v = line.split()
    print("split 후 k,v에 넣기 : ", k,v)
    data[k] = v

print(data)
f.close()

#296
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)


#297
per = ["10.31", "", "8.00"]
new_per = []

for i in per:
    try:
        v = float(i)
    except:
        v = 0
    new_per.append(v)

print(new_per)

#298
num1 = int(input("숫자를 입력하세요"))
num2 = int(input("숫자를 입력하세요"))

try : 
    print(num1/num2)
except ZeroDivisionError :
    print("0d으로 나누면 안 돼요")

#299
try :
    data = [1,2,3]

    for i in range(5) :
        print(data[i])
except IndexError as nope :
    print(nope) #nope으로 list index out of range 라는 문장을 출력함

#300
per = ["10.31","", "8.00"]

for i in per :
    print("for문 시작합니다")
    try : 
        print(float(i))
    except :
        print("오류발생함")
        print(0)
    else :
        print("오류 발생 안 함")
    finally :
        print("항상 실행함")