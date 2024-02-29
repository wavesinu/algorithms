import re


def solution(user_id: str) -> str:
    new_id = user_id.lower()
    symbols = set(["-", "_", "."])

    def is_valid_char(char, symbols):
        return char.isalnum() or char in symbols

    # 1. symbols와 다른 기호를 삭제
    new_id = ''.join(char for char in new_id if is_valid_char(char, symbols))

    # 2. 마침표가 2번 이상 연속된 부분을 하나의 마침표로 치환
    new_id = re.sub('\.+', '.', new_id)

    # 3. 마침표가 처음이나 끝에 위치한다면 제거
    new_id = new_id.strip('.')
    # while '..' in new_id:
    #     new_id = new_id.replace('..', '.')

    # 4. new_id가 빈문자열이라면 new_id에 a를 대입
    if new_id == '':
        new_id = 'a'

    # 5. new_id의 길이가 16자 이상이라면, new_id의 첫 15개 문자를 제외한 나머지 문자들을 모두 제거
    # 6. 만약 제거 후, 마침표가 new_id의 끝에 위치한다면 끝에 위치한 마침표 제거

    if len(new_id) > 15:
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')

    # 7. new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임
    while len(new_id) < 3 and new_id:
        new_id += new_id[-1]

    return new_id


a = input()
print(solution(a))
