import random
from os.path import * # 운영체제에서 제공하는 파일, 파일의 정보
from os import * # 운영체제의 정보

print(random.random()) # 0.0~1.0 사이의 실수
print(random.random())

# 리스트 내장(리스트 컴프리헨션)
print([random.randrange(20) for i in range(10)]) 
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])

# 샘플함수, 중복된 숫자 안나옴
print("---sample---")
print(random.sample(range(20), 10))
print(random.sample(range(20), 10))

print("---로또번호 생성---")
print(random.sample(range(1,46),5))
print(random.sample(range(1,46),5))
print(random.sample(range(1,46),5))
print(random.sample(range(1,46),5))
print(random.sample(range(1,46),5))

print(abspath("python.exe"))
print(basename("c:\\python310\\python.exe"))

fileName = "c:\\python310\\python.exe"
if exists(fileName):
    print("파일의 크기:{0}".format(getsize(fileName)))
else:
    print("파일 없음")

print("현재 작업폴더:{0}".format(getcwd()))

print("---운영체제---")
print(name)
print(environ)
system("notepad.exe")
 