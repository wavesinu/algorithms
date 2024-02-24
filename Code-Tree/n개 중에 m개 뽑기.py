def combination(n, m):
    answer = []

    def print_combination():
        for num in answer:
            print(num, end=" ")
        print()

    def find_combinations(current_num, cnt):
        if cnt == m:
            print_combination()
            return

        for num in range(current_num + 1, n + 1):
            answer.append(num)
            find_combinations(num, cnt + 1)
            answer.pop()

    find_combinations(0, 0)


m, n = tuple(map(int, input().split()))

# 함수 호출
combination(m, n)


# n, m = tuple(map(int, input().split()))
# answer = []

# def print_answer():
#     # for i in range(n):
#     #     if answer[i] == 1:
#     #         print(i + 1, end=" ")
#     # print()
#     for elem in answer:
#         print(elem, end=" ")
#     print()

# def choose(curr_num, cnt):
#     if curr_num == n + 1:
#         if cnt == m:
#             print_answer()
#         return
    
#     answer.append(curr_num)
#     choose(curr_num + 1, cnt + 1)
#     answer.pop()

#     choose(curr_num + 1, cnt)

# choose(1, 0)