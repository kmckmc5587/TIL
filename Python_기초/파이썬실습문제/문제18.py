string = input('Dictionary:')

dic = {}

for chr in string:
    if chr in dic:
        dic[chr] += 1
    else:
        dic[chr] = 1
print(dic)