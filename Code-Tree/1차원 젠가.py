# 처음 놓여있는 블럭의 수 n
n = int(input())

# n개의 줄에 걸쳐 각 층에 놓여있ㅅ는 블럭에 적힌 숫자를 입력 받음



# 첫 번째로 제거할 블럭의 정보를 나타내는 s1, e1 값을 공백을 사이에 두고 입력 받음
s1, e1 = map(int, input().split())

# 두 번째로 제거할 블럭의 정보를 나타내는 s2, e2 값을 공백을 사이에 두고 입력 받음
s2, e2 = map(int, input().split())

# 블럭을 제거하는 함수
def remove_block(s, e, blocks):
    temp_blocks = blocks.copy()
    for i in range(s-1, e):
        temp_blocks[i] = [0] * len(temp_blocks[i])
    return temp_blocks

# 블럭을 제거
blocks = remove_block(s1, e1, blocks)
blocks = remove_block(s2, e2, blocks)

# 첫줄에는 남아있는 블럭의 수를 출력
print(sum(map(sum, blocks)))

# 둘째 줄부터는 남아있는 블럭의 정보를 출력
for block in blocks:
    for elem in block:
        if elem != 0:
            print(elem, end=' ')
    print()