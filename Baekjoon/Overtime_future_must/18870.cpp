// 백준 18870 좌표 압축
// 240518 시간 초과
// 구글링으로 해결
// 좌표 압축 개념, lower_bound, erase, unique 함수

#include <iostream>
#include <algorithm> 
#include <vector>
using namespace std;

int main()
{

	int n;
	cin >> n;

	int* arr;
	arr = new int[n];

	vector<int> v;
	for (int i = 0; i < n; i++) {
		cin >> arr[i]; 

		v.push_back(arr[i]);
	}

	sort(v.begin(), v.end()); 
	v.erase(unique(v.begin(), v.end()), v.end());
  
	for (int i = 0; i < n; i++) {
		int idx = lower_bound(v.begin(), v.end(), arr[i]) - v.begin();
		cout << idx << " ";
	}

	return 0;
}