#41
from typing import Tuple


ticker = "btc_krw "
print(ticker.upper())
print(ticker)
#ticker 자체는 변하지 않음

#42
ticker="BTC_KRW"
print(ticker.lower())

#43
print('hello'.capitalize())

#44
file_name="보고서.xlsx"
print(file_name.endswith('xlsx'))

#45
print(file_name.endswith('xlsx' or 'xls'))
print(file_name.endswith(('xlsx','xls')))
#endswith() + ('xlsx', 'xls')

#46
file_name ='2020_보고서.xlsx'
print(file_name.startswith('2020'))

#47 
a="hello world"
a = a.split()
print(a)
#split()은 원래 변수를 변화시키는 함수는 아님
#blank가 없이 괄호만 한 경우에 공백을 기준으로 나누는 것임

#48
ticker = "btc_krw"
answer = ticker.split('_')
print(answer)

#49
date = "2020-05-01"
date = date.split("-")
print("{}년 {}월 {}일" .format(date[0], date[1], date[2]))
#formatting 할 때 백틱기호일 필요 없음

#50
data = "039490-"
print(data.rsplit())
print(data.rstrip("-"))
print(data)

#51
movie_rank = ['닥터 스트레인지' ,'스플릿', '럭키']

#52
movie_rank.append("배트맨")
print(movie_rank)

#53
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)
#inser(index, elements)

#54
movie_rank.remove('럭키')
print(movie_rank)
#del movie_rank[3]

#55
del movie_rank[2:]
print(movie_rank)
#[start : end(x) : step]

#56
lang1 = ["C","C++", "JAVA"]
lang2 = ["Python", "Go" ,"C#"]
langs = lang1 + lang2
print(langs)
#배열에서 extend 함수는 뭐지

#57
nums = [1,2,3,4,5,6,7]

print("min : " + str(min(nums)))
print("max : " + str(max(nums)))
# print("3"+3) : 자바랑 다르게 자동형변환이 안되는건가?
print("max : ", max(nums))
print("min : ", min(nums))
#와우와우 : 자료형이 다른 건 +로 연결할 수 없지만 ,로 연결할 수 있음


#58
nums = [1,2,3,4,5]
print(sum(nums))

#59
cook = ["피자", "김밥", '만두','양념치킨','족발','피자','김치만두','쫄면','쏘세지','라면','팥빙수','김치전']
print(len(cook))

#60 
nums = [1,2,3,4,5]
average = sum(nums)/len(nums)
print(average)

#61
price =['20180728','100','130','140','150','160','170']
print(price[1:])
#슬라이싱 [start : end : step]
price.pop(0)
print(price) 
#pop()이면 가장 마지막 index를 지우고, 괄호 안에 인덱스를 지정하면 그것을 지움


#62
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[::2])

#63
print(nums[1::2])

#64
nums = [1,2,3,4,5]
print(nums[::-1])
print(nums[-1::]) #이렇게 하면 5만 나옴

#65 
interest = ['삼성전자' ,'lg전자','Naver']
print(interest[::2])
print(interest[0],interest[2])

#66
interest = ['삼성전자', '엘지전자','네이버','sk하이닉스','미래에셋대우']
print(" ".join(interest))
print("".join(interest))

#67
print("/".join(interest))

#68
print("\n".join(interest))

#69
string="삼성전자/lg전자/naver" 
interest=string.split("/")
print(interest)

#70
data=[2,4,3,1,5,10,9]
print(data.sort())
print(data)
#sort는 원래 리스트 자체를 바꿈 return은 none임
data=[2,4,3,1,5,10,9]
print(sorted(data))
print(data)
#sorted는 원래 리스트를 바꾸지 않음

#71
my_variable = ()
print(type(my_variable))

#72
movie_rank = ("닥터 스트레인지" ,"스플릿" ,"럭키")
print(movie_rank, type(movie_rank))

#73
tuple_ex = (1)
print(tuple_ex, type(tuple_ex))

tuple_ex =(1,)
print(tuple_ex, type(tuple_ex))
#데이터를 하나만 저장하는 튜플의 경우 쉼표를 입력해야함

#74
#튜플은 요소 변경이 불가능하다

#75
t=1,2,3,4
print(type(t), t)
#튜플은 괄호없이도 동작합니다

#76
t=('a','b','c')
print(t[0])
#튜플은 요소를 변경할 수 없음. 다만 변수가 새로운 튜플을 가르키도록 할 수 있음
t=("A",'b','c')
print(t)

#77
interest=("삼성전자", "엘지전자" ,'sk hynix')
print(interest)
data=list(interest)
print(data)

#78
interest = ["삼성전자", 'lg전자','sk hynix']
data = tuple(interest)
print(data)

#79
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
print(a)
print(b)
print(c)

#80
data = tuple(range(2,100,2))
data2 = list(range(2,100,2))
print(data)
print(data2)

data3 = tuple(range(5))
print(data3)

