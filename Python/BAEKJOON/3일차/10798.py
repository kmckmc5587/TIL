words = []
length = []

for i in range(5):
    word = input()
    words.append(word)
    length.append(len(word))

read = ''
for i in range(max(length)):
    for j in range(5):
        if i < length[j]:
            read += words[j][i]

print(read)