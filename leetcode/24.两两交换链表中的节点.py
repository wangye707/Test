#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 24.两两交换链表中的节点.py
# @Author: WangYe
# @Date  : 2019/8/27
# @Software: PyCharm
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        p = head
        while head or head.next:
            temp = head.next
            head = head.next.next
            head = head.next
            head.next = temp
            head = head.next
        return p
