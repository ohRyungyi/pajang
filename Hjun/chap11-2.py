# 261
class Stock():
    pass

# 262
class Stock():
    def __init__(self, name, code):
        self.name = name
        self.code = code

삼성 = Stock("삼성전자", "005930")

# 263
class Stock():
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_code(self, code):
        self.code =code

삼성 = Stock("삼성전자", "005930")
a = Stock(None, None)
a.set_code("005930")
print(a.code)

# 264
class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code =code    

a = Stock(None, None)
a.set_name("삼성전자")  # Stock.set_name(a, "삼성전자")
print(a.name)

# 265
class Stock:
    def __init__(self, name, code, per, pbr, 배당수익률):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code =code    

    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code
    
    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, dividend):
        self.dividend = dividend

    



# 267
삼성 = Stock('삼성전자', '005930', 15.79, 1.33, 2.83)
print(삼성.name)

# 268
# 위와 동일

# 269
삼성.set_per(12.75)
print(삼성.per)

# 270
종목 = []

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
    print(i.code, i.per) 