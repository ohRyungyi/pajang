#181
apart = [["101호", "102호"],["201호", "202호"], ["301호","302호"]]

#182
stock = [["시가",100,200,300], ["종가",80,210,330]]

#183
stock = {
    "시가" : [100,200,300],
    "종가" : [80,210,330]
}

#184
stock = {
    "10/10" : [80,110,70,90],
    "10/11" : [210,230,190,200]
}

#185
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart :
    for j in range(2) :
        print(i[j], "호")

for i in apart :
    for j in i :
        print(j, "호")

#186
apart = [ [101, 102], [201, 202], [301, 302] ]

for i in apart[::-1] : 
    for j in i :
        print(j, "호")

#187
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1] :
    for j in i[::-1] :
        print(j, "호")

#188
apart = [ [101, 102], [201, 202], [301, 302]]
for i in apart :
    for j in i :
        print(j, "호")
        print("-"*5)

#189
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart :
    for j in i :
        print(j, "호")
    print('-'*5)

#190
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart :
    for j in i :
        print(j, "호")
print("-"*5)

#191
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for i in data :
    for j in i :
        print(j*(1+0.014/100))

#192
for i in data :
    for j in i :
        print(j*(1+0.014/100))
    print("-"*4)

#193
result = []
for i in data :
    for j in i :
        result.append(j*(1+0.014/100))
print(result)


#194
result = []
for i in data :
    temp =[]
    for j in i :
        temp.append(j*(1+0.014/100))
    result.append(temp)
print(result)


#195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc : #블로그에 올리기
    if isinstance(i[3], int): 
        print(i[3])
 
for i in ohlc[1:] :
    print(i[3])

#196
for i in ohlc[1:] :
    if i[3] > 150 :
        print(i[3])

#197
for i in ohlc[1:] :
    if i[0] <= i[3] :
        print(i[3])

#198
volatility = []
for i in ohlc[1:] :
    gap = i[1] - i[2] 
    volatility.append(gap)
print(volatility)

#199
for i in ohlc[1:] :
    if (i[3]-i[0]) > 0:
        print(i[1]-i[2])

#200
sum = 0
for i in ohlc[1:] :
    temp = i[3]-i[0]
    sum += temp
print(sum)

#201
def print_coin() :
    print("비트코인")

#202
print_coin()

#203
for i in range(100) :
    print_coin()

#204
def print_coins() :
    for i in range(100) :
        print("비트코인")

#205
# 함수를 선언(정의)하기 전에 호출했기 때문

#206
def message() :
    print("A")
    print("B")

message()
print("C")
message()
#A/B/C/A/B

#207
print("A")

def message() :
    print("B")

print("C")
message()
#A/C/B

#208
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()
#A/C/B/E/D

#209
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()
#B/A

#210
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()

#B
#C
#B
#C
#B
#C
#A