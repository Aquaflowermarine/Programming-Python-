in0 = input("탑승객 수는?")
in0 = int(in0)
out = input("하차객 수는?")
out = int(out)
sum = in0 - out
print("버스에 있는 사람 수는", sum)
if 0 <= sum < 10:
    print("여유")
elif 10 <= sum < 20:
    print("보통")
else:
    print("혼잡")