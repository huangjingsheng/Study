import re
import json
def ergdic():
    emp = {'name': 'Tom', 'age': 20, 'salary': 8800.00}
    a = type(emp)
    print(a)
    for k in emp.keys():
        print(k)

def testFor():
    i = 1
    for i in  range(10):
        if i == 5:
            continue
        if i == 8:
            break
        print(i)
def testTry():
    a = 5
    b = 0
    try:
        c = a/b
    except:
        print("aaaa")

def testAdd():
    a = 0
    b = 10
    if a :
        print(a)

    if b :
        print(b)

    if a or b :
        print("TRUE")

    a += 1
    print(a)


if __name__ == '__main__':
    ergdic()