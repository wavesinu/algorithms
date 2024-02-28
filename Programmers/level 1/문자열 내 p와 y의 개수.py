def solution(s):
    new_string = s.upper()
    count_p, count_y = 0, 0

    for i in new_string:
        if i == 'P':
            count_p += 1
        elif i == 'Y':
            count_y += 1

    if count_p != count_y:
        return "false"
    else:
        return "true"
    return True


def solution_v2(s):
    return s.upper().count('P') == s.upper().count('Y')