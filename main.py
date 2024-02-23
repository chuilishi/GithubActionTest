# 打开cache/test.txt 如果存在则打印exist,不存在则打印not exist 并且创建
import os
path = './cache/test.txt'
# get current directory
print(os.getcwd())
if os.path.exists(path):
    print('exist')
else:
    print('not exist')
    with open(path, 'w') as f:
        f.write('test')
