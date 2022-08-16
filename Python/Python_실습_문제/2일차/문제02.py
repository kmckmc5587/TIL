word = input()
l = 0
for i in word:
    l += 1
    print(l)

word = 'happy!'
count = 0
# 모든 문자를 돌면서
for char in word:
# 1씩 증가시킨다.
    count = count + 1
    # count += 1
    print(count)