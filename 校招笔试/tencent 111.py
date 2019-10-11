#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : tencent 111.py
# @Author: WangYe
# @Date  : 2019/9/1
# @Software: PyCharm
#include<iostream>
#include<string.h>
#include<vector>
#include<map>
using namespace std;
int main(){
    int t,k;
    //int a[100][100000];
    cin>>t>>k;
    int i,j,sum;
    for (i=0;i<t;++i){
        int a,b;
        cin>>a>>b;
        //cout<<a<<b<<endl;
        sum=0;
        for (j=a;j<=b;++j){
            if (j<k) {
                ++sum;
                continue;
            }
            else{
                sum+=1;
                for (int x=k;x<=j;x+=k)
                    sum+=j+1-x;
            }
        }
        cout<<sum<<endl;
    }
}