#!D:/workplace/python
# -*- coding: utf-8 -*-
# @File  : 111dasd.py
# @Author: WangYe
# @Date  : 2019/6/21
# @Software: PyCharm
'''
2019-06-21 07:13:19.599755: I tensorflow/core/platform/cpu_feature_guard.cc:140] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 AVX512F FMA
2019-06-21 07:13:19.808933: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1356] Found device 0 with properties:
name: Tesla P100-PCIE-16GB major: 6 minor: 0 memoryClockRate(GHz): 1.3285
pciBusID: 0000:18:00.0
totalMemory: 15.90GiB freeMemory: 15.61GiB
2019-06-21 07:13:19.808984: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1435] Adding visible gpu devices: 0
2019-06-21 07:13:20.105524: I tensorflow/core/common_runtime/gpu/gpu_device.cc:923] Device interconnect StreamExecutor with strength 1 edge matrix:
2019-06-21 07:13:20.105579: I tensorflow/core/common_runtime/gpu/gpu_device.cc:929]      0
2019-06-21 07:13:20.105587: I tensorflow/core/common_runtime/gpu/gpu_device.cc:942] 0:   N
2019-06-21 07:13:20.105868: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1053] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 15137 MB memory) -> physical GPU (device: 0, name: Tesla P100-PCIE-16GB, pci bus id: 0000:18:00.0, compute capability: 6.0)
ERROR:tensorflow:Exception in QueueRunner: Cannot assign a device for operation 'input_producer/input_producer/limit_epochs/CountUpTo': Could not satisfy explicit device specification '' because the node was colocated with a group of nodes that required incompatible device '/job:localhost/replica:0/task:0/device:GPU:0'
Colocation Debug Info:
Colocation group had the following types and devices:
CountUpTo: CPU
VariableV2: GPU CPU

Colocation members and user-requested devices:
  input_producer/input_producer/limit_epochs/epochs (VariableV2)
  input_producer/input_producer/limit_epochs/CountUpTo (CountUpTo)

  [[Node: input_producer/input_producer/limit_epochs/CountUpTo = CountUpTo[T=DT_INT64, _class=["loc:@input_producer/input_producer/limit_epochs/epochs"], limit=1](input_producer/input_producer/limit_epochs/epochs)]]
Exception in thread QueueRunnerThread-in

'''