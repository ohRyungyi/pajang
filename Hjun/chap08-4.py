# 161
for i in range(0,100):
    print(i)

# 162
for i in range(2002,2051,4):
    print(i)

# 163
for i in range(1,31):
    if i%3==0:
        print(i)

# 164
for i in reversed(range(0,100)):
    print(i)

# 165
for i in range(0,10):
    print(f'0.{i}')

# 166
for i in range(1,10):
    print(f'3 x {i} = {3*i}')

# 167
for i in range(1,10):
    if i%2 != 0:
        print(f'3 x {i} = {3*i}')

# 168
sum = 0
for i in range(1,11):
    sum+=i
print(f'합 : {sum}')

# 169
sum = 0
for i in range(1,11):
    if i %2!=0:
        sum+=i
print(f'합: {sum}')

# 170
sum = 1
for i in range(1,11):
    sum *=i

print(sum)