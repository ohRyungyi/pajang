#211
def 함수(문자열) :
    print(문자열)

함수("안녕")
함수("Hi")
#안녕/Hi

#212
def 함수(a, b) :
    print(a + b)

함수(3, 4)
함수(7, 8)

#213
def 함수(문자열) :
    print(문자열)
#함수() => 인수를 넣지 않아서

#214
def 함수(a, b) :
    print(a + b)

# 함수("안녕", 3)
#문자열과 정수를 더할 수 없음

#215
def print_with_smile(a) :
    print(a, end=":D")

#216
print_with_smile("안녕하세요")

#217
def print_upper_price() :
    price = input()
    print(1.3*str(price))
def price_upper_price(price) :
    print(price*1.3)

#218
def print_sum(a,b) :
    print(a+b)

#219
def print_arithmetic_operation(a,b) :
    print("{} + {} = {}" .format(a, b, a+b))
    print("{} - {} = {}" .format(a, b, a-b))
    print("{} * {} = {}" .format(a, b, a*b))
    print("{} / {} = {}" .format(a, b, a/b))

#220
def print_max(a,b,c) :
    if (a>b) :
        if (a>c) :
            print(a)
        else :
            print(c)
    else :
        if (b>c) :
            print(b)
        else : 
            print(c)

def print_max(a,b,c) :
    max_val = 0
    if a >max_val:
        max_val = a
    if b>max_val :
        max_val=b
    if c > max_val :
        max_val=c
    print(max_val)

#221
def print_reverse(a) :
    print(a[::-1])

print_reverse("Python")

#222
def print_score(a) :
    print(sum(a)/len(a))

#223
def print_even(a) :
    for i in a :
        if i %2 ==0 :
            print(i)

#224
def print_keys(a) :
    for i in a.keys() :
        print(i)

#225
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
def print_value_by_key(dict, date) :
    print(dict[date])
print_value_by_key  (my_dict, "10/26")

#226
def prit_5xn(string) :
    num = int(len(string)/5)
    for i in range(num+1) :
        print(string[i*5:i*5+5])

#227
def printmxn(string, inline) :
    num = int(len(string)/inline)  #입력한 문자열을 원하는 수로 나눈 몫 inline만큼 꽉 채워서 나오는 줄의 수
    for i in range(num+1): #0,1,2,3
        print(string[i*inline:i*inline+inline]) #0,1,2/3,4,5/6,7,8/9,10,11 -> 범위 초과하면 그냥 끝까지 출력
printmxn("아이엠어보이유알어걸", 3)

#228
import math
def calc_monthly_salary(annual_salary) :
    return math.floor(annual_salary/12)

#int만해줘도 됨

#229
#230

#231
def n_plus_1 (n) :
    result = n + 1

n_plus_1(3) #print가 없으니까 별도로 보여지는 것 없음/ 함수자체를 프린트해도 None임
#print (result) #함수밖에서 함수 안의 변수에 접근할 수 없음

#232
def make_url(url) :
    return ("www.{}.com". format(url))
print(make_url("ccc"))
#return에도 format사용가능

#233
def make_list(a) :
    a_list = []
    for i in range(len(a)) :
        a_list.append(a[i])
    return a_list

print(make_list("abcd"))

def make_list2(a) :
    return list(a)
print(make_list2("absc"))

#234
def pickup_even(a) :
    even_list = []
    for i in a :
        if i % 2 ==0 :
            even_list.append(i)
    return even_list

print(pickup_even([3, 4, 5, 6, 7, 8]))

#235
def convert_int(string) :
    return string.replace(",","")
#replace()가 색칠되지 않아서 당황했다, Parameter가 뭔지모르니까 색칠이 안 되는 건가
print(convert_int("1,234,568"))

#236
def 함수(num) :
    return num + 4

a = 함수(10) #14
b = 함수(a) #18
c = 함수(b) #22
print(c)

#237
def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c)

#238
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10) #14
c = 함수2(a) #140
print(c)

#239
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2 #12
    return 함수1(num) #16

c = 함수2(10) 
print(c)

#240
def 함수0(num) : #14
    return num * 2  #28

def 함수1(num) : #12
    return 함수0(num + 2) #28

def 함수2(num) :
    num = num + 10 #12
    return 함수1(num) #28

c = 함수2(2)
print(c) #28