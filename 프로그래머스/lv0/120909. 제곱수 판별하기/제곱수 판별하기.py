def solution(n):
    x = n ** 0.5
    if x % 1 == 0:
        return 1
    return 2