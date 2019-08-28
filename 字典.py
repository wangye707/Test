#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 字典.py
# @Author: WangYe
# @Date  : 2019/8/12
# @Software: PyCharm
d = {}
d.update({'a':10})
d['b']=4
print(d)
math_score = {'Nelly': 89}         #创建一个班级数学成绩字典 math

math_score['Baade'] = 77                       #新增一个键值对 'Baade': 77
print(math_score)                              #{'Madonna': 89, 'Cory': 99, 'Annie': 65, 'Nelly': 89, 'Baade': 77}
import java.util.Scanner;
public class Main8 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String str = input.nextLine();
        String[] strs = str.split(",");
        mySort(strs);
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<strs.length;i++){
            sb.append(strs[i]);
            sb.append(",");
        }
        String res = sb.substring(0,sb.length()-1);
        System.out.println(res);
    }
    public static void mySort(String[] arr)
    {
        for (int pass = 1; pass < arr.length; pass++)
        {
            int largestPos = findLargest(arr, arr.length - pass);
            if (largestPos != arr.length - pass)
            {
                swap(arr, largestPos, arr.length - pass);
            }
        }
    }
    public static int findLargest(String[] arr, int num)
    {
        int largestPos = 0;
        for (int i = 1; i <= num; i++)
        {
            if (arr[i].compareToIgnoreCase(arr[largestPos]) <= 0)
            {
                largestPos = i;
            }
        }
        return largestPos;
    }
    public static void swap(String[] arr, int first, int second)
    {
        String temp = arr[first];
        arr[first] = arr[second];
        arr[second] = temp;
    }
}
