#81
from typing import SupportsComplex


a,b,*c=(0,1,2,3,4,5)
print(a)
print(c)

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = scores
print("valid_score" , valid_score)
print("first : ", _)
print(_)
#변수 _ 는 결국 1개만 저장 가능한거지?
#*는 제일 마지막에 할 필요 없다 앞에서 해도 됨
scores = scores[::-1]
a,b,*c = scores
print(a)
print(b)
print(c)

#82
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

_,_,*valid_score = scores 
print(valid_score)
#*는 남은 것들이 다 나오는 거임 , 1번만 사용가능함

#83
_,*valid_score,_ = scores
print(valid_score)

#84
temp = {}
print(type(temp))

#85
icecream = {
    "메로나" : 1000,
    "폴라포" : 1200,
    "빵빠레" : 1800,
}
print(icecream,type(icecream))

#86
icecream["조스바"] = 1200
icecream["월드콘"] = 1200

print(icecream)

#87
print("메로나 가격 :", icecream["메로나"])

#88
icecream["메로나"] =1300
print(icecream)

#89
del icecream["메로나"]
print(icecream)

# icecream.pop('메로나')
# print(icecream)

#90
# "딕셔너리에 없는 키를 인덱싱"

#121
# print("a".islower()) 함수가 실행하는 과정에서 print가 있는게 아니면 실행하는 단계 단계를 볼 수 없음 return은 함수실행을 print해야함

user_input = input()
if user_input.islower() :
    print(user_input.upper())
else :
    print(user_input.lower()) 

#input()랑 input("")가 차이가 있나?

#122
user_input=int(input("score : "))
score = "E"
if (81 <= user_input and user_input <=100) :
    score = "A"
elif (61 <= user_input and user_input <=80) :
    score ="B"
elif (41<= user_input and user_input <=60) :
    score ="C"
elif (21 <= user_input and user_input <=40):
    score = "D"
print("greade is {}" .format(score))

#123
user_input=input("입력 : ")
user_input=user_input.split(" ")
before_money = int( user_input[0])
before_unit = user_input[1]

if before_unit == "달러":
    after_money = 1167 * before_money
elif before_unit == "엔" :
    after_money = 1.096 * before_money
elif before_unit == "유로" :
    after_money = 1268 * before_money
else :
    after_money = 171 * before_money

print(after_money)

#key, value로 연결할 수 있으면 dict형태로 나타낼 것
환율 = {"달러": 1167, 
        "엔": 1.096, 
        "유로": 1268, 
        "위안": 171}
user = input("입력: ")
num, currency = user.split() #리스트도 별도로 뺄 수 있다
print(float(num) * 환율[currency], "원")

#124
nums = [] 
num1 = int(input("input number 1 : "))
num2 = int(input("input number 2 : "))
num3 = int(input("input number 3 : "))
nums.append(num1)
nums.append(num2)
nums.append(num3)
print (max(nums))

#125
phone = {
    "011" : "skt",
    "016" : "kt",
    "019" : 'lgu',
    "010" : "알수없음"
}

user_input = input("휴대전화 번호를 입력 : ")
user_input = user_input.split('-')
print("당신은 {} 사용자입니다." .format(phone[user_input[0]]))

#126
address = {
    0 : "강북구",
    1 : "강북구",
    2 : "강북구",
    3 : "도봉구",
    4 : "도봉구",
    5 : "도봉구",
    6 : "노원구",
    7 : "노원구",
    8 : "노원구",
    9 : "노원구",
}

user_input = input ("우편변호 : ")
user_input = int(user_input[2:3])
print (address[user_input])

#127
user_input = input("주민등록번호 : ")
user_input = user_input.split('-')
gender = int(user_input[1][0])
if gender ==1 or gender==3 :
    print ("남자")
else :
    print("여자")

#128
user_input = input("주민등록번호 : ")
user_input = user_input.split('-')
city = int(user_input[1][1:3])
if 0<= city and city <= 8 :
    print ("서울입니다")
else :
    print ("서울이 아닙니다")

#129
user_input = input("주민등록번호 : ")
user_input = user_input.split('-')

#변수 Scope이 어떻게 되지
sum = 0
for i in range(0,6) :
    sum += int(user_input[0][i]) * (i+2)

sum = sum + int(user_input[1][0])*8 + int(user_input[1][1])*9

for i in range(2,6) :
    sum += int(user_input[1][i])*i

valid = 11-(sum%11)

if int(user_input[1][-1]) != valid :
    print("유효하지 않은 주민등록번호입니다")
else :
    print("유효한 주민등록번호 입니다")

#130



    