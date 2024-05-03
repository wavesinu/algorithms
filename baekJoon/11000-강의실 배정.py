import sys
import heapq
input = sys.stdin.readline

N = int(input())
class_schedule = [list(map(int, input().split())) for _ in range(N)]
class_schedule.sort()

pq = list()
heapq.heappush(pq, class_schedule[0][1])

for i in range(1, N):
    if class_schedule[i][0] >= pq[0]:
        heapq.heappop(pq)
    heapq.heappush(pq, class_schedule[i][1])

print(len(pq))

