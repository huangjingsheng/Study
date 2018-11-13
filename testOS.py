import os

def test_path():
    # 获取当前工作目录路径
    s = os.getcwd()

    # 获取当前工作目录路径
    s1 = os.path.abspath('.')

    # 获取当前目录文件下的工作目录路径
    s2 = os.path.abspath('testOS.py')

    # 获取当前工作的父目录 ！注意是父目录路径
    s3 = os.path.abspath('..')

    # 获取当前工作目录路径
    s4 = os.path.abspath(os.curdir)
    print(s)
    print(s1)
    print(s2)
    print(s3)
    print(s4)
if __name__ == "__main__":
    test_path()