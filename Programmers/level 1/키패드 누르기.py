from typing import List


def solution(numbers: List[int], hand: str) -> str:
    answer = ""
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        "*": (3, 0), 0: (3, 1), "#": (3, 2)
    }

    left = keypad["*"]
    right = keypad["#"]

    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            left = keypad[number]
        elif number in [3, 6, 9]:
            answer += "R"
            right = keypad[number]

        else:
            # 누르려는 키패드로부터 왼손 오른손 거리 계산
            left_distance = abs(left[0] - keypad[number][0]) + abs(left[1] - keypad[number][1])
            right_distance = abs(right[0] - keypad[number][0]) + abs(right[1] - keypad[number][1])

            if left_distance < right_distance:
                answer += "L"
                left = keypad[number]
            elif left_distance > right_distance:
                answer += "R"
                right = keypad[number]

            else:
                if hand == "left":
                    answer += "L"
                    left = keypad[number]
                else:
                    answer += "R"
                    right = keypad[number]
    return answer


# 테스트
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))  # "LRLLLRLLRRL"