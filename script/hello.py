import sys

print("hello")
a = 4
b = 4
print(a is b)
### a 와 b 는 같은 객체화 된다??? 메모리의 효율을 위해 >> cache 구조 인터프리터의 영역 저장소

c = 4
print(sys.getrefcount(4))

a, b = ("python", "life")

c = ["aa", "bb"]
[a, b] = ["python", "life"]
print(c)
