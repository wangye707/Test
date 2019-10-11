#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 携程.py
# @Author: WangYe
# @Date  : 2019/9/4
# @Software: PyCharm
# num = int(input())
# list1 = []
# for i in range(num):
#     list1.append([float(i) for i in input().split(' ')])
# def go(list1):
#     zheng = []
#     fu = []
#     for i in list1:
#         if i[0] == 1:
#             zheng.append(i)
#         else:
#             fu.append(i)
#     M = len(zheng)
#     N = len(fu)
#     new_list = []
#     for i in range(len(zheng)):
#         for j in range(len(fu)):
#             if zheng[i][1] > fu[j][1]:
#                 new_list.append(1)
#             elif zheng[i][1] == fu[j][1]:
#                 new_list.append(0.5)
#             elif zheng[i][1] < fu[j][1]:
#                 new_list.append(0)
#     fenzi = 0
#     for i in new_list:
#         fenzi = fenzi + i
#     return fenzi/(M*N)
# go(list1)
'''
10
1 0.90
0 0.70
1 0.60
1 0.55
0 0.52
1 0.40
0 0.38
0 0.35
1 0.31
0 0.10
'''
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