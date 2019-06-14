#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 矩阵裁剪.py
# @Author: WangYe
# @Date  : 2019/3/8
# @Software: PyCharm
import numpy as np
import tensorflow as tf

# x =[[[1,1],[1,1]],[[1,1],[1,1]],[[1,1],[1,1]]]
# x = np.asarray(x)
# matrix_pad = np.pad(x,pad_width=((1, 2),#向上填充1个维度，向下填充两个维度
#                                  (2, 1),#向左填充2个维度，向右填充一个维度
#                                  (0,0)) #通道数不填充
#                     ,mode="constant",#填充模式
#                     constant_values=(6, 5)  #第一个维度（就是向上和向左）填充6，第二个维度（向下和向右）填充5
#                     )
# print(matrix_pad)



a = [[[[1,2,3],
     [1,2,3],
     [1,2,3]],[[1,2,3],
     [1,2,3],
     [1,2,3]]],[[[1,2,3],
     [1,2,3],
     [1,2,3]],[[1,2,3],
     [1,2,3],
     [1,2,3]]]]
a1 = np.array(a)
#a1 = a
b = [[1,2,3],
     [1,2,3]]
c = [[1,2],
     [1,2],[1,2]]

d = [[[1,1],
     [1,1],[1,1]],
     [[2, 2],
      [2, 2], [2, 2],],[[1,2],
     [1,2],[1,2]]
     ]
e = [[1],[2],[1]]  #  3*1的矩阵
e1 = [[1],[2],[1]]
e2 = [[1],[2],[1]]
q = np.asarray(e)
# q1 = np.asarray(e1)
# q2 = np.asarray(e2)

w = e+e1+e2
w1 = np.array(w)
print(w1.shape)



# dx = np.asarray(c)
# # q = np.reshape(dx,(3,2,1))
# print(dx[1:2])
# print(dx.shape)


# dx = dx.reshape(3,2,1)
# print(dx)
# print(dx.shape)
# dq = np.asarray([dx[0]])
# print(dq.shape)
# print(dx[2])
# cx =np.ravel(c)
# cw = np.reshape(a,(3,1,2))
# print(cx)

# d = tf.constant([[1,2,3],
#      [1,2,3]],tf.float64)
# e = tf.constant([[1,2,3],
#      [1,2,3]],tf.float64)
#
# print(d)
# print(e)
# with tf.Session() as sess:
#      # dis1 = sess.run(tf.square(e-d))
#      # dis2 = sess.run(tf.reduce_sum(dis1))#
#      dis = sess.run(tf.sqrt(tf.reduce_sum(tf.square(d-e), 2)))
#      # dis3 = sess.run(tf.sqrt(dis2))#
#      #print(dis1,"++++++",dis2,"+++++",dis3)
#      print(dis)



# b1 = np.array(b)
# c1 = np.array(c)
# print(c1.shape)
# c2 = np.pad(c1,pad_width=((0,0),(1,0)),mode="constant",constant_values=(0,0))
# #                       行填充    列填充
#
# # c2 = np.pad(c1,pad_width=((0,0),(1,0)),mode="reflect",constant_values=(0,0))
# print(c2)
# print(c2.shape)
# print(type(b1))#<class 'numpy.ndarray'>
# print(b1.shape)#(2, 3)
# x1 = b1.shape
# x2 = c1.shape
# # print(type(x1))#<class 'tuple'>
# temp = []
# temp.append(x1[0])
# temp.append(x2[1])
# print(max(temp))




# print(a1.shape)
# print(a1[2:2])
# print(a1[2:2].shape)
