#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 链表逆序.py
# @Author: WangYe
# @Date  : 2019/7/10
# @Software: PyCharm
class LNode:
    def __init__(self,x=None):
        self.data=x
        self.next=None

def Reverse(head):
    if head == None or head.next == None:
        return
    pre = None #前驱节点
    cur = None#当前节点
    next = None#后继节点
    #把链表首节点变为尾节点
    cur = head.next
    # print(cur.data)
    # next = cur.next
    # # print(next)
    # # cur.next = None
    # pre = cur
    # cur =next
    # print(cur.data)
    #使当前遍历节点cur指向前驱节点
    while cur.next != None:
        next = cur.next
        print('1',cur.data)
        # print('next',next.data)
        cur.next = pre

        pre = cur
        print('2', pre.data)
        cur = next
        print('3', cur.data)
    #遍历到链表最后一个节点时候，将其指向前驱节点
    cur.next = pre
    #头节点指向原来链表的最后一个节点
    head.next = cur

if __name__ == "__main__":

    i = 1
    #链表的头结点
    head = LNode()
    cur = head
    #构造单链表
    while i<8:
        tmp = LNode(i)
        cur.next = tmp
        cur = tmp
        i += 1

    # print("原链表：")
    cur = head.next
    while cur != None:
        # print(cur.data)
        cur= cur.next
    # print("\n逆序后：")
    Reverse(head)
    cur = head.next
    while cur != None:
        # print(cur.data)
        cur = cur.next