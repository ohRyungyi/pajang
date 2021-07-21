#151

list1 = [3, -20, -3, 44]
for i in list1 :
    if i < 0:
        print(i)

#152

list2 = [3, 100, 23, 44]
for i in list2 :
    if i % 3 ==0 :
        print(i)



#153

list3 = [13, 21, 12, 14, 30, 18]
for i in list3:
    if i % 3 == 0 and i <20:
        print(i)

#154

list4 = 리스트 = ["I", "study", "python", "language", "!"]
for i in list4 :
    if len(i) >=3 :
        print(i)

#155

list5 = ["A", "b", "c", "D"]
for i in list5 :
    if i.isupper() :
        print(i)

#156

list6 = ["A", "b", "c", "D"]
for i in list6 :
    if i.islower() :
        print(i)

#157

list7 = ['dog', 'cat', 'parrot']
for i in list7 :
    print(i.capitalize())

#158

list8 = ['hello.py', 'ex01.py', 'intro.hwp']
for i in list8 :
    print(i.split('.')[0])

#159

list9 =  ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in list9 :
    if i.split(".")[1] == "h" :
        print(i)
    
#160

list10 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in list10 :
    ext = i.split(".")[1]
    if ext =='h' or ext == 'c' :
        print(i)

#161

for i in range(100) :
    print(i)

#162

for i in range(2002, 2051, 4) :
    print(i)

#163

for i in range(1,31) :
    if i%3 ==0 :
        print(i)

#164

for i in range(100) :
    print(99-i)

#165

for i in range(10) :
    print(i/10)

#166

for i in range(1,10) :
    print("3x{} = {}" .format(i, 3*i))

#167

for i in range(1,10,2) :
    print("3x{} = {}" .format(i, 3*i))

#168

sum=0
for i in range(11) :
    sum = sum+i
print(sum)

#169

sum =0
for i in range(11) :
    if i%2 != 0:
        sum += i
print(sum)

#170

multi=1
for i in range(1,11) :
    multi = multi*i
print(multi)

#171

price_list = [32100, 32150, 32000, 32500]
for i in range(4) :
    print(price_list[i])

#172

for i in range(4) :
    print(i, price_list[i])

for i, data in enumerate(price_list) :
    print(i, data)
#enumerate : 몇번째 데이터인지 확인

#173

for i in range(len(price_list)):
    print((len(price_list)-1)-i, price_list[i])

#174

for i in range(1, len(price_list)) :
    print(90+i*10, price_list[i])

#175

my_list = ["가", "나", "다", "라"]
for i in range(len(my_list)-1) :
    print(my_list[i], my_list[i+1])

#176

my_list = ["가", "나", "다", "라", "마"]
for i in range(len(my_list)-2) :
    print(my_list[i], my_list[i+1], my_list[i+2])

for i in range(len(my_list)-2): 
    for j in range(i,i+3) :
        print(my_list[j], end=" ")
    print("")

#177

my_list = ["가", "나", "다", "라"]
num = len(my_list)-1
for i in range(num) :
    print(my_list[num-i], my_list[num-i-1])

#178

my_list = [100, 200, 400, 800]
for i in range(len(my_list)-1) :
    print(my_list[i+1]-my_list[i])

#179 

my_list = [100, 200, 400, 800, 1000, 1300]

for i in range(len(my_list)-2) :
    sum = 0
    for j in range(i, i+3) :
        sum = sum + my_list[j]
    print(sum/3)

#180

low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

days = len(low_prices)
volatility = []
for i in range(days) : 
    gap = high_prices[i] - low_prices[i]
    volatility.append(gap)
print(volatility)
