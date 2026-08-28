# 연산자

#산술 연산자
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b) #소수점까지
print(a % b) #나머지
print(a // b) #몫
print(a ** b)

#복합 대입 연산자
a = 0
a += 4
print(a)

a -= 2
print(a)

#증감 연산자 없음
# b = a++과 b = ++a가 다르기 때문에 오류가 발생 -> 삭제 (추정)

#비교 연산자
print(3 == 3.0) #타입은 달라도 값만 같으면 True
print("apple" < "apble")
print(1 < 2 < 3) # 1 < 2 and 2 < 3
print(1 < 3 < 2) # 1 < 3 and 3 < 2

#논리 연산자
a = True
b = False

print(a and b) #False
print(a or b) #True
print(not b) #True


# Short-circuit 테스트
a = 10
b = 0

#print(a / b) Zero Division Error

if a > 0 or a / b:
    print("yes")
else:
    print("no")