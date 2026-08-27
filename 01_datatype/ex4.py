# 문자열
# "", ''

a = "python"
print(a, type(a))

# I'll be back
print("I'll be back")
print('I\'ll be back')

multiline = """
Life is short
You need Python
""" #멀티 라인으로 쓸 때는 쌍따옴표 세개

print(multiline)

# docstring
def func():
    """이 함수는 테스트용입니다."""
    pass

print(func.__doc__)

# 문자열 연결
print("Hello" + "Python")

#문자열 반복
print("Hello" * 10)
print("*" * 50)

# 문자열끼리만 +가능
#print("Hello" + 10)
print("Hello" + str(10))

print("10" + "2")
print(int("10") + int("2"))

#문자열 포캣팅 (f-string)
name = "pororo"
age = 23

print(f"이름: {name}, 나이: {age}살")
print(f"내년 나이: {age+1}살")
print(f"{name.upper()}")

pi = 3.141592

print(f"{pi:.3f}")
print(f"{pi:.0f}")

num = 123456789

print(f"{num:,}") #천(1000) 단위로 콤마를 찍어주는 기능
print(f"{num:15d}") #오른쪽 정렬은 '>' 생략 가능
print(f"{num:<15d}")
print(f"{num:015d}") #앞을 0으로 채운다
print(f"{num:015,d}")