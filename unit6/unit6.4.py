# 입력 값을 변수 두개에 저장하기
a, b = input('문자열 두개를 입력하세요: ').split()
print(a)
print(b)
a = int(a)
b = int(b)
print(a + b)
print(int(a) + int(b))

a, b = map(int, input('숫자 두 개를 입력하세요: ').split())
print(a + b)
