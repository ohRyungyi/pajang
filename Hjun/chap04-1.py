# 051
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
print(movie_rank)

# 052
movie_rank.append('배트맨')
print(movie_rank)

# 053
movie_rank.insert(1, '슈퍼맨')
print(movie_rank)

# 054
del movie_rank[3]
print(movie_rank)

# 055
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

# 056
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
print(lang1+lang2)

# 057
nums = [1, 2, 3, 4, 5, 6, 7]
print(f'max: {max(nums)}')
print(f'min: {min(nums)}')

# 058
nums = [1,2,3,4,5]
print(sum(nums))

# 059
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "쏘세지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 060
nums = [1, 2, 3, 4, 5]
avg = sum(nums)/len(nums)
print(avg)

# 후기
# append는 리스트의 맨뒤에 데이터를 붙여주는것
# insert는 지정한 위치에 데이터를 추가하는것
# del은 지정한 위치에 있는 데이터를 삭제하는것