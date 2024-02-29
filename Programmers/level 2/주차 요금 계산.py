from typing import List


def solution(fees: List[int], records: List[str]) -> List[int]:
    default_hour = fees[0]
    default_fee = fees[1]
    unit_time = fees[2]
    unit_fee = fees[3]

    cars = {}
    result = {}

    for record in records:
        time, car_num, state = record.split()
        if car_num not in cars:
            cars[car_num] = []
        cars[car_num].append((time, state))

    for car_num, record in cars.items():
        if len(record) % 2 == 1:  # 입차 기록만 있는 경우
            record.append(("23:59", "OUT"))

        total_hour = 0
        for i in range(0, len(record), 2):
            in_time, in_state = record[i]
            out_time, out_state = record[i + 1]

            in_hour, in_minute = map(int, in_time.split(':'))
            out_hour, out_minute = map(int, out_time.split(':'))

            total_hour += (out_hour - in_hour) * 60 + (out_minute - in_minute)

        if total_hour <= default_hour:
            result[car_num] = default_fee
        else:
            result[car_num] = default_fee + (total_hour - default_hour) // unit_time * unit_fee
            if (total_hour - default_hour) % unit_time != 0:
                result[car_num] += unit_fee

    # 차 번호 순으로 정렬된 결과를 출력
    return [result[car_num] for car_num in sorted(result.keys())]


    # test case


fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
           "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))
