#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> nums(n);

    for (int i = 0; i < n; i++)
    {
        cin >> nums[i];
    }

    int max_sum = nums[0];  // 최대 부분 배열합 초기화
    int current_sum = nums[0];  // 현재 부분 배열합 초기화

    for (int i = 1; i < n; i++)
    {
        current_sum = max(nums[i], current_sum + nums[i]);  // 현재 부분 배열합 갱신
        max_sum = max(max_sum, current_sum);    // 최대 부분 배열합 갱신
    }

    cout << max_sum << endl;

    return 0;
}
