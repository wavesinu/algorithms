def solution(num):
    nums = [int(i) for i in reversed(str(num))]
    return nums


def solution_v2(num):
    return list(map(int, reversed(str(num))))


print(solution(int(input())))
