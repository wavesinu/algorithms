import sys
sys.setrecursionlimit(10**6)

def postorder(start, end):
    if start > end:
        return
    root = pre[start]
    i = start + 1
    while i <= end:
        if pre[i] > root:
            break
        i += 1
    postorder(start + 1, i - 1)
    postorder(i, end)
    print(root)

pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break

postorder(0, len(pre) - 1)