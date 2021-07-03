#91
inventory={
    "메로나" : [300,20],
    "비비빅" : [400,3],
    "죠스바" : [250,100],
}
print(inventory)
#튜플이 아니라 리스트로 하는 이유는 변경을 위해서?

#92
print(inventory.keys()) #key값을 다 보여줌
print(inventory.values()) #value값을 다 보여줌
print(inventory["메로나"])
print(inventory["메로나"][0], "원")

#93
print(inventory["메로나"][1], "개")

#94
inventory["월드콘"] = [500,7]
print(inventory)

#95
icecream={
    "탱크보이" : 1200,
    "폴라포" : 1200,
    "빵빠레" : 1800,
    "월드콘" : 1500,
    "메로나" : 1000,
}
keyofice = icecream.keys()
print(keyofice)

#96
valueofice = icecream.values()
print(valueofice)

#97
print(sum(valueofice))
#키값이나 벨류 값 찾으면 리스트 형태로 주어짐

#98
new_product={
    "팥빙수" : 2700,
    "아맛나" : 1000,
}
icecream_update = icecream.update(new_product)
print(icecream_update) #none으로 나옴
print(icecream) #원래 변수 자체가 바뀜

#99
keys=("apple","pear","peach")
vals =(300,250,400)
print(list(zip(keys,vals)))
result = dict(zip(keys,vals))
print(result)

#100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date,close_price))
print(close_table)

#remember
date_tuple = tuple(date)
print(date_tuple)
keys_list=list(keys)
print(keys_list)

#summary
print("딕셔너리 : ", dict(zip('abc','123')))
print("리스트 : ", list(zip('abc','123','가나다')))
print("튜플 : ", tuple(zip('abc','123','가나다')))

#101
#bool

#102
print(3==5) # :False

#103
print(3<5) #True

#104
x=5
print(1<x<5) #True

#105
print((3==3) and (4!=3)) #True

#106
print(3>=4) #항상 부등호가 등호보다 먼저

#107
if 4<3 :
    print("hello world")
    #어떠한 것도 출력되지 않음

#108
if 4<3 : 
    print("hello world")
else : #여기가 실행됨
    print("hi, there")
    
#109
if True :
    print('1')
    print('2')
else : 
    print('3')
print('4')
#1/2/4

#110
if True :
    if False :
        print('1')
        print('2')
    else :
        print('3')
else :
    print('4')
print('5')
#3,5

#111
user_input = input()
print(user_input*2)

#112
user_input=input("숫자를 입력하세요 : ")
print(int(user_input)+10)

#113
user_input=int(input())
if user_input%2==0 : 
    print("짝수")
else :
    print("홀수")

#114
user_input=int(input())
number=20+user_input
standard = 255
if number > standard :
    print(standard)
else :
    print(number)

#115
user_input=int(input())
number =user_input-20
if number < 0 : 
    print(0)
elif number >standard:
    print(standard)
else :
    print(number)

#116
user_input=input("현재시간 : ")
min = user_input[-2:]
if int(min)==0 : 
    print("정각 입니다")
else :
    print("정각이 아닙니다")
#파이썬은 문자열도 ==으로 해결 가능 equals(자바

#117
fruit = ["사과", "포도", "홍시"]
#print('사과' in fruit)
user_input = input("좋아하는 과일은?")
if (user_input in fruit) :
    print("정답입니다.")
else :
    print("오답입니다")

#118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
user_input = input()
if user_input in warn_investment_list :
    print("투자 경고 종목입니다")
else :
    print("투자 경고 종목이 아닙니다")

#119
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
print(fruit.keys()) #리스트 형태로 주어짐
fruit_keys = fruit.keys()
user_input = input("제가 좋아하는 계절은 : ")
if user_input in fruit_keys :
    print('정답입니다')
else :
    print("오답입니다")

#120
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
fruit_values = fruit.values()
user_input = input("제가 좋아하는 과일은 : ")
if user_input in fruit_values :
    print("정답입니다")
else :
    print("오답입니다")
