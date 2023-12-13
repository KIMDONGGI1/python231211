# 정규표현식
import re

result = re.search("[0-9]*th", "35th")
print(result)
print(result.group())

result = re.match("[0-9]*th", "35th")
print(result)
print(result.group())


result = re.search("\d{4}", "우리 동네는 52300")
print(result)
print(result.group())