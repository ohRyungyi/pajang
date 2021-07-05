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