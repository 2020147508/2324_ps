// 백준 1181 나이순 정렬

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

struct inst {
    int age; // string 아니라 int로 해야 두 자리 수, 세 자리 수 제대로 비교할 수 있음
    string name;
    int index;
};

bool compare(inst a, inst b) { 
    if (a.age != b.age) {
        return a.age < b.age;
    }
    else {
        return a.index < b.index;
    }
}

int main()
{
    string num;
    getline(cin, num);
    int n = stoi(num);
    inst* arr;
    arr = new inst[n];

    for (int i = 0; i < n; i++) {
        string str;
        getline(cin, str);
        int size_of_str = str.length();

        int split_index = str.find(" ");
        arr[i].age = stoi(str.substr(0, split_index));
        arr[i].name = str.substr(split_index + 1, size_of_str - (split_index + 1));
        arr[i].index = i;
    }

    sort(arr, arr + n, compare);

    for (int i = 0; i < n - 1; i++) {
        cout << arr[i].age << " " << arr[i].name << "\n";
    }
    cout << arr[n-1].age << " " << arr[n-1].name;
}