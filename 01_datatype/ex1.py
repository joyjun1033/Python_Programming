# 변수
a = 2
b = 3
print(a, end="--") #a를 쓴 다음에 --프린트
print(b)
print(a, b, sep=",") #a와 b 중간에 콤마 프린트

a = 2; b = 3 #파이썬스럽지는 않음
print(a, b)

a, b = 2, 3
print(a, b) #한 줄에 쓰려면 이게 더 선호됨 #튜플 언패킹

a = b = c = 0

#값 swap
a, b = 2, 3
temp = a
a = b
b = temp
print(a, b)

a, b = b, a
print(a, b)

# 변수명 규칙 (C와 동일)
# 알파벳, 숫자, 특수문자(_)만 가능
# 숫자로 시작 불가
# 대소문자 구분
# 예약어 사용 불가

# scake_case
# camelCase

# name! = "pororo"
# 2name = "pororo"
# class = "test"

이름 = "뽀로로"
print(이름)