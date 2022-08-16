N = int(input())
logs = dict()
for i in range(N):
    # 공백으로 나눠진 두 개의 언어
    # print(input.split())
    key, value = input().split()
    logs[key] = value
    # print(logs)

    # logs['Baha'] = 'enter'
    # logs['Askar'] = 'enter'
    # logs['Baha'] = 'leave'
    # logs['Artem'] = 'enter'

list_ = []
for key in logs:
    print(key)
    # value가 enter인 key를 찾아서 리스트에 저장
    if logs[key] == 'enter':
        list_.append(key)

# print(list_)
list_.sort(reverse = True)
for name in list_:
    print(name)