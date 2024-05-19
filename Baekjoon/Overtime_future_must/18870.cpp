// 백준 18870 좌표 압축
// 240518 시간 초과
// 구글링으로 해결
// 좌표 압축 개념, lower_bound, erase, unique 함수 등 공부 완료
// 효율성 개념 인지

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

	// O(n)

	sort(v.begin(), v.end()); // sort = O(n*logn) (quick sort)
	v.erase(unique(v.begin(), v.end()), v.end());
	// unique = O(n) -> 중복되지 않는 원소들을 앞으로 끌어온다. 중복되는 건 다 뒤로 보냄. 뒤로 보내진 것들 중 가장 첫 번째 원소의 주소 리턴
	// erase = O(n) -> 첫번째 파라미터 ~ 두 번째 파라미터 까지의 원소들 삭제
	// erase(unique) = O(2n)

	// O(n*logn) + O(2n) = O(n*logn)
  
	for (int i = 0; i < n; i++) {
		int idx = lower_bound(v.begin(), v.end(), arr[i]) - v.begin();
		// lower_bound / upper_bound : binary search -> O(logn)
		cout << idx << " ";
	}

	// O(n*logn)

	// O(n) + O(n*logn) + O(n*logn) = O(n*logn)

	return 0;
}