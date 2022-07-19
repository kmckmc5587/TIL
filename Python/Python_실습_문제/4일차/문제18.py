string = input('Dictionary:')

dic = {}

for chr in string:
    if chr in dic:
        dic[chr] += 1
    else:
        dic[chr] = 1
print(dic)

word = 'banana'

result = {}
for char in word:
    # 딕셔너리에 키가 있으면?
    if not char in result:
        # 키랑 값을 0으로 초기화한다.
        result[char] = 1
    # 딕셔너리에 키가 없으면?
    else:
        result[char] = result[char] + 1
        print(result)