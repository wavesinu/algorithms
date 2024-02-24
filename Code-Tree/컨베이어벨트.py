n, t = tuple(map(int, input().split()))
u = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(t):
    # Step 1
    # 위에서 가장 오른쪽 요소를 저장
    temp = u[n - 1]
    
    # Step 2
    # 위에서 가장 오른쪽 요소를 제외한 나머지 요소를 오른쪽으로 한 칸씩 이동
    for i in range(n - 1, 0, -1):
        u[i] = u[i - 1]
    u[0] = d[n - 1]
    
    # Step 3
    for i in range(n - 1, 0, -1):
        d[i] = d[i - 1]
    d[0] = temp
    
for elem in u:
    print(elem, end=' ')
print()

for elem in d:
    print(elem, end=' ')

