#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 携程旅行问题.py
# @Author: WangYe
# @Date  : 2019/9/4
# @Software: PyCharm
'''
4
6
0 1 4
0 2 3
0 3 1
1 2 1
1 3 2
2 3 5
'''
import itertools
position = int(input())
luxian = int(input())
list1 = []
for i in  range(luxian):
    list1.append([int(i) for i in input().split(' ')])
du = []
for i in list1:
    du.append(i[0])
    du.append(i[1])
du =set(du)

def t1(i,j):
    for m in list1:
        #
        if m[:2] ==[i,j] or m[:2] ==[j,i]:
            # print(m[:2])
            return m[-1]
    return 9999
def go(list1):
    # # print(du)
    # if len(gone) == len(du):
    #     t = t + t1(gone[-1], 0)
    #     return t
    # for i in du:
    #     if i not in gone:
    #         gone.append(i)
    #         t = t + t1(gone[-1],gone[-2])
    #         return go(list1,gone,t)
    pailie = []
    for i in du:
        if i!=0:
            pailie.append(i)
    p = (list(itertools.permutations(pailie)))
    timee = []
    for i in p:
        tt = 0
        for j in range(len(i)-1):
            list(i)
            tt = tt + t1(i[j],i[j+1])
        timee.append(tt)
    return max(timee)



# time = 0
# gone = [0]
print(go(list1))
#include<iostream>
#include<string.h>
#include<vector>
#include<map>


# 阿贵代码
# using namespace std;
# int main(){
#     //19：38
#     string s;
#     cin>>s;
#     vector<int> ans;
#     int end=0,tem,begin=0;
#     for (int i=0;i<s.length();++i){
#         for (tem=s.length()-1;tem>end&&s[tem]!=s[i];--tem);
#         end=tem;
#         if (i==end){
#             ans.push_back(end-begin+1);
#             begin=end+1;
#             end+=1;
#         }
#     }
#     int i;
#     for (i=0;i<ans.size()-1;++i) cout<<ans[i]<<',';
#     cout<<ans[i];
# }