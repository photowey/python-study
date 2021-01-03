# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file Annotation.py
# @description Annotation
# @author WcJun
# @date 2020/07/02
# ---------------------------------------------


def around_logger(fn):
    def inner(*args, **kwargs):
        print("--- the log pre log ---")
        fn(*args, **kwargs)
        print("--- the log post ---")

    return inner


@around_logger
def useful(a, b):
    print(a * b)


if __name__ == "__main__":
    useful(2, 5)
