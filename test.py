# -*- coding: utf-8 -*-
"""
@File    :  test.py
@Time    :  2022/12/21 21:53
@Author  :  changzheng
@Version :  1.0
@Desc    :  测试 随时可以删除
"""

import os

if __name__ == '__main__':
    # os.mkdir("./output/3. Signal Processing - Communication Centric/3.1 Standardized Waveform")
    a="./output/3. Signal Processing - Communication Centric/3.1 Standardized Waveform";
    print(a[:a.rfind("/")])
