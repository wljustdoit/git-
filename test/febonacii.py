#!/usr/bin/env python
# coding=utf-8
import time 
import threading

def febonacii(num):
    a = 0
    b = 1
    current_index = 0
    while current_index < num :
        yield a
        a, b = b , a + b
        current_index += 1


def main():
    try:
        num1 = int(input("请输入数字"))
        result = febonacii(num1)
        for value in result:
            print(value)
    except EXCEPTION as e:
        print(e)
    finally:
        print("byebye")
        return


if __name__ == "__main__":
        main()
