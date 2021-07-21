
# 1
print('Hello World')

# 2
print("Mary's cosmetics")
print('Mars\'s cosmetics')

# 3
print('신씨가 소리질렀다. "도둑이야".')

# 4
print('C:\Windows')

# 5
print("안녕하세요.\n 만나서\t\t반갑습니다.")
# \n : 줄바꿈
# \t : tap 키

# 6
print("오늘은", "일요일")
# ,와 +의 차이점

# 7
print("naver", "kakao", "samsung", sep=";")
# ,와 sep =" "

# 8
print('naver', 'kakao', 'sk', 'samsung', sep="/")

# 9
print('first', end="\n")
print('second')
# sep과 end의 차이
# sep을 사용하지 않으면 sep=" "와 동일
# end를 사용하지 않으면 end="\n"과 동일

# 10
print(5/3)

# 11
삼성전자 = 50000
총평가금액 = 삼성전자*10
print(총평가금액)
# 바인딩 : 변수가 값을 가리키게 하는 것

# 12
시가총액 = 298*(10**12)
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))
# type(변수명)

# 13
s = "hello"
t = "python"
print(s, t, sep="! ")
print(s+"! "+t)
print(s+"!", t)
# 문자열을 +로 연결하느냐 ,로 연결하느냐

# 14
print(2+2*3)  # 8

# 15
a = 128
print(type(a))  # int
a = "132"
print(type(a))  # str

# 16
num_str = "720"
print(int(num_str))
num_int = int(num_str)
print(num_int)

# 17
num = 100
str = str(num)
print(str, type(str))

# 18
str = "15.79"
float = float(str)
print(float, type(float))

# 19
year = "2020"
year = int(year)
print(year-2, year-1, year)

# 20
price_per_month = 48584
month = 36
gross_price = price_per_month * month
print(gross_price)

# 21
letters = "python"
print(letters[0], letters[2])
# 문자열도 리스트처럼!

# 22
license_plate = "24가 2210"
print(license_plate[-4:])
# [first : last(포함x) : step]

# 23
string = "홀짝홀짝홀"
print(string[::2])

# 24
string = "PYTHON"
print(string[::-1])
# 역으로 출력하기 !!!

# 25
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)
# replace(원래, 나중) 메서드!!

# 26
phone_number2 = phone_number.replace("-", "")
print(phone_number2)

# 27
url = "http://sharebook.kr"
print(url[-2:])
url_split = url.split('.')
print(url_split[-1])
# split(기준) -> 기준으로 나눠서 배열형태로 저장

# 28
# lang = 'python'
# lang[0] = 'P'
# print(lang)
# 문자열은 수정할 수 없음(immutable)

arr = [0, 1, 2]
arr[0] = 'p'
print(arr)
# 배열은 수정할 수 있음

# 29
string = 'abcdef2a354a32a'
string1 = string.replace('a', 'A')
print(string1)
# replace의 경우 원래 변수를 바꾸지 않음

# 30
string = 'abcd'
string.replace('b', "B")
print(string)  # abcd
# 문자열은 변경할 수 없는 자료형이기 때문에 replace 메서드를 사용하면 원본은 그대로 둔 채 새로운 문자열 객체를 리턴해줌

# 31
a = '3'
b = '4'
print(a+b)  # 34

# 32
print('hi'*3)  # hihihi

# 33
print('-'*80)

# 34
t1 = 'python'
t2 = 'java'
print((t1+' ' + t2+' ')*4)

# 35
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13

print("이름 : %s 나이 : %d" % (name1, age1))
print("이름 : %s 나이 : %d" % (name2, age2))
print("%s" % name2)

# 36
print("이름 : {} 나이 : {}" .format(name1, age1))
print("이름 : {} 나이 : {}" .format(name2, age2))

# 37
print(f"이름 : {name1} 나이 : {age1}")
print(f"이름 : {name2} 나이 : {age2}")

# 38
상장주식수 = "5,969,782,550"
상장주식수 = 상장주식수.replace(',', '')
num = int(상장주식수)
print(num, type(num))

# 39
분기 = "2020/03(E) (IFRS연결)"
print(분기[0:7])
print(분기[:7])

# 40
data = "    삼성전자    "
data1 = data.replace('  ', '')
print(data1)
data2 = data.strip()  # strip메서드는 공백 제거
print(data2)

exam = '123454321'
exam1 = exam.strip('1')  # strip으로 모든 '1'제거
print(exam1)
exam2 = exam.replace('1', '0')  # replace로 모든 '1'을 '0'으로 대체
print(exam2)
