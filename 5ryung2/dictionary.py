# 081 - 별 표현식
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = list(scores)
print(valid_score)

# 082 - 별 표현식
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, _, *valid_score = list(scores)
print(valid_score)

# 083 - 별 표현식
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, *valid_score, _ = list(scores)
print(valid_score)

# 084 - 딕셔너리 생성
temp = {}
print(temp, type(temp))

# 085 - 딕셔너리 생성
temp = {'메로나' : 1000, '폴라포' : 1200, '빵빠레' : 1800}
print(temp)

# 086 - 딕셔너리 삽입
# dictionary.update(dictionary) : 2개의 딕셔너리의 원소들을 하나로 합치는 메소드
temp1 = {'죠스바' : 1200, '월드콘' : 1500}
temp.update(temp1)
print(temp)

# 답지
# temp['조스바'] = 1200
# temp['월드콘'] = 1500 

# 087 - 딕셔너리 조회
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
result = ice.get('메로나')
# result = ice['메로나']
print('메로나 가격 : ',result)

# 088 - 딕셔너리 수정
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
# ice['메로나']=1300
ice.update({'메로나' : 1300})
print(ice)

# 089 - 딕셔너리 삭제
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
del ice['메로나']
print(ice)

# 090 - 
# 존재하지 않은 key 의 value 값을 조회해서 생긴 에러입니다.
# 딕셔너리에 없는 키를 인덱싱하면 발생하는 에러입니다.

# 091 - 딕셔너리 생성
inventory = {
    '메로나': [300, 20],
    '비비빅': [400, 3],
    '죠스바': [250, 100]
}
print(inventory)

# 092 - 딕셔너리 인덱싱
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
result = inventory.get('메로나')[0]
print(result, '원', sep = ' ')

# 093 - 딕셔너리 인덱싱
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
result = inventory['메로나'][1]
print(result, "개")

# 094 - 딕셔너리 추가
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}
inventory['월드콘'] = [500, 7]
print(inventory)

# 095 - 딕셔너리 keys() 메소드
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
result = list(icecream.keys())
print(result)

# 096 - 딕셔너리 values() 메소드
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
result = list(icecream.values())
print(result)

# 097 - 딕셔너리 values() 메소드
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
result = list(icecream.values())
result = sum(result)
print(result)

# 098 - 딕셔너리 update 메소드
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

# 099 - zip과 dict
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

# 100 - zip과 dict
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)