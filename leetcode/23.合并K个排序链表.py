#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 23.合并K个排序链表.py
# @Author: WangYe
# @Date  : 2019/8/27
# @Software: PyCharm
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next
