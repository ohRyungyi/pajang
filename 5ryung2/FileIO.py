# # 291
# # 005930
# # 005380
# # 035420
# f = open("./5ryung2/매수종목1.txt", mode = "wt", encoding = "utf-8")
# f.write("005930\n")
# f.write("005380\n")
# f.write("035420\n")
# f.close()

# # 292
# # 005930 삼성전자\n
# # 005380 현대차\n
# # 035420 NAVER\n
# f = open("./5ryung2/매수종목2.txt", mode = "wt", encoding = "utf-8")
# f.write("005930 삼성전자\n")
# f.write("005380 현대차\n")
# f.write("035420 NAVER\n")
# f.close()

# # 293
# import csv
# f = open("./5ryung2/매수종목3.csv", mode = "wt", encoding = "cp949")
# writer = csv.writer(f)
# writer.writerow(["종목명", "종목코드", "PER"])
# writer.writerow(["삼성전자", "005930", "15.72"])
# writer.writerow(["NAVER", "035420", "55.82"])
# f.close()

# # 294
# f = open("./5ryung2/매수종목1.txt", encoding = "utf-8")
# lines = f.readlines()

# codes = []
# for line in lines:
#     code = line.strip()
#     codes.append(code)

# print(codes)
# f.close()

# # 295
# f = open("./5ryung2/매수종목2.txt", encoding = "utf-8")
# lines = f.readlines()

# items = dict()

# for line in lines:
#     item = line.strip().split(' ')
#     items[item[1]] = item[0]

# print(items)
# f.close()

# # 296
# per = ["10.31", "", "8.00"]

# for i in per:
#     try :
#         print(float(i))
#     except:
#         print(0)


# # 297
# per = ["10.31", "", "8.00"]
# nPer = []

# for i in per:
#     try:
#         nPer.append(float(i))
#     except:
#         nPer.append(float(0))

# print(nPer)

# # 298
# try:
#     b = 3/0
# except ZeroDivisionError:
#     print('0으로 나눌수 없습니다.')

# # 299
# # try:
# #     실행코드
# # except 예외 as 변수:
# #     예외처리코드 

# data = [1, 2, 3]

# for i in range(5):
#     try:
#         print(data[i]) 
#     except IndexError as error:
#         print(error)

# # 300
# # try:
# #     실행 코드
# # except:
# #     예외가 발생했을 때 수행할 코드
# # else:
# #     예외가 발생하지 않았을 때 수행할 코드
# # finally:
# #     예외 발생 여부와 상관없이 항상 수행할 코드

# per = ["10.31", "", "8.00"]

# for i in per:
#     try:
#         print(float(i))
#     except:
#         print(float(0))
#     else:
#         print('clean data', end=' ')
#     finally:
#         print('print per data ', end=' ')