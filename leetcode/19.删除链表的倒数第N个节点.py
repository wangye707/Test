#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 19.删除链表的倒数第N个节点.py
# @Author: WangYe
# @Date  : 2019/8/26
# @Software: PyCharm
def removeNthFromEnd(head, n) :
    a = head
    b = head

    for i in range(n):
        if a.next:
            a = a.next
        else:
            return head.next

    while a.next:
        a = a.next
        b = b.next
    b.next = b.next.next
    return head