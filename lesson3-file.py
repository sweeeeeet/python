import os.path as op
import os
#把目录下所有的文件路径都打印出来
my_path='d:/Tools'
for base_path,_,files in os.walk(my_path):
    for f in files:
        print(op.join(base_path,f))