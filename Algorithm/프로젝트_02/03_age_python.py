import random

print('==========나이를 알려드립니다.==========')
name = input('이름을 입력해주세요:')
print('=======================================')
# 이름마다 똑같은 숫자가 있으면 좋겠다...
# 민찬
# ord(민) # 문자 => 숫자
# ord(찬) # 문자 => 숫자
# 합한 값을 가져가면 이름마다 같겠다.
random.seed(sum(map(ord, name)))
print(f'{random.choice(range(10, 90))}살 입니다.')