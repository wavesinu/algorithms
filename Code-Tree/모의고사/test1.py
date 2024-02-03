def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def max_gcd(chain_lengths):
    max_gcd_value = 0
    for i in range(len(chain_lengths)):
        for j in range(i+1, len(chain_lengths)):
            max_gcd_value = max(max_gcd_value, gcd(chain_lengths[i], chain_lengths[j]))
    return max_gcd_value

n = int(input())
chain_lengths = list(map(int, input().split()))

print(max_gcd(chain_lengths))