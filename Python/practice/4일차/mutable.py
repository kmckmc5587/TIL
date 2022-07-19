# 리스트는 mutable
a = [1, 2, 3]
a[0] = 100
print(a)
# 리스트는 바꿀 수 있다~!

# 문자열은 immutable
a = 'hi'
a[0] = 'c'
print(a)
# 문자열의 첫 번째 인덱스에 해당하는 값을 바꿀 수 있냐? 없다~!
# Traceback (most recent call last):
#   File "C:\Users\김민찬\Desktop\TIL\Python_기초\practice\4일차\mutable.py", line 8, in <module>
#     a[0] = 'c'
# TypeError: 'str' object does not support item assignment