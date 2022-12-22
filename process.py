# -*- coding: utf-8 -*-
"""
@File    :  process.py
@Time    :  2022/12/21 19:03
@Author  :  changzheng
@Version :  1.0
@Desc    :  处理最新的data.txt文件
"""
import re

if __name__ == '__main__':
    file = "./data.txt"
    with open(file, 'rb') as f:
        content = f.read()
    unProcessNameList = content.decode('utf-8').split("\r\n")
    # 处理空行
    afterProcessEmptyLine = []
    for data in unProcessNameList:
        if len(data.strip()) != 0:
            afterProcessEmptyLine.append(data.strip())
    titleTwoRe = r'^#{2} \[(.*)\]'
    titleThreeRe = r'^#{3} \[(.*)\]'
    paperTitleRe = r'\d{1,2}\. \*\*(.*)\*\*'
    paperIndex = 1
    with open("./data_after_process.txt", 'w', encoding='utf-8') as file:
        for line in afterProcessEmptyLine:
            titleOne = re.findall(titleTwoRe, line)
            titleTwo = re.findall(titleThreeRe, line)
            paperTitle = re.findall(paperTitleRe, line)
            if len(titleOne) > 0:
                print("file:" + titleOne[0])
                file.write("file:" + titleOne[0])
                file.write("\n")
                paperIndex = 1
            if len(titleTwo) > 0:
                print("file:" + titleTwo[0])
                file.write("file:" + titleTwo[0])
                file.write("\n")
                paperIndex = 1
            if len(paperTitle) > 0:
                print('[' + str(paperIndex) + ']' + paperTitle[0])
                file.write('[' + str(paperIndex) + ']' + paperTitle[0])
                file.write("\n")
                paperIndex = paperIndex + 1
    with open("./data_after_process_title.txt", 'w', encoding='utf-8') as file:
        for line in afterProcessEmptyLine:
            paperTitle = re.findall(paperTitleRe, line)
            if len(paperTitle) > 0:
                file.write(paperTitle[0])
                file.write("\n")
                paperIndex = paperIndex + 1
