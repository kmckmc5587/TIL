N = 7
gom = 0
log_list = [
    'ENTER', 'pjshwa', 'chansol', 'chogahui05', 'ENTER', 'pjshwa', 'chansol'
]
set_ = set()
for log in log_list:
    if log == 'ENTER':
        set_.clear()

    else:
        # 닉네임 = log
        if log not in set_:
            set_.add(log)
            gom += 1

print(gom)