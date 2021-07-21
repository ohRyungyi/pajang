#241
import datetime
print(datetime.datetime.now()) 
#datetime모듈의 datetime객체??의 now함수

#242
now = datetime.datetime.now()
print(type(now))

#243
now = datetime.datetime.now()
for i in range(5,0,-1) :
    print(now - datetime.timedelta(days=i))

#244
now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))

#245
print(datetime.datetime.strptime("2020-05-04", "%Y-%m-%d" ))

#246
import time
import datetime

#while True :
    # now = datetime.datetime.now()   
    # print(now) 
    # time.sleep(1)

#247
# import datetime
# from datetime import *
# from datetime import datetime
# import datetime as dt

#248
import os
print(os.getcwd())

#249

#250
# import numpy as np #왜 import가 안 될까
# for i in np.arange(0.0, 5.0, 0.1) :
#     print(i)

#251

#252
class Human : 
    pass

#253
areum = Human() #바인딩

#254
class Human :
    def __init__(self):
        print("응애응애")

areum = Human()

#255
class Human :
    def __init__(self, name, age, gender) :
        self.name = name
        self.age = age
        self.gender = gender

areum = Human("아름" ,25, "여자")
print(areum.name)

#256
print(areum.age)
print(areum.gender)

#257
class Human :
    def __init__(self, name, age, gender) :
        self.name = name
        self.age = age
        self.gender = gender
    def who(self) :
        print("이름 : {} , 나이 : {} , 성별 : {}" .format(self.name, self.age, self.gender))

areum = Human("조아름", 25, "여자")
areum.who()

#258 ==> 블로그로 옮기기
class Human :
    def __init__(self, name, age, gender) :
        self.name = name
        self.age = age
        self.gender = gender
    def who(self) :
        print("이름 : {} , 나이 : {} , 성별 : {}" .format(self.name, self.age, self.gender))
    def setInfo(self, name, age, gender) :
        self.name = name
        self.age = age
        self.gender = gender

areum = Human("모름", 0, "모름")
print(areum.name)

areum.setInfo("아름", 25, "여자")
print(areum.name)

#259
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print("나의 죽음을 알리지마라")

    def who(self):
        print("이름: {} 나이: {} 성별: {}".format(self.name, self.age, self.sex))

    def setInfo(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("아름", 25, "여자")
del(areum)

#261
class Stock :
    pass

#262
class Stock :
    def __init__(self, name, code) :
        self.name = name
        self.code = code

#263
class Stock :
    def __init__(self, name, code) :
        self.name = name
        self.code = code
    def set_name(self, name) :
        self.name = name

a = Stock(None, None)
a.set_name("삼성전자")
print(a.name)

#264
class Stock :
    def __init__(self, name, code) :
        self.name = name
        self.code = code
    def set_name(self, name) :
        self.name = name
    def set_code(self, code) :
        self.code = code

a = Stock(None, None)
a.set_code("005930")

#265
class Stock :
    def __init__(self, name, code) :
        self.name = name
        self.code = code
    def set_name(self, name) :
        self.name = name
    def set_code(self, code) :
        self.code = code
    def get_name(self) :
        return self.name
    def get_code(self) :
        return self.code

삼성 = Stock("삼성전자", "005930")
print(삼성.get_name())
print(삼성.get_code())

#266
class Stock :
    def __init__(self, name, code, PER, PBR, rate) :
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.rate = rate
    def set_name(self, name) :
        self.name = name
    def set_code(self, code) :
        self.code = code
    def get_name(self) :
        return self.name
    def get_code(self) :
        return self.code

#267
삼성전자 = Stock("삼성전자", "005930",15.79, 1.33, 2.83)

#268
class Stock :
    def __init__(self, name, code, per, pbr, devidend) :
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.devidend = devidend
    def set_name(self, name) :
        self.name = name
    def set_code(self, code) :
        self.code = code
    def set_per(self, per) :
        self.per = per
    def set_pbr(self,pbr) :
        self.pbr = pbr
    def set_dividend(self,devidend) :
        self.devidend = devidend
    def get_name(self) :
        return self.name
    def get_code(self) :
        return self.code

#269
삼성전자 = Stock("삼성전자", "005930",15.79, 1.33, 2.83)
삼성전자.set_per(12.75)
print(삼성전자.per)

#270
현대차  = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

stock_list = [삼성전자, 현대차, LG전자]

for i in stock_list :
    print(i.code, i.per)
    
