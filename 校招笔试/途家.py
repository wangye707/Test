#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 途家.py
# @Author: WangYe
# @Date  : 2019/9/6
# @Software: PyCharm
import numpy as np
def bag_for_wy(bag_weight_list, bag_for_value, weight_most):  # 返回最大价值
    num = len(bag_weight_list)
    #创建全零矩阵
    bag_weight_list.insert(0, 0)
    bag_for_value.insert(0, 0)
    bag_arr = np.zeros((num + 1, weight_most + 1), dtype=np.int32)  # 现在我们开始进填充，从00开始
    for i in range(1, num + 1):
        for j in range(1, weight_most + 1):
            if bag_weight_list[i] <= j:
                bag_arr[i][j] = max(bag_arr[i - 1][j - bag_weight_list[i]] + bag_for_value[i], bag_arr[i - 1][j])
            else:
                bag_arr[i][j] = bag_arr[i - 1][j]
    # print(bag_arr)
    return bag_arr[-1, -1]

if __name__ == '__main__':

    s = input().split(' ')
    n = int(s[0])
    weight = int(s[1])
    v = []
    w = []

    for i in range(n):
        temp = input().split(' ')
        w.append(int(temp[0]))
        v.append(int(temp[1]))
    result = bag_for_wy(w, v, weight)
    print(result)
    # weight = [2, 2, 6, 5, 4]
    # value = [3, 6, 5, 4, 6]
    # weight_most = 10

'''
#include<iostream>
#include<vector>
#include<string>
using namespace std;
int main(){
    string a;
    int b;
    cin>>a>>b;
    int max,begin=0,tag;
    while(b){
        max=-1;
        for (int i=begin;i<a.length()&&i<=begin+b;++i){
            if (a[i]>max){
                max=a[i];
                tag=i;
            }
        }
        b-=tag-begin;
        a.erase(a.begin()+begin,a.begin()+tag);
        ++begin;
    }
    cout<<a;
}


'''