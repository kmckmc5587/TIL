word = input()
index = 0

for i in range(len(word)):
    if word[i] == 'a':
        print(i)
        index = 1
        break
if index == 0:
    print('-1')

word = input()

for i in range(len(word)):
    if word[i] == 'a':
        print(i, end = ' ')