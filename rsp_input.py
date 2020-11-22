# selected = None
# while selected not in ['가위', '바위', '보']:
#     selected = input('가위, 바위, 보 중에서 선택하세요> ')
# print('선택한 값은:', selected)

st = 'Programming'
# 자음이 나타나는 동안만 출력하는 기능
for ch in st:
    if ch in ['a','e','i','o','u']:
        continue #모음일 경우 아래 출력을 건너띈다
    print(ch)
print('The end')

st = 'Programming'
# 자음이 나타나는 동안만 출력하는 기능
for ch in st:
    if ch in ['a','e','i','o','u']:
        break #모음일 경우 반복문을 종료
    print(ch)
print('The end')