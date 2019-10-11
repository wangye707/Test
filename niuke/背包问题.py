#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 背包问题.py
# @Author: WangYe
# @Date  : 2019/7/8
# @Software: PyCharm
# import numpy as np
#
# def solve(vlist,wlist,totalWeight,totalLength):
#     resArr = np.zeros((totalLength+1,totalWeight+1),dtype=np.int32)
#     # print(resArr)
#     for i in range(1,totalLength+1): #物品数量
#         for j in range(1,totalWeight+1): #背包重量
#             if wlist[i] <= j:
#                 resArr[i,j] = max(resArr[i-1,j-wlist[i]]+vlist[i],resArr[i-1,j])
#             else:                   #   重量差的价值定位
#                 resArr[i,j] = resArr[i-1,j]
#     return resArr[-1][-1]
import numpy as np

def solve(vlist,wlist,totalWeight,totalLength):
    resArr = np.zeros((totalLength+1,totalWeight+1),dtype=np.int32)
    # print(resArr)
    for i in range(1,totalLength+1): #物品数量
        for j in range(1,totalWeight+1): #背包重量
            if wlist[i] <= j:
                resArr[i,j] = max(resArr[i-1,j-wlist[i]]+vlist[i],resArr[i-1,j])
            else:                   #   重量差的价值定位
                resArr[i,j] = resArr[i-1,j]
    return resArr[-1][-1]

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
    # print(v,w,weight,n)
    # v = [1,4,9]
    # w = [9,2,1]
    # weight = 10
    # n =2
    # v = [3,6,5,4,6]
    # w = [2,2,6,5,4]
    # weight = 10
    # n = 4
    result = solve(v,w,weight,n-1)
    print(result)

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
    # print(v,w,weight,n)
    # v = [1,4,9]
    # w = [9,2,1]
    # weight = 10
    # n =2
    # v = [3,6,5,4,6]
    # w = [2,2,6,5,4]
    # weight = 10
    # n = 4
    result = solve(v,w,weight,n-1)
    print(result)
    '''
    3 10
    9 1
    2 4
    1 9
    '''
'''
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
'''