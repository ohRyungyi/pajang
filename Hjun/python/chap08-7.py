# 191
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for i in data:
    for j in i:
        print(j+(j*0.00014))

# 192
for i in data:
    for j in i:
        print(j+(j*0.00014))
    print('----')

# 193
result =[]
for i in data:
    for j in i:
        result.append(j+(j*0.00014))
print(result)

# 194

result = []
for i in data:
    result_1 =[]
    for j in i:
        result_1.append(j+(j*0.00014))
    result.append(result_1)
print(result)

# 195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:
    print(i[3])


# 196
for i in ohlc[1:]:
    if i[3] >150:
        print(i[3])

# 197
for i in ohlc[1:]:
    if (i[0] <= i[3]):
        print(i[3])

# 198
volatility= []

for i in ohlc[1:]:
    value = i[1]-i[2]
    volatility.append(value)
print(volatility)

# 199
for i in ohlc[1:]:
    if i[3] > i[0]:
        print(i[1]-i[2])

# 200
sum = 0
for i in ohlc[1:]:
    sum+=(i[3]-i[0])
print(sum)