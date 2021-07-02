# 051 - 리스트 생성
# 리스트 생성 list = []
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)

# 052 - 리스트에 원소 추가
# 원소 추가시 list = list1 + list2 형태로 저장
# list.append(원소) : 인수로 전달받은 요소를 리스트의 끝에 덧붙여 추가
movie_rank.append("배트맨")
print(movie_rank)

# 053 - 리스트에 원소 삽입
# list.insert(위치, 원소): 삽입학 위치와 요소값을 전달받아 리스트의 중간에 삽입
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 054 - 리스트에 원소 삭제
# list.remove(원소) : 인수로 전달받은 요소값을 찾아서 삭제
#                    값이 2개 이상이면 처음 발견한 요소 하나만 삭제
# del(list[인덱스]) : 인수로 전달받은 리스트의 원소값을 삭제
movie_rank.remove("럭키")
print(movie_rank)

# 055 - 2개이상의 원소를 리스트에서 삭제
# list.pop() : 리스트의 맨 뒤에 있는 원소를 삭제
# list.pop(인덱스) : 리스트의 맨 뒤에서 인덱스 순서에 있는 원소를 삭제
movie_rank.pop()
movie_rank.pop()
print(movie_rank)

# 056 - 2개의 리스트의 모든 원소를 하나의 리스트로 합치기
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = lang1 + lang2
print(langs)

# 057 - 리스트의 최댓값, 최솟값
# min() : 리스트의 최솟값
# max() : 리스트의 최댓값
nums = [1, 2, 3, 4, 5, 6, 7]
print("max : ", max(nums))
print('min : ', min(nums))

# 058 - 리스트의 합
nums = [1, 2, 3, 4, 5]
tot = 0
for i in nums:
    tot += i
print(tot)

# 답지
# sum(list) : 리스트의 합의 값을 반환
print(sum(nums))

# 059 - 리스트의 갯수
# len(list) : 리스트의 길이를 반환
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 060 - 리스트의 평균
nums = [1, 2, 3, 4, 5]
print(sum(nums)/len(nums))

# 061 - 리스트 슬라이싱
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 062 - 리스트 슬라이싱
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = nums[ : :2]
print(result)

# 063 - 리스트 슬라이싱
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = nums[1: : 2]
print(result)

# 064 - 리스트 슬라이싱
nums = [1, 2, 3, 4, 5]
result = nums[::-1]
print(result)

# 065 - 리스트 인덱싱
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2], sep = ' ')

# 066 - join 메소드
# ''.join(list) : 리스트를 문자열로 변환
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
result = ' '.join(interest)
print(result)

# 067 - join 메소드
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
result = '/'.join(interest)
print(result)

# 068 - joi 메소드
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
result = '\n'.join(interest)
print(result)

# 069 - 문자열 split 메소드
string = "삼성전자/LG전자/Naver"
result = string.split('/')
print(result)

# 070 - 리스트 정렬
# list.sort() : 리스트 자체가 정렬된 상태로 재 배열된다.
# sorted(list) : 인자로 전달받은 리스트를 정렬하여 반환
data = [2, 4, 3, 1, 5, 10, 9]
result = sorted(data)
print(result)
result = data.sort()
print(data)