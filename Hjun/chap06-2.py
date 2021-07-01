# 091
ice = {
    '메로나':[300,20],
    '비비빅':[400,3],
    '죠스바':[250,100]
}
print(ice)

# 092
print('%d 원'%ice['메로나'][0])

# 093
print('%d 개'%ice['메로나'][1])

# 094
ice['월드콘'] = [500,7]
print(ice)

# 095
icecream = {
    '탱크보이': 1200,
    '폴라포': 1200,
    '빵빠레': 1800,
    '월드콘': 1500,
    '메로나': 1000
}
icecream_keys = list(icecream.keys())
print(icecream_keys)

# 096
icecream_values = list(icecream.values())
print(icecream_values)

# 097
icecream_values_sum = sum(icecream_values)
print(icecream_values_sum)

# 098
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

# 099
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys,vals))
print(result)

# 100
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date,close_price))
print(close_table)

# 후기
# zip기능은 처음봤다.
# zip은 리스트나 튜플 자료형으로 선언되어있는 변수두개를 키와 밸류로 구성해 딕셔너리로 만들때 사용된다.