# 201 - 
def print_coin():
    print("비트코인")

# 202 - 
print_coin()

# 203 -
for i in range(100):
    print_coin()

# 204 -
def print_coins():
    for i in range(100):
        print('비트코인')

205 - 
함수가 정의되기도 전에 함수를 선언해서 에러가 발생하였습니다.

# 206 - 
def message() :
    print("A")
    print("B")

message()
print("C")
message()

A
B
C
A
B
출력

# 207 -
print("A")

def message() :
    print("B")

print("C")
message()

A
C
B
출력

# 208 -
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()

A
C
B
E
D
출력

# 209 - 
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()

B
A
출력

# 210 - 
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

B
C
B
C
B
C
A
출력

# 211 - 
def 함수(문자열) :
    print(문자열)

함수("안녕")
함수("Hi")

안녕
Hi
출력

# 212 - 
def 함수(a, b) :
    print(a + b)

함수(3, 4)
함수(7, 8)

7
15
출력

# 213 - 
def 함수(문자열) :
    print(문자열)
함수()

# 이때의 문제는 함수의 경우 매개변수가 1개 존재하지만 호출할 때는 매개변수가 없어서 발생하는 에러입니다.

# 214 - 
def 함수(a, b) :
    print(a + b)

함수("안녕", 3)

# 문자열과 정수끼리는 더할 수 없다. 타입에러가 발생하였다.

# 215 - 
def print_with_smile(string):
    print(string+':D')

# 216 - 
print_with_smile('안녕하세요')

# 217 - 
def print_upper_price(price):
    print(price*(1+0.3))

# 218 - 
def print_sum(a, b):
    print(a+b)

# 219 - 
def print_arithmetic_operation(a, b):
    print('%d + %d  = %d' %(a, b, a+b))
    print('%d - %d  = %d' %(a, b, a-b))
    print('%d * %d  = %d' %(a, b, a*b))
    print('%d / %d  = %.2f' %(a, b, a/b))

# 220 -
def print_max(a, b, c):
    if (a>b):
        if a>c:
            print(a)
        else:
            print(c)
    else:
        if (b>c):
            print(b)
        else:
            print(c)

# 221 - 
def print_reverse(string):
    for i in string[::-1]:
        print(i, end='')
    # # 답지 풀이
    # print(string[::-1])

# 222 - 
def print_score(list):
    print(sum(list)/len(list))

# 223 - 
def print_even(list):
    for i in list:
        if i%2==0:
            print(i)

# 224 - 
def print_keys(dict):
    for i in dict.keys():
        print(i)

# 225 - 
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}

def print_value_by_key(map, date):
    print(map[date])

# 226 -
def print_5xn(string):
    repeat = int(len(string)/5 )
    if len(string)%5 !=0:
        repeat+=1
    
    start = 0
    for i in range(repeat):
        print(string[start:start+5])
        start +=5

# 227 -
def print_mxn(string, m ):
    repeat = int(len(string)/m )
    if len(string)%m !=0:
        repeat+=1
    
    start = 0
    for i in range(repeat):
        print(string[start:start+m])
        start +=m

# 228 -
def calc_monthly_salary(salary):
    print(int(salary/12))

# 229 -
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)

# 왼쪽: 100
# 오른쪽: 200
# 출력

# 230 -
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)

# 왼쪽: 200
# 오른쪽 : 100
# 출력

# 231 - 
def n_plus_1 (n) :
    result = n + 1

n_plus_1(3)
print (result)

# 에러가 발생한다. result 라는 변수를 선언하기도 전에 호출하였기 때문이다.

# 232 - 
def make_url(domain):
    return 'www.'+domain+'.com'
print(make_url('naver'))

# 233 - 
def make_list(string):
    ans = []
    for i in string:
        ans.append(i)
    return ans

print(make_list("abcd"))

# 234 - 
def pickup_even(list):
    even = []
    for i in list:
        if i%2==0:
            even.append(i)
    return even

print(pickup_even([3, 4, 5, 6, 7, 8]))

# 235 - 
def convert_int(value):
    vals = value.split(',')
    val = ''
    for i in vals:
        val+=i
    return int(val)

print(convert_int("1,234,567"))

# 236 -
def 함수(num) :
    return num + 4

a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)

# a = 14
# b = 18
# c = 22
# 이므로 22가 출력

# 237 -
def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)

# 10 -> 14 -> 18 -> 22이므로 
# 22가 출력

# 238 -
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10)
c = 함수2(a)
print(c)

# a = 14
# c = 140 이므로
# 140 출력


# 239 -
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)

# 함수 2의 num의 값이 12로 바인딩되므로 함수2(10)의 리턴값은 16이 된다.
# 16 출력

# 240 -
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)

# 함수2(2) 내부의 지역변수인 num의 값이 12로 바인딩되므로 함수1(12)의 리턴값이자 함수0(14)의 리턴값은 28이 된다.
# 28 출력

# 241 - 
import datetime

now = datetime.datetime.now()
print(now)

# 242 - 
import datetime
now = datetime.datetime.now()
print(type(now))
# # 답지 풀이
# print(now, type(now))

# 243 - 
import datetime
now  = datetime.datetime.now()
for i in range(5, 0, -1):
    day = datetime.timedelta(days = i)
    date = now - day
    print(date)

244 - 
datetime.datetime.now().strfime(형식) : 현재 시간을 인자로 제공하는 형식에 맞춰서 출력
import datetime
now = datetime.datetime.now()
print(now.strftime('%H:%m:%S'))

# 245 - 
import datetime
timeStr = "2020-05-04"
timeVal = datetime.datetime.strptime(timeStr, '%Y-%m-%d')
print(timeVal, type(timeVal))

# 246 -
import datetime, time
while True:
    now  = datetime.datetime.now()
    print(now)
    time.sleep(1)

# # 247 - 모듈 임포트 방법
# 예를 들어서 modi.py 파일 내에 add, sub, multi, division 이라는 함수가 정의된 모듈이 정의되어 있다.
# 1. import 모듈이름
# 예) import modi # 주의 mody.py 라고 하지 않도록 주의한다.
# 2. from 모듈이름 import 모듈함수
# 예) from modi import add
# 3. from 모듈이름 import 모듈함수1, 모듈함수2
# 예) from mody import add, sub
# 4. from 모듈이름 import * 
# 모듈 내의 모든 함수를 호출한다.

# 248 -
import os
print(os.getcwd())

# 249 -
import os
os.rename('/Users/yelimoh/Desktop/test.txt', '/Users/yelimoh/Desktop/changeFileName.txt')

# 250 - 
import numpy
for i in numpy.arange(1.0, 5.0, 1.0):
    print(i)