participants = input().split(" ")

correct = input().split(" ")

score = dict(zip(participants, correct))
sum = 0
num = len(participants)

for i in range(num) :
    if correct[i] == "기권" :
        del score[participants[i]]
        del participants[i]
        num -= 1 #for로 다시 올라가기 때문에 이렇게 하면 안 된다 correct를 지우면 안 된다
    else :
        sum = sum + int(correct[i])

average = sum / len(correct)

for i in range(num) :
    if int(score[participants[i]]) <= average :
        del score[participants[i]]

print(score)

score = score.items()
print(score)

sorted(score, key=lambda x: x[1])

========


friend = input()
friend = friend.split(" ")
age = input()
age = age.split(" ")
info = dict(zip(friend, age))
print(info)

for i in range(len(friend)) :
    info[friend[i]] = int(info[friend[i]])+3

print(info)


# for i in range(len(correct)) :
#     if correct[i] == "기권" :
#         del correct[i]
#         del participants[i]

# average = sum(correct)/len(correct)

# for i in range(len(correct)) :
#     if correct[i] < average 
#         del correct[i]
#         del participants[i]



