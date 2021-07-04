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
print(', '.join('{}:{}'.format(k,v) for k,v in dictionary.items()))

# 사용자에게 5자리 숫자를 입력받는다
# "일의 자리"부터 각 자리수에 3,4,5,6,7을 곱한 뒤 그 값을 전부 더한다 (#합계의 변수는 sum으로, #for문을 사용하세요)
# sum을 3으로 나눈 나머지를 고유번호로 알려준다 (#format을 사용하세요)
# ** 각 과정이 보일 수 있도록 for 문을 작성하세요

# ex. 
# 5자리 숫자를 입력하세요 : 12345
# 5 x 3 = 15
# 4 x 4 = 16
# 3 x 5 = 15
# 2 x 6 = 12
# 1 x 7 = 7
# 합계 : 65
# 고유번호는 "2" 입니다. (#반드시  "고유번호"로 나타내주세요)

user_input = input()
sum = 0
key = 3
for i in user_input[::-1]:
    sum+= int(i)*key
    key+=1
result = sum%3
print(f'고유번호는 \"{result}\" 입니다.')