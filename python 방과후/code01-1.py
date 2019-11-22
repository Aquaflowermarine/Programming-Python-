i, j, hap = 0, 0
num = 0

num = int(input("값을 입력하세요: "))

for i in range(1, num + 1, 1):
    hap = hap + i

print("1에서 %d 까지의 합계 : %d % (num, hap)")

num2 = int(input("단을 입력하세요: "))

for j in range(1, num * 1, 1):
    hap = hap * j

