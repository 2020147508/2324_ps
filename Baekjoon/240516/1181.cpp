#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// 그냥 sort는 처음 정렬되기 전 주어진 순서가 보장 X (퀵 정렬)
// 아래 compare처럼 모든 경우의 순서 조건을 명시해주던지 아니면 sort(v.begin(), v.end()) 하고서 stable_sort(v.begin(), v.end(), compare) 해 주기

bool compare(string a, string b) { 
    if (a.size() != b.size()) {
        return a.size() < b.size();
    }
    else {
        return a < b;
    }
}

int main()
{
    int n;
    cin >> n;
    vector<string> v;
    
    for (int i = 0; i < n; i++) {
        string str;
        cin >> str;
        int itsnotok = 0;
        for (int j = 0; j < v.size(); j++) {
            if (v[j] == str) {
                itsnotok = 1;
            }
        }
        if (itsnotok == 0) {
            v.push_back(str);
        }
    }

    sort(v.begin(), v.end(), compare);

    for (int i = 0; i < v.size()-1; i++) {
        cout << v[i] << "\n";
    }
    cout << v[v.size() - 1];
}