# 071
my_variable = ()
print(type(my_variable))

# 072
movie_rank = ('닥터 스트레인지','스플릿','럭키')
print(movie_rank)

# 073
tuple_int = (1,)
print(type(tuple_int))

# 074
# 튜플은 수정이 불가능한 자료형이므로 0번째 자리에 임의의 값으로 변경이 불가능하다.

# 075
t = 1, 2, 3, 4
print(type(t))
# 튜플은 괄호와 함께 선언되어야함이 맞지만 괄호가 없더라도 선언이 가능하다.

# 076
t = ('a', 'b', 'c')
# 튜플은 임의로 값을 변경할수 없으므로 새롭게 선언해야한다.

# 077
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest_list = list(interest)
print(type(interest_list))

# 078
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest_tuple = tuple(interest)
print(type(interest_tuple))

# 079
# apple banana cake

# 080
data = tuple(range(2,100,2))
print(data)

# 후기
# 수정이 안되는것을 제외하고는 리스트와 같아 쉬웠다.
# 괄호가 없더라도 변수에 값을 나열하여 저장하면 리스트가 아닌 
# 튜플로 선언된다는것을 알게 되었다.