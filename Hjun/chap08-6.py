# 181
apart = [['101호', '102호'],['201호','202호'],['301호','302호']]
print(apart)

# 182
stock = [[100,200,300],[80,210,330]]
print(stock)

# 183
key = [100,200,300]
value = [80,210,330]
stock=dict(zip(key,value))
print(stock)

# 184
stock={'10/10':[80,110,70,90],'10/11':[210,230,190,200]}
print(stock)

# 185
apart = [ [101, 102], [201, 202], [301, 302] ]
for k,v in apart:
    print(f'{k} 호')
    print(f'{v} 호')

# 186
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in reversed(range(0,3)):
    print(apart[i][1])
    print(apart[i][0])

# 187
for row in apart[::-1]:
    for col in row[::-1]:
        print(col, "호")

# 188
for i in apart:
    for j in i:
        print(f'{j} 호')
        print('-----')

# 189
for i in apart:
    for j in i:
        print(f'{j} 호')
    print('-----')

# 190
for i in apart:
    for j in i:
        print(f'{j} 호')
print('-----')