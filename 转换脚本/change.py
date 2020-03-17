#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : change.py
# @Author: WangYe
# @Date  : 2020/1/30
# @Software: PyCharm
path = 'train.list'
new_path = 'train1.list'
with open(new_path,'w') as f1:
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            tl = line.split()
            train = tl[0].split('/')
            label = tl[0].split('/')
            label[0] = 'label'
            label[1] = 'label_' +label[1][-1]
            label[2] = label[2].replace('.jpg','.png')
            # print(train)
            train_str = ''
            for i in train:
                train_str +='/'
                train_str += i
            print(train_str[1:])
            # print(label)
            label_str = ''
            for k in label:
                label_str +='/'
                label_str+=k
            print(label_str[1:])
            f1.write(train_str[1:] + ' ' + label_str[1:] + '\n')
