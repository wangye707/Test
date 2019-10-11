#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 依图.py
# @Author: WangYe
# @Date  : 2019/9/6
# @Software: PyCharm
'''
10
0 0 1 0 0 0 0 1 0 0
3
'''
# num = int(input())
# list1 = [int(i) for i in input().split(' ')]
# def go():
#     k= 0
#     for i in range(num):
#         if i == 0 :
#             if list1[i] ==0 and list1[i+1] == 0:
#                 list1[i] = 1
#                 k = k + 1
#                 continue
#             else:
#                 continue
#         if i == num-1:
#             if list1[i] ==0 and list1[i-1] == 0:
#                 list1[i] = 1
#                 k = k + 1
#                 continue
#         if list1[i] ==0 and list1[i-1] == 0 and list1[i+1] == 0:
#             list1[i] = 1
#             k = k + 1
#             continue
#     return k
# print(go())
'''
5 4
1 2 1 4 1
1 1 1 1 3
2 4 1 2 3
2 5 1 3 2
5 2 1 5 5
1 2
1 3
1 5
3 4
'''
# s = input().split(' ')
# n = int(s[0])
# m = int(s[1])
# arr = []
# clik = []
# for i in range(n):
#     arr.append([int(i) for i in input().split(' ')])
# for i in range(m):
#     clik.append([int(i) for i in input().split(' ')])
def weight(list1):
    hh = len(list1)  #竖向遍历
    # l = len(list1[0])  #长
    tiao = 0
    for i in range(hh):
        temp = []
        for j in range(hh):  #下落
            # print(j,i,list1[j][i])
            if list1[j][i] == '*':
                continue
            else:
                temp.append(list1[j][i])
        if len(temp) !=0:
           # tiao = tiao +1
            for k in range(hh):
                if k < len(temp):
                    list1[(k+1)*-1][i] = temp[k]
                    # list1[k][i] = '*'
                else:
                    list1[(k+1)*-1][i] = '*'
                    # list1[k][i] = '*'
    return list1
def left(list1):
    hh = len(list1)
    tiao = 0
    for i in range(hh):
        temp = []
        for j in range(hh):
            if list1[j][i] == '*':
                continue
            else:
                temp.append(list1[j][i])
        if len(temp) == 0:
            for j in range(hh):
               del list1[j][i]
               list1[j].append('*')
               #  list1[j][i] = list1[j][i+1]
    return list1


        # print(list1)
        # else:
        #     for j in range(hh):  # 下落
        #         del list1[j][i]

    # return list1
li = [[1,'*',1],['*','*',1],['*','*',1]]
# print(weight(li))
def do(list1,click):
    i = click[0]-1
    j = len(list1)+1-click[1]
    tar = list1[i][j]
    for i

print(left(weight(li)))
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
}

'''


