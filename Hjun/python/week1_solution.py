# 코딩테스트 대회가 개최되었습니다. 이 때, 참여자들 이름을 공백을 통해 구분을 하여 입력을 합니다.
# 예) "홍길동" "김길동" "최길동"
# 그 후 코딩테스트에서 순차대로 각 대회에서 맞춘 문제를 공백을 통해 구분하여 입력이 됩니다.
# 예) 2 10 4
# 만약 중간에 기권을 했을 경우 '기권'이라고 입력이 됩니다.
# 예) 2 10 기권
# 이 때 기권을 하지 않은 학생들의 성적의 평균을 넘긴 학생들만은 참가상을 모두 받을 수 있습니다.
# 참가상을 받은 학생들을 푼 점수가 높은 순서대로 공백으로 구분하여 출력해 주세요
import operator
names = input().split(' ')
scores = input().split(' ')
dictionary = dict(zip(names,scores))
sum = 0
awards = []
for i in range(len(dictionary.keys())):
    if dictionary[i] == "기권":
        del dictionary[i]
    else:
        sum += int(dictionary[i])
avg = int(sum/len(dictionary.keys()))
for i in range(len(dictionary.keys())):
    dictionary[i] = int(dictionary[i])
    if dictionary[i] < avg:
        del dictionary[i]
    else:
        continue

sdict= sorted(dictionary.items(), key=operator.itemgetter(0))
print(sdict.keys())