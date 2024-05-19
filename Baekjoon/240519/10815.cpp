// 백준 10815 숫자 카드
// 시간초과
// cin.tie(NULL);
// ios_base::sync_with_stdio(false);
// 추가해 줬더니 통과

#include <iostream>
#include <algorithm> 
#include <vector>

using namespace std;

int main()
{

	cin.tie(NULL);
	ios_base::sync_with_stdio(false);

	int n;
	cin >> n;

	vector<int> arr;
	int input_num;

	for (int i = 0; i < n; i++) {
		cin >> input_num; 
		arr.push_back(input_num);
	}

	sort(arr.begin(), arr.end());

	int new_n;
	cin >> new_n;

	int new_input_num;

	for (int i = 0; i < new_n; i++) {
		cin >> new_input_num;
		int idx = lower_bound(arr.begin(), arr.end(), new_input_num) - arr.begin();
		if (idx < arr.size()) { // 만약 제일 큰 숫자보다도 더 큰 숫자가 들어오면 idx = arr.end() + 1. 그 경우까지 모두 고려 필요!!
			if (arr[idx] == new_input_num) {
				cout << "1" << " ";
			}
			else {
				cout << "0" << " ";
			}
		}
		else {
			cout << "0" << " ";
		}
	}

	return 0;
}