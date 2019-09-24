#p.219

class OddError(Exception):
    def __init__(self, message="홀수는 안 됩니다."):
        self.message = message

    def __str__(self):
        return self.message

n = 10
if n % 2 != 0:
    raise OddError
else:
    print(n, ", n/2 =", n/2)