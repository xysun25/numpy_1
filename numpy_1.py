# numpy创建数组，数据类型
import random

import numpy as np
t1 = np.array([1,2,3,4,5])
print(t1)
# a.dtype 输出numpy中的数据类型
print(t1.dtype)

# type() 输出数组的类名
print(type(t1))

t2 = np.array(range(10))
print(t2)
print(t2.dtype)
print(type(t2))

t3 = np.array(range(1,10))
print(t3)
print(t3.dtype)
print(type(t3))

t4 = np.arange(1,6)
print(t4)
print(t4.dtype)
print(type(t4))

# 输出4到15，每隔2个步长
t5 = np.arange(4,15,2)
print(t5)
print(t5.dtype)
print(type(t5))
print("*"*100)

# 修改数据类型 float
t6 = np.array(range(1,4),dtype=float)
print(t6)
print(t6.dtype)
print(type(t6))

# 数据类型 int8
t7 = np.array(range(1,4),dtype="i1")
print(t7)
print(t7.dtype)
print(type(t7))
print("*"*100)

# 数据类型 bool
t8 = np.array([1,1,0,1,0,0],dtype=bool)
print(t8)
print(t8.dtype)
print(type(t8))
print("*"*100)

# numpy 中的小数
t9 = np.array([random.random() for i in range(10)])
print(t9)
print(t9.dtype)

# round取t9小数点后两位
t10 = np.round(t9,2)
print(t10)