
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
