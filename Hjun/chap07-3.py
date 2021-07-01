# 121
#c = input("")
#if c.islower() == True:
#    print(c.upper())
#else:
#    print(c)

# 122
#grade = int(input())
#if 81 <= grade <= 100:
#    print('A')
#elif 61 <= grade <= 80:
#    print('B')
#elif 41 <= grade <= 60:
#    print('C')
#elif 21 <= grade <= 40:
#    print('D')
#elif 0 <= grade <= 20:
#    print('E')
#else:
#    print('error')

# 123
#환율 = {"달러": 1167, 
#        "엔": 1.096, 
#        "유로": 1268, 
#        "위안": 171}
#user = input("입력: ")
#num, currency = user.split()
#print(float(num) * 환율[currency], "원")

# 124
#n1 = int(input("input number1: "))
#n2 = int(input("input number2: "))
#n3 = int(input("input number3: "))
#if n1 > n2:
#    if n1 > n3:
#        print(n1)
#    else:
#        print(n3)
#else:
#    if n2> n3:
#        print(n2)
#    else:
#        print(n3)

# 125
#a,b,c = input().split('-')
#if a == '011':
#    print('SKT')
#elif a == '016':
#    print('KT')
#elif a == '019':
#    print('LGU')
#else:
#    print('알수없음')

#126
#우편번호 = input("우편번호: ")
#우편번호 = 우편번호[:3]
#if 우편번호 in ["010", "011", "012"]:
#    print("강북구")
#elif 우편번호 in ["014", "015", "016"]:
#    print("도봉구")
#else:
#    print("노원구")

# 127
#a = input("주민등록번호: ")
#a_split = a.split('-')[1]
#if a_split[0] == '1' or a_split[0] == '3':
#    print('남자')
#else:
#    print('여자')

# 128
#c = input()
#c_split = c.split('-')[1]
#if 0< int(c_split) <8:
#    print('서울입니다.') 
#else:
#    print('서울이 아닙니다.')

# 129
#num = input("주민등록번호: ")
#계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
#        int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10])* 3 + \
#        int(num[11])* 4 + int(num[12]) * 5
#계산2 = 11 - (계산1 % 11)
#계산3 = str(계산2)

#if num[-1] == 계산3[-1]:
#    print("유효한 주민등록번호입니다.")
#else:
#    print("유효하지 않은 주민등록번호입니다.")

# 130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")

# 후기
# 귀찮은 문제가 많아졌다.
# 분기문이 쉽다한건 취소한다.
# 생각을해야하는 문제가 나오니 졸려진다..