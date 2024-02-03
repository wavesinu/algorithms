n, x, y = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    direction, distance = input().split()
    distance = int(distance)
    
    moved
    
    if direction == 'W':
        x -= distance
    elif direction == 'S':
        y -= distance
    elif direction == 'N':
        y += distance
    elif direction == 'E':
        x += distance

if x == 0 and y == 0:
    print("Yes")
else:
    print("No")