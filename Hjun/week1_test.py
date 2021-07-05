# 유저에게 5명의 친구의 이름을 입력받고 각자의 나이에 대해 입력을 받으세요.
# 입력 받을때 구별은 공백으로합니다.(ex.철수 영희 형준 ... 과 같이 입력받음) (ex. 21 25 26 ...)
# 각각 입력받은 나이, 이름 이 두입력값들을 합쳐 딕셔너리 형태로 만들고
# for문을 사용하여 각자의 나이에 3년을 더한값으로 업데이트 후 이름과 나이를 출력하시오.
# 출력 예(철수:24, 영희:25, 형준:29 ...)

friends = input().split(' ')
age = input().split(' ')
age_int = []
for i in age:
    age_int.append(int(i)+3)

dictionary = dict(zip(friends,age_int))
print(', '.join('{}:{}'.format(k,v) for k,v in dictionary.items()))# python 람다