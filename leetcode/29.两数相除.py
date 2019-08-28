#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 29.两数相除.py
# @Author: WangYe
# @Date  : 2019/8/28
# @Software: PyCharm


def divide(dividend, divisor):
    jianshu = dividend
    beijianshu = divisor
    i = 0
    if dividend == 0:
        return 0
    if (dividend > 0 and divisor > 0):
        # if dividend < 0:
        if divisor == 1:
            return min(2**31 - 1,dividend)

        if divisor < dividend:
            while divisor <= dividend:
                divisor += beijianshu
                i = i + 1
                #print(i)#
            return min(2**31 - 1,i)
        elif dividend == divisor:
            return 1
        else:
            return 0
    if (dividend < 0 and divisor < 0):
        dividend1 = dividend * -1
        divisort1 = divisor * -1
        jianshu1 = dividend1
        beijianshu1 = divisort1
        #print(divisort)
        if divisort1 == 1:
            return min(2**31 - 1,dividend1)
        if divisort1 < dividend1:
            while divisort1 <= dividend1:
                divisort1 += beijianshu1
                i = i + 1
                #print(i)#
            return i
        elif dividend1 == divisort1:
            return 1
        else:
            return 0
    if (dividend < 0 and divisor > 0):
        dividend1 = dividend * -1
        divisort1 = divisor
        jianshu1 = dividend1
        beijianshu1 = divisort1
        # print(divisort)
        if divisort1 == 1:
            return dividend1 * -1
        if divisort1 < dividend1:
            while divisort1 <= dividend1:
                divisort1 += beijianshu1
                i = i + 1
                # print(i)#
            return i * -1
        elif dividend1 == divisort1:
            return -1
        else:
            return 0
    if (dividend > 0 and divisor < 0):
        dividend1 = dividend
        divisort1 = divisor * -1
        jianshu1 = dividend1
        beijianshu1 = divisort1
        # print(divisort)
        if divisort1 == 1:
            return dividend1*-1
        if divisort1 < dividend1:
            while divisort1 <= dividend1:
                divisort1 += beijianshu1
                i = i + 1
                # print(i)#
            return i * -1
        elif dividend1 == divisort1:
            return -1
        else:
            return 0

print(divide(-2147483648,-2))

