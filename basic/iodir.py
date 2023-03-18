#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

# 创建目录test
os.mkdir("test")

# 将当前目录改为"/tmp/newdir"
os.chdir("/tmp/newdir")

# 给出当前的目录
print (os.getcwd())

# 删除”/tmp/test”目录
os.rmdir( "/tmp/test"  )