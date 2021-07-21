#131
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)

#132
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
  print("#####")

#133
for 변수 in ["A", "B", "C"]:
  print(변수)

변수 = "A"
print('변수')
변수 = "B"
print('변수')
변수 = "C"
print('변수')

#134
for 변수 in ["A", "B", "C"]:
  print("출력:", 변수)

변수 = "A"
print("출력:", 변수)
변수 = "B"
print("출력:", 변수)
변수 = "C"
print("출력:", 변수)

#135
for 변수 in ["A", "B", "C"]:
    b = 변수.lower()
    print("변환:", b)

변수 = "A"
b=변수.lower()
print ("변환 : ", b)

변수 = "B"
b=변수.lower()
print ("변환 : ", b)

변수 = "C"
b=변수.lower()
print ("변환 : ", b)

#136
for 변수 in (10,20,30) :
    print(변수) 
#리스트, 튜플 다 돌아감

#137
for i in [10,20,30] :
    print(i)

#138
for i in [10,20,30] :
    print(i)
    print("-"*6)

#139
print("+"*4)
for i in [10,20,30] :
    print(i)

#140
for i in range(4) :
    print("-"*6)

#141
리스트 = [100, 200, 300]
for i in 리스트 :
    print(i+10)

#142
리스트 = ["김밥", "라면", "튀김"]
for i in 리스트 :
    print("오늘의 메뉴 : {}" .format(i))

#143
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
for i in 리스트 :
    print(len(i))

#144
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트 :
    print(i, len(i))

#145
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트 :
    print(i[0])

#146
리스트 = [1, 2, 3]
for i in 리스트 :
    print("3 x {}" .format(i))

#147
리스트 = [1, 2, 3]
for i in 리스트 :
    print("3 x {} = {} " .format(i, 3*i))

#148
리스트 = ["가", "나", "다", "라"]
for i in range(1, len(리스트)) :
    print(리스트[i])
#scope이 문제 되는건 밖에서 안을 사용하려고 할 떄인건가? for안에서 했던 일들이 밖에서도 그대로 기억됨

#149
리스트 = ["가", "나", "다", "라"]
for i in range(0,4,2) :
    print(리스트[i])

for i in 리스트[::2] :
    print (i)
    
#150
리스트 = ["가", "나", "다", "라"]
for i in 리스트[::-1] :
    print(i)


