# 101 - True/False
# bool 타입

# 102 - True/False
print(3 == 5)
# False

# 103 - True/False
print(3 < 5)
# True

# 104 - True/False
x = 4
print(1 < x < 5)
# True

# 105 - True/False
print ((3 == 3) and (4 != 3))
# True and True = True
# True

# 106 - True/False
# print(3 => 4)
# 지원하는 연산자는 : < , > , == , != , <= , >= 이므로
# 지원하지 않는 연산자이기 때문

# 107 - True/False
if 4 < 3:
    print("Hello World")
# 아무것도 출력하지 않는다

# 108 - 
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")
# Hi, there.

# 109 - 
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")
# 1
# 2
# 4 출력

# 110 - 
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
# 3
# 5 출력

# 111 - input()
str = input()
print(str*2, sep='')

# 112 - input()
n = input('숫자를 입력하세요: ')
result = int(n)+10
print(result)

# 113 - input() & if
n = int(input())
result = '짝수' if (n%2==0) else '홀수'
print(result)

# 114 - input() & if & print
n = int(input('입력값: '))
result = 255 if (n+20>255) else n+20
print('출력값:', result)

# 115 - input()
n = int(input('입력값: '))
result = (255) if (n-20 >255) else ( (0) if (n-20<0) else (n-20) )
print('출력값:', end=' ')
if n-20>255 :
    print(255)
elif n-20<0:
    print(0)
else:
    print(n-20)

# 116 - 
s = input('현재시간:')
hour, min = s.split(':')
if int(min) ==0:
    print('정각 입니다.')
else:
    print('정각이 아닙니다.')

# 117 - in
# item in list : list 안에 item이 있으면 True, 아니면 False
fruit = ["사과", "포도", "홍시"]
item = input('좋아하는 과일은? ')
if item in fruit:
    print('정답입니다.')
else:
    print('오답입니다.')

# 118 - 
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
item = input()
if item in warn_investment_list:
    print('투자 경고 종목입니다.')
else:
    print('투자 경고 종목이 아닙니다.')

# 119 - 
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
item = input('제가좋아하는계절은: ')
if item in fruit.keys():
    print('정답입니다.')
else:
    print('오답입니다.')

# 120 - 
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
item = input('좋아하는과일은? ')
if item in fruit.values():
    print('정답입니다.')
else:
    print('오답입니다.')

# 121 - islower, upper, lower
# islower() : 해당 문자가 소문자인지 판별
n = input()
if n.islower():
    print(n.upper())
else:
    print(n.lower())

# 122 - 
score = int(input('score: '))
if score>=81:
    grade = 'A'
elif score>=61:
    grade = 'B'
elif score>=41:
    grade = 'C'
elif score>=21:
    grade = 'D'
else:
    grade = 'E'
print('grade is ', grade)

# 123 - 
val = {
    '달러' : 1167,
    '엔' : 1.096,
    '유로' : 1268,
    '위안' : 171
}
cost, data = input('입력: ').split()
cost = int(cost)
print(format(cost*val[data], '.2f'), '원')

# 124 - 
num = []
for i in range(1, 4):
    n = input('input number%d: ' %i)
    num.append(int(n))
print(max(num))

# 125 - 
call = {
    '011':'SKT',
    '016': 'KT',
    '019': 'LGU',
    '010': '알수없음'
}
number = input('휴대전화 번호 입력: ').split('-')
print(f'당신은 {call[number[0]]} 사용자입니다.')

# 126 - 
dong = {
    int(0): '강북구',
    int(1): '강북구',
    int(2): '강북구',
    int(3): '도봉구',
    int(4): '도봉구',
    int(5): '도봉구',
    int(6): '노원구',
    int(7): '노원구',
    int(8): '노원구',
    int(9): '노원구',
}
num = input('우편번호: ')
print(dong[int(num[2])])

# 답지
num = input('우편번호: ')
num = num[:3]
if num in ['010', '011', '012']:
    print('강북구')
elif num in ['013', '014', '015']:
    print('도봉구')
else:
    print('노원구')

# 127 - 
num = input('주민등록번호: ').split('-')
if int(num[1][0]) in [1, 3]:
    print('남자')
else:
    print('여자')

128 - 
num = input('주민등록번호: ').split('-')
result = int(num[1][1:3])
if result<=8 :
    print('서울 입니다.')
else:
    print('서울이 아닙다.')

# 129 - 
# range(n, m) : n, n+1, n+2, ... , m-1 출력
num = input('주민등록번호: ').split('-')
arr =[]
for i in num:
    for j in i:
        arr.append(int(j))
index=1
sum = 0
for i in range(1, 13, 1):
    index = index+1 if index<9 else 2
    sum+=index*arr[i-1]
div = sum%11
if arr[-1] == 11-div:
    print('유효한 주민등록번호입니다.')
else:
    print('유효하지 않은 주민등록번호입니다.')

# 130 - 
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
change = float(btc['closing_price']) - flot(btc['opening_price'])
if float(btc['opening_price']) > float(btc['max_price']):
    print('상승장')
else:
    print('하락장')