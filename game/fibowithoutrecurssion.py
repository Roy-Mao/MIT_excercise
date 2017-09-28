# 5:00
def iterative_fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        two_away = 1
        one_away = 1
        nums = 0
        while nums <= n:
            nums = two_away + one_away
            two_away = one_away
            one_away = nums
            nums = 0
        return one_away
print iterative_fibonacci(6)