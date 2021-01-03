# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file File.py
# @description File
# @author WcJun
# @date 2020/06/20
# ---------------------------------------------
from typing import List

import pandas as pd

RESOURCE_FILE = "../../resources"


def full_path(file: str) -> str:
    return RESOURCE_FILE + file


def read_file(file_path: str) -> str:
    """
    Returns the context of file,by segmented reading
    :param file_path: the target file path
    :return: the file content
    """
    with open(file_path, mode="r", encoding="utf-8") as target:
        length: int = 128
        loop: bool = True
        file_context: str = ""
        while loop:
            try:
                context = target.read(length)
                if not context:
                    break
                file_context += context
            except StopIteration:
                loop = False
                print("Iteration is stopped.")

        return file_context


# 读
f = open(RESOURCE_FILE + "/Hello.txt", encoding="utf-8")
words = f.read()
print(words)
f.close()

# 写
f = open(RESOURCE_FILE + "/Write.txt", mode="w", encoding="utf-8")
f.write("""床前明月光，
疑是地上霜。
""")
f.write("""举头望明月，
低头思故乡。
""")
f.close()

if __name__ == "__main__":
    text = read_file(full_path("/Text.txt"))
    print(text)
