# 081
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, a,b = scores
print(valid_score)

# 082
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a,b,*valid_score = scores
print(valid_score)

# 083
a, *valid_score, b = scores
print(valid_score)

# 084
temp = {}
print(type(temp))

# 085
dictionary = {
    '메로나':1000,
    '폴라포':1200,
    '빵빠레':1800
}
print(dictionary)

# 086
dictionary['죠스바']=1200
dictionary['월드콘']=1500
print(dictionary)

# 087
print('메로나 가격: %d'%dictionary['메로나'])

# 088
dictionary['메로나']=1300
print(dictionary)

# 089
del dictionary['메로나']
print(dictionary)

# 090
# 딕셔너리내에 존재하지 않는 키값을 호출했으므로 에러가 발생하였다.

# 후기
# 나머지는 아는내용이였으나 star expression이라는 용어는 처음들었다.
# *의 기능만 알았지 용어는 처음이었고
# 변수중 파이썬내에서 _는 자리를 차지할뿐 값을 사용하지 않을때 사용한다.