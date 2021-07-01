# -*- coding: utf-8 -*-

# 001 
print('Hello World')

# 002
print("Mary's cosmetics")

# 003
print('신씨가 소리질렀다. "도둑이야"')

# 004
print("C:\Windows")

# 005
# \n : 한 줄 엔터 = 줄 바꿈
# \t : 탭 키 입력 = 탭

# 006
print("오늘은", "일요일")
# 오늘은 일요일 , 여러 문자열을 , 로 구분하는 경우 두 문자열 사이에 뛰여쓰기를 적용하여 출력한다.

# 007
print("naver", "kakao","sk", "samsung", sep=';')

# 008
print("naver", "kakao", "sk", "samsung", sep='/')

# 009
print("first", end='');print("second")

# 010
print(5/3)
# 1.6666666666 ...

# 011
삼성전자 = 50000
print(int(삼성전자)*10)

# 답지
# 삼성전자 = 5000
# 총평가금액 = 삼성전자 * 10
# print(총평가금액)

# 012
시가총액 = 298000000000000
현재가 = 5000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

# 013
s="hello"
t="python"
print(s, t, sep='! ')

# 014
print(2+2*3)
# 8

# 015
# type() : 데이터 타입 판별
# a = 132
# print(type(a)) 
# <class 'int'>
a="132"
print(type(a))
# <class 'str'>

# 016
# int(n) : n을 정수로 변환
num_str = "720"
print(int(num_str))

# 017
# str(n) : n을 문자열로 변환
num = 100
n_str = str(num);
print(n_str, type(n_str))

# 018
# float(n) : n을 실수로 변환
str = "15.79"
f_str = float(str)
print(f_str, type(f_str))

# 019
year = "2020"
n_year = int(year)
print(n_year-1, n_year, n_year+1, sep="\n")

# 020
money = 48584
n_year = 36
print(money*n_year)

# 021 - 문자열 인덱싱
letters = 'python'
print(letters[0], letters[2])

# 022 - 문자열 슬라이싱
# 문자열의 시작 인덱스를 생략하면 0으로 간주, 끝 인덱스를 생략하면 문자열 끝을 의미
license_plate = "24가 2210"
print(license_plate[-4 : ])

# 023 - 문자열 인덱싱
string = "홀짝홀짝홀짝"
print(string[0], string[2], string[4], sep='')
# 답지
# print(string[::2])
# arr[ 시작인덱스 : 끝인덱스 : 오프셋 ]

# 024 - 문자열 슬라이싱
string = "PYTHON"
print(string[::-1])

# 025 - 문자열 치환
# replace('바꿀 문자', '바뀔 문자') : 문자열 일부를 치환
phone_number = "010-1111-2222"
arr = phone_number.split('-')
print(arr[0], arr[1], arr[2])
arr = phone_number.replace('-', ' ')
print(arr)

# 026 - 문자열 다루기
arr = phone_number.replace('-', '')
print(arr)

# 027 - 문자열 다루기
url = "http://sharebook.kr"
arr = url.split('.')
print(arr[1])
# 답지
# print(arr[-1])

# 028 - 문자열은 immutable
lang = 'python'
#lang[0] = 'P' # error
print(lang) # error
# 문자열은 변경할 수 없다

# 029 - replace 메소드
string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)

# 030 - replace 메소드
string = 'abcd'
string.replace('b', 'B')
print(string) # abcd
# n.replace() 의 리턴값이 변화된 값이기 때문에 기존의 문자열에는 영향을 미치지 않는다

# 031 - 문자열 합치기
a = "3"
b = "4"
print(a+b) # 34

# 032 - 문자열 곱하기
print("Hi"*3) # HiHiHi

# 033 - 문자열 곱하기
print('-'*80)

# 034 - 문자열 곱하기
t1 = 'python'
t2 = 'java'
print((t1 + ' '+t2+ ' ')*4)

# 035 - 문자열 출력
# %s : 문자열 데이터 타입 값
# %d : 정수 데이터 타입 값
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print('이름 : %s 나이 : %d \n'*2 %(name1, age1, name2, age2), end='')

# 036 - 문자열 출력
# ??

# 'data : {}'.format(n) : data : n 의 형태가 출력
print('이름 : {} 나이 : {}'.format(name1, age1))
print('이름 : {} 나이 : {}'.format(name2, age2))

# 037 - 문자열 출력
# f-string : 문자열 앞에 f가 붙은 형태
# data = 3
# f"data : {data}"" = "data : 3"
print(f"이름 : {name1} 나이 : {age1}")
print(f"이름 : {name2} 나이 : {age2}")

# 038 - 컴마 제거하기
# 문자열 변화와 타입변환은 동시에 이루어지지 않는다
# 문자열 변환을 ㅁ너저 진행한 후 타입변환을 진행해야 한다.
상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(',', '')
타입변환 = int(컴마제거)
print(타입변환)

# 039 - 문자 슬라이싱
분기 = "2020/03(E) (IFRS연결)"
분기 = 분기.split('(')
print(분기[0])

# 답지
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 040 - strip 메소드
# strip() : 문자열 좌우 공백 제거, 공백이 제거된 문자열이 반환
data = "   삼성전자    "
data = data.strip()
print(data)
# 원본 문자열은 그대로 유지되고 공백에 제거된 문자열만 반환
data = "   삼성전자    "
data1 = data.strip()
print(data, data1, sep='\n')

# 041 - upper 메소드
# upper() : 소문자를 대문자로 변환한 문자열이 반환되고 원본 문자열은 유지된다.
ticker = "btc_krw"
print(ticker.upper())

# 042 - lower 메소드
# lower() : 대문자를 소문자로 변환한 문자열이 반환되고 원본 문자열은 유지된다
ticker = "BTC_KRW"
print(ticker.lower())

ticker = "BTC_KRW"
ticker1 = ticker.lower()
print(ticker1, ticker, sep='\n')