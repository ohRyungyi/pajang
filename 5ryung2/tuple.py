# 071 - 빈 튜플 생성
# tuple = () : 빈 튜플 생성
my_variable = ()
print(my_variable)

# 072 - 튜플에 원소 저장
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank)

# 073 - 튜플에 원소 저장
data = (1)
print(data)

# 074 - tuple immutable
# 튜플 생성시 숫자의 원소들을 저장하였지만, 해당 값을 문자로 변경하려고 하니까 오류가 발생하였다.
# 튜플의 원소 값은 변경이 불가능하다

# 075 - 
t = 1, 2, 3, 4
print(type(t))
# tuple으로 바인딩 된다. 튜플의 경우 괄호를 생략해도 튜플로서 생성된다.

# 076 - 
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
print(t)

# 077 - 튜플을 리스트로 변환
interest = ('삼성전자', 'LG전자', 'SK Hynix')
result = list(interest)
print(type(result))

# 078 - 리스트를 튜플로 변환
interest = ['삼성전자', 'LG전자', 'SK Hynix']
result = tuple(interest)
print(type(result))

# 079 - 튜플 언팩킹
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)
# apple banana cake 이 출력

# 080 - range 함수
# (2, 4, 6, 8 ... 98)
result = tuple(range(2, 100, 2))
print(result)