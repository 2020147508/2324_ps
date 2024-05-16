#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(vector<string> friends, vector<string> gifts) {
    
    // 선물 거래 명시 위한 2차원 배열 만들기 및 초기화
    int f_len = friends.size();
    int** arr;
    arr = new int*[f_len];
    for(int i = 0; i < f_len; i++){
        arr[i] = new int[f_len];
    }
    
    for (int j = 0; j < f_len; j++){
        for (int i = 0; i < f_len; i++){
            arr[j][i] = 0;
        }
    }
    
    // 2차원 배열에 선물 거래 수치화하여 집어넣기
    for (int i = 0; i < gifts.size(); i++){
        string str = gifts[i];
        int size_of_str = str.length();
        
        int split_index = str.find(" ");
        string giver = str.substr(0, split_index);
        string receiver = str.substr(split_index + 1, size_of_str - (split_index + 1));
        
        int giv_index = 0;
        int rec_index = 0;
        
        for (int j = 0; j < f_len; j++){
            if (friends[j] == giver){
                giv_index = j;
            }
            if (friends[j] == receiver){
                rec_index = j;
            }
        }
        arr[giv_index][rec_index] += 1;
    }
    
    // 선물 거래 보고 선물 지수 계산하기
    int* present_num;
    present_num = new int[f_len];
    for (int j = 0; j < f_len; j++){
        present_num[j] = 0;
    }
    for (int i = 0; i < f_len; i++){
        for (int j = 0; j < f_len; j++){
            present_num[i] += arr[i][j];
        }
        for (int j = 0; j < f_len; j++){
            present_num[i] -= arr[j][i];
        }
    }
    
    // 각 친구들이 선물을 받아야 하는지 여부를 계산
    int** pres_arr;
    pres_arr = new int*[f_len];
    for(int i = 0; i < f_len; i++){
        pres_arr[i] = new int[f_len];
    }
    
    for (int j = 0; j < f_len; j++){
        for (int i = 0; i < f_len; i++){
            pres_arr[j][i] = 0;
        }
    }
    for (int i = 0; i < f_len; i++){
        for (int j = 0; j < f_len; j++){
            if (i != j){
                if (arr[i][j] > arr[j][i]){
                    pres_arr[i][j] = 1;
                }
                else if (arr[i][j] < arr[j][i]){
                    pres_arr[i][j] = 0;
                }
                else{
                    if (present_num[i] > present_num[j]){
                        pres_arr[i][j] = 1;
                    }
                }
            }
        }
    }
    
    // 선물 받아야 하는지 여부 보고 각각 받는 총 선물 개수 계산하기
    int* total_rec_present_num;
    total_rec_present_num = new int[f_len];
    for (int j = 0; j < f_len; j++){
        total_rec_present_num[j] = 0;
    }
    for (int i = 0; i < f_len; i++){
        for (int j = 0; j < f_len; j++){
            total_rec_present_num[i] += pres_arr[i][j];
        }
    }
    
    int answer = 0;
    for (int i = 0; i < f_len; i++){
        if (total_rec_present_num[i] > answer){
            answer = total_rec_present_num[i];
        }
    }
    
    return answer;
}