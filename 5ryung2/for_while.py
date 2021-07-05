# 131 -
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)
# 사과
# 귤
# 수박
# 출력

# 132 - 
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print("#####")
# #####
# #####
# #####

# 133 - 
# for 변수 in ["A", "B", "C"]:
#   print(변수)
print('A')
print('B')
print('C')

# 134 - 
# for 변수 in ["A", "B", "C"]:
#   print("출력:", 변수)
print('출력:',"A")
print('출력:','B')
print('출력:','C')

# 135 - 
# for 변수 in ["A", "B", "C"]:
#   b = 변수.lower()
#   print("변환:", b)
print('변환:','a')
print('변환:','b')
print('변환:','c')

# 136 - 
# 변수 = 10
# print(변수)
# 변수 = 20
# print(변수)
# 변수 = 30
# print(변수)
for i in [10, 20, 30]:
    print(i)

# 137 - 
# print(10)
# print(20)
# print(30)
for i in [10, 20, 30]:
    print(i)

# 138 - 
# print(10)
# print("-------")
# print(20)
# print("-------")
# print(30)
# print("-------")
for i in [10, 20, 30]:
    print(i, "-------", sep="\n")

# 139 - 
# print("++++")
# print(10)
# print(20)
# print(30)
for i in [0, 10, 20, 30]:
    if i ==0:
        print("++++")
    else:
        print(i)

# 140 - 
# print("-------")
# print("-------")
# print("-------")
# print("-------")
for i in range(4):
    print("-------")

# 141 - 
리스트 = [100, 200, 300]
for i in 리스트:
    print(i+10)

# 142 - 
리스트 = ["김밥", "라면", "튀김"]
for menu in 리스트:
    print('오늘의 메뉴:',menu)

# 143 - 
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in 리스트:
    print(len(i))

# 144 - 
리스트 = ['dog', 'cat', 'parrot']
for item in 리스트:
    print(item, len(item))

# 145 - 
리스트 = ['dog', 'cat', 'parrot']
for item in 리스트:
    print(item[0])

# 146 - 
리스트 = [1, 2, 3]
for item in 리스트:
    print("3 x %d" %item)

# 147 - 
리스트 = [1, 2, 3]
for item in 리스트:
    print("3 x %d = %d" %(item, item*3))

# 148 - 
리스트 = ["가", "나", "다", "라"]
for i in 리스트[1:]:
    print(i)

# 149 - 
리스트 = ["가", "나", "다", "라"]
for i in 리스트[::2]:
    print(i)

# 150 - 
리스트 = ["가", "나", "다", "라"]
for i in 리스트[::-1]:
    print(i)

# 151 - 
리스트 = [3, -20, -3, 44]
for i in 리스트:
    if i<0:
        print(i)

# 152 - 
리스트 = [3, 100, 23, 44]
for i in 리스트:
    if i%3 == 0:
        print(i)

# 153 - 
리스트 = [13, 21, 12, 14, 30, 18]
for i in 리스트:
    if i<20 and i%3 ==0:
        print(i)

# 154 - 
리스트 = ["I", "study", "python", "language", "!"]
for i in 리스트:
    if len(i)>=3:
        print(i)

# 155 - 
리스트 = ["A", "b", "c", "D"]
for i in 리스트:
    if i.isupper():
        print(i)

# 156 - 
리스트 = ["A", "b", "c", "D"]
for i in 리스트:
    if i.islower():
        print(i)

# 157 - 
리스트 = ['dog', 'cat', 'parrot']
for item in 리스트:
    # print(item.capitalize())
    # 답지 풀이
    print(item[0].upper(), item[1:], sep="")

# 158 -
리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
for file in 리스트:
    print(file.split('.')[0])

# 159 - 
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for file in 리스트:
    if file.split('.')[-1] == 'h':
        print(file)

# 160 -
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for file in 리스트:
    if file.split('.')[-1] == "h" or file.split('.')[-1] == "c":
        print(file)

# 161 - for && range
for i in range(100):
    print(i)

# 162 - for && range
for year in range(2002, 2051, 4):
    print(year)

# 163 - for && range or for && if
for num in range(1, 31):
    if num%3==0:
        print(num)

# 164 - for && range
for i in range(99, -1, -1):
    print(i)

# 165 - for && range
for i in range(0, 10):
    print(float(i/10))

# 166 - 
for i in range(9):
    print('3x%d = %d' %(i+1, (i+1)*3))

# 167 - 
for i in range(1, 10, 2):
    print('3x%d = %d' %(i, (i)*3))

# 168 - 
# danger : range(10) = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 로 확인
sum = 0
for i in range(1, 11, 1):
    sum+=i
print(sum)

# 169 - 
sum=0
for i in range(1, 11,2):
    sum+=i
print(sum)

# 170 - 
m =1
for i in range(1, 11):
    m *=i
print(m)

# 171 - for && range
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])

# 172 - for && range
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(i, price_list[i])

# 173 - for && range
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list) ):
    print(len(price_list)-i-1, price_list[i])

# 174 - 
price_list = [32100, 32150, 32000, 32500]
for i in range(1, len(price_list)):
    print((90+i*10),price_list[i])

# 175 - 
my_list = ["가", "나", "다", "라"]
for i in range(1, len(my_list)):
    print(my_list[i-1], my_list[i])

# 176 - 
my_list = ["가", "나", "다", "라", "마"]
for i in range(2, len(my_list)):
    print(my_list[i-2], my_list[i-1], my_list[i])

# 177 - 
my_list = ["가", "나", "다", "라"]
for i in range(-1, -len(my_list), -1):
    print(my_list[i], my_list[i-1])

# 178 - 
my_list = [100, 200, 400, 800]
for i in range(len(my_list)-1):
    print(my_list[i+1]-my_list[i])

# 179 - 
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(len(my_list)-2):
    print((my_list[i]+my_list[i+1]+my_list[i+2])/3)

# 180 - 
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)):
    volatility.append(high_prices[i]-low_prices[i])
print(volatility)

# 181 - 
apart = [['101호', '102호'], ['201호', '202호'] , ['301호', '302호']]
print(apart)

# 182 - 
stock = [['시가', 100, 200, 300],['종가', 80, 210, 330]]
print(stock)

# 183 - 
stock = {
    '시가' : [100, 200, 300],
    '종가' : [80, 210, 330]
}
print(stock)

# 184 - 
stock = {
    '10/10' : [80, 110, 70, 90],
    '10/11' : [210, 230, 190, 200]
}
print(stock)

# 185 - 
apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in range(len(apart)):
#     for j in range(len(apart[i])):
#         print(apart[i][j], '호')
for i in apart:
    for j in i:
        print(j,'호')

# 186 - 
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in range(len(apart)-1, -1, -1):
    for j in apart[i]:
        print(j,'호')

187 - 
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in range(len(apart)-1, -1, -1):
    for j in range(len(apart[i])-1, -1, -1):
        print(apart[i][j], '호')
# 답지 풀이
for i in apart[::-1]:
    for j in i[::-1]:
        print(j, '호')

# 188 - 
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::1]:
    for j in i[::1]:
        print(j, ' 호', '\n', '_'*5, '\n', sep = '')

# 189 - 
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::1]:
    for j in i[::1]:
        print(j, '호')
    print('_'*5)

# 190 -
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::1]:
    for j in i[::1]:
        print(j, '호')
print('_'*5)
 
# 191 - 
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for i in data[::1]:
    for j in i[::1]:
        print(j*(1.00014))

# 192 - 
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for i in data[::1]:
    for j in i[::1]:
        print(j*1.00014)
    print('_____')

# 193 - 
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = []
for i in data[::1]:
    for j in i[::1]:
        result.append(j*1.00014)
print(result)

# 194 - 
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
result = []
for i in data[::1]:
    result.append([])
    for j in i[::1]:
        result[-1].append(j*1.00014)
print(result)

# 195 - 
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1::1]:
    print(i[3])

# 196 - 
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1::1]:
    if i[3]>150:
        print(i[3])

# 197 - 
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1::1]:
    if i[0]<=i[3]:
        print(i[3])

# 198 - 
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
volatility = []
for i in ohlc[1::1]:
    volatility.append(i[1]-i[2])
print(volatility)

# 199 - 
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1::1]:
    if i[3]>i[0]:
        print(i[1]-i[2])

# 200 - 
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
money = 0
for i in ohlc[1:]:
    money+=i[3]-i[0]
print(money)
