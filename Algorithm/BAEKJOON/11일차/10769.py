import sys

sys.stdin = open("10769.txt")

emoticon = input()
happy, sad = 0, 0
for i in range(0, len(emoticon) - 2):
    if emoticon[i] == ':' and emoticon[i + 1] == '-':
        if emoticon[i + 2] == ')':
            happy += 1
        elif emoticon[i + 2] == '(':
            sad += 1

if happy == 0 and sad == 0:
    print('none')
else:
    if happy > sad:
        print('happy')
    elif happy < sad:
        print('sad')
    else:
        print('unsure')