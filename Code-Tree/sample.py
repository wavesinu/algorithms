k, n = tuple(map(int, input().split()))
selected_nums = []

def print_permutation():
    for num in selected_nums:
        print(num, end=' ')
    print()
    
def find_permutations(cnt):
    if cnt == n:
        print_permutation()
        return
    
    for num in range(1, k + 1):
        if cnt >= 2 and selected_nums[cnt - 2] == selected_nums[cnt - 1] == num:
            continue
        
        selected_nums.append(num)
        find_permutations(cnt + 1)
        selected_nums.pop()
        
find_permutations(0)
