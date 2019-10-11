#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 度小满.py
# @Author: WangYe
# @Date  : 2019/9/15
# @Software: PyCharm
s1 = [int(i) for i in input().split(' ')]
fin = s1[:2]
nums = s1[-1]
position = []
xt=[fin[0],0]
yt=[fin[1],0]
for i in range(nums):
    temp = [int(i) for i in input().split(' ')]
    xt.append(temp[0])
    yt.append(temp[1])
    position.append(temp)
# print(fin,position)
out = []
xtop = max(xt)
xdown = min(xt)
ytop = max(yt)
ydown = min(yt)
# print(xt,yt)
# print(xtop+2,xdown-2,ytop+2,ydown-2)
def go(x,y,bushu,went):
    p = [x,y]
    if (p in went) or(p in position)  or (x>(xtop+2)) or (x<(xdown-2)) or (y<(ydown-2)) or (y>(ytop+2)):
        # print(went)
        return False
    else:
        if [x,y] == fin:
            out.append(bushu)
            return True
        else:
            bushu = bushu + 1
            went.append([x,y])
            if go(x+1,y,bushu,went) or go(x,y+1,bushu+1,went) or go(x,y-1,bushu+1,went) or go(x-1,y,bushu+1,went):
                print(x,y)
                # return out
                return out
went = []
print(go(0,0,bushu=0,went=went))
'''
2 0 3
1 0
1 1
1 -1
'''

# bushu = bushu + 1
# went.append([x,y])
# if fin[0]>x:
# if [x+1, y + 1] not in position and [x, y + 1] not in went:
#     went.append([x+1, y])
#     return go(x+1,y,bushu,went) or go(x,y+1,bushu+1,went) or go(x,y-1,bushu+1,went) or go(x-1,y,bushu+1,went)
# # if fin[1]>y:
# #     return go(x+1,y,bushu,went) or go(x,y+1,bushu+1,went)  or go(x-1,y,bushu+1,went) or go(x,y-1,bushu+1,went)
# if [x,y+1] not in position and [x,y+1] not in went:
#     went.append([x,y+1])
#     return go(x,y+1,bushu+1,went)
# if [x,y-1] not in position and [x,y-1] not in went:
#     went.append([x,y-1])
#     return go(x,y-1,bushu+1,went)
# if [x-1,y] not in position and [x-1,y] not in went:
#     went.append([x-1,y])
#     return go(x-1,y,bushu+1,went)
# print(out)
# return out














#include<cstdio>
#include<cstring>
#include<algorithm>
# using namespace std;
# int w,h,sg[210][210];
# void get_sg(){
#     bool ext[50010];
#     for (int i=2;i<=200;i++)
#       for (int j=2;j<=200;j++){
#           memset(ext,false,sizeof(ext));
#           for (int k=2;k+k<=i;k++)//注意这里枚举的时候从2开始，因为1是初值
#               ext[sg[k][j]^sg[i-k][j]]=true;
#           for (int k=2;k+k<=j;k++)//注意循环退出的条件：再往后循环就重复了
#               ext[sg[i][k]^sg[i][j-k]]=true;
#           for (int k=0;;k++)
#             if (ext[k]==false){
#                 sg[i][j]=k;
#                 break;
#             }
#       }
#     return;
# }
# int main()
# {
#     get_sg();
#     while (scanf("%d%d",&w,&h)==2)
#       if (sg[w][h]==0)
#         printf("LOSE\n");
#       else printf("WIN\n");
#     return 0;
# }
#include<iostream>
#include<algorithm>
#include<cmath>
#include<map>
# using namespace std;
# int n,a,b,c,ans;
# void solve(int begin,int cost,vector<int> &x){
#     if (cost>=ans) return;
#     if (begin==n-1) {
#         if (cost<ans) ans=cost;
#         return;
#     }
#     solve(x[begin],cost+a;x);
#     if (x[begin]>0){
#         x[begin]--;
#         solve(x,cost+b;x);
#         x[begin]++;
#     }
#     if (x[begin]<n-1){
#         x[begin]++;
#         solve(x,cost+c;x);
#         x[begin]--;
#     }
# }
# int main(){
#     cin>>n>>a>>b>>c;
#     ans=min(n*c+a,n*b+a);
#     vector<int> x(n);
#     for (int i=0;i<n;i++)
#         cin>>x[i];
#     solve(0,0,x);
#     cout<<ans;
# }
