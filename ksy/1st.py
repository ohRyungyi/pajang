participants = input()
participants = participants.split(" ")

correct = input()
correct = correct.split(" ")

sum = 0
for i in range(len(correct)) :
    if correct[i] == "기권" :
        del correct[i]
        del participants[i]
    else :
        sum = sum + int(correct[i])

score = dict(zip(participants, correct))
average = sum / len(participants)

for i in range(len(participants)) :
    if int(score[participants[i]]) <= average :
        del score[participants[i]]
        del correct[i]
        del participants[i]

# for i in range(len(participants)) :
#     if


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



