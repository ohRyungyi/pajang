# 271
import random
class Account():
    cnt = 0
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.bank_name = "SC은행"
        self.deposit_cnt = 0
        self.deposit_his = []
        self.withdraw_his = []
        ran1 = str(random.randint(0,999))
        ran2 = str(random.randint(0,99))
        ran3 = str(random.randint(0,999999))
        self.account_num = ran1.zfill(3)+'-'+ran2.zfill(2)+'-'+ran3.zfill(6)
        Account.cnt +=1
    @classmethod
    def get_account_num(acc):
        print(acc.cnt)

    def deposit(self, plus_money):

        if plus_money>=1:            
            self.money += plus_money
            self.deposit_his.append(plus_money)
            if self.deposit_cnt %5==0:
                self.money*=1.01  
                self.deposit_his.append(plus_money)  
        else: 
            print('최소 입금금액은 1원입니다.')

    def withdraw(self, minus_money):
        if minus_money <= self.money:
            self.money -= minus_money
            self.withdraw_his.append(minus_money)
        else:
            print(f'{self.money}초과한 금액입니다.')
    
    def display_info(self):
        print(f'은행이름: {self.bank_name}')
        print(f'예금주: {self.name}')
        print(f'계좌번호: {self.account_num}')
        print(f"잔고: {self.money}원")

    def deposit_history(self):
        for i in self.deposit_his:
            print(f'입금: {i}')
    
    def withdraw_history(self):
        for i in self.withdraw_his:
            print(f'출금: {i}')

ok = []
HJ = Account('이형준', 50000)        
JY = Account('이지예', 600000)
KA = Account('카카오', 100000000)
ok.append(HJ)
ok.append(JY)
ok.append(KA)
for i in ok:
    if i.money >=1000000:
        i.display_info()