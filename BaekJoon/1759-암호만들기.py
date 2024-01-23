import sys


def generate_passwords(L, C, chars):
    vowels = set("aeiou")
    chars.sort()

    def backtrack(start, path, vowel_count, consonant_count):
        if len(path) == L:
            if vowel_count >= 1 and consonant_count >= 2:
                passwords.append(''.join(path))
            return

        for i in range(start, C):
            if chars[i] in vowels:
                backtrack(i + 1, path + [chars[i]], vowel_count + 1, consonant_count)
            else:
                backtrack(i + 1, path + [chars[i]], vowel_count, consonant_count + 1)

    passwords = []
    backtrack(0, [], 0, 0)
    return passwords


# 사용자 입력
L, C = map(int, sys.stdin.readline().split())
chars = input().split()

# 가능한 암호들 생성
possible_passwords = generate_passwords(L, C, chars)
for password in possible_passwords:
    print(password)
