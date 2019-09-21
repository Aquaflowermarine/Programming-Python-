#P.217
l = [1, 2, 3]
try:
    print(l[1])
    print(l[2])

except IndexError as e:
    print("인덱스에러")
    print(e)
else:
    print("성공적으로 모든 코드를 실행")