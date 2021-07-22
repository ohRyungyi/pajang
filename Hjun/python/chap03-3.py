# 041
ticker = "btc_krw"
ticker_upper = ticker.upper()
print(ticker_upper)

# 042
ticker = "BTC_KRW"
ticker_lower = ticker.lower()
print(ticker_lower)

# 043
string = "hello"
print(string.capitalize())

# 044
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

# 045
print(file_name.endswith(("xlsx", "xls")))

# 046
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

# 047
a = "hello world"
a_split = a.split(' ')
print(a_split)

# 048
ticker = "btc_krw"
ticker_split = ticker.split('_')
print(ticker_split)

# 049
date = "2020-05-01"
year, month, nal = date.split('-')
print(year, month, nal)

# 050
data = "039490     "
print(data.rstrip())

# 후기
# 대문자로 바꿔줄때는 upper, 소문자는 lower함수
# 맨앞의 문자만 바꿔줄때는 capitalize함수
# 문자열의 마지막 문자열을 찾아볼때 endswith, 시작 문자열은 startswith를 씀으로써 True, False값을 반환한다.
