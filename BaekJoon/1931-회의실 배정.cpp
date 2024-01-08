#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// 회의 시간을 저장하기 위한 구조체
struct Meeting {
    int start;
    int end;
};

// 끝나는 시간이 빠른 순, 같으면 시작 시간이 빠른 순으로 정렬하기 위한 함수
bool compare(Meeting a, Meeting b) {
    if (a.end == b.end) return a.start < b.start;
    return a.end < b.end;
}

int main() {
    int n;
    cin >> n;
    vector<Meeting> meetings(n);

    for (int i = 0; i < n; i++) {
        cin >> meetings[i].start >> meetings[i].end;
    }

    sort(meetings.begin(), meetings.end(), compare);

    int count = 0;
    int currentTime = 0;

    // 가능한 회의 선택
    for (int i = 0; i < n; i++) {
        if (meetings[i].start >= currentTime) {
            count++;
            currentTime = meetings[i].end;
        }
    }

    cout << count << endl; // 최대로 할 수 있는 회의의 수 출력

    return 0;
}
