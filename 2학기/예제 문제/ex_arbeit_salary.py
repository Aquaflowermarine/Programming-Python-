# 일주일에 몇 시간 일하는지 입력받기.
week_time = input("일주일에 몇 시간 일 해?")

# 몇 주 일하는지 입력 받기.
how_long = input("몇 주 일 해?")

# 시급 얼마인지 입력받기
how_much = input("시급 얼마야?")

# 주 15시간 이상이면, 주휴수당 지급
# 주휴수당 : 주 5일 근무로 생각하고 1일치 더 줌.
if week_time >= 15:
    week_time += (week_time/5)

# 알바비 계산하기
salary = int(week_time) * int(how_long) * int(how_much)
print("알바비는 : ", salary)