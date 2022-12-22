# -*- coding: utf-8 -*-
"""
@File    :  downLoadPaper.py
@Time    :  2022/12/21 19:41
@Author  :  changzheng
@Version :  1.0
@Desc    :  根据data_after_process.txt文件进行论文的下载
"""
import downLoadByDoiAndSave
import re
import getDioList

if __name__ == '__main__':
    file = './data_after_process.txt'
    with open(file, 'rb') as f:
        content = f.read()
    fileOrTitles = content.decode('utf-8').split("\r\n")

    fileOrTitles = fileOrTitles[:-1]
    dioList = getDioList.getDioList("./result.html")
    fileIndex = 38
    if len(dioList) != 190:
        print("dio缺失,dio数量---" + str(len(dioList)))
        exit(0)
    dioList = dioList[38:]
    fileOrTitles = fileOrTitles[fileOrTitles.index(
        "[1]IEEE 802.11ad-Based Radar: An Approach to Joint Vehicular Communication-Radar System.") - 2:]
    index = 0
    filename = ""
    threeTitleReg = r'^(\d\.\d)'
    for fileOrTitle in fileOrTitles:
        if fileOrTitle.startswith("file:"):
            if len(re.findall(threeTitleReg, fileOrTitle.split(":")[1])) == 0:
                filename = ""
            if len(re.findall(threeTitleReg, fileOrTitle.split(":")[1])) == 1:
                filename = filename[:filename.index("/") + 1]
            filename = filename + fileOrTitle.split(":")[1].strip() + "/"
            print("filename " + filename)
        else:
            tmpFile = filename + fileOrTitle
            print("tmpFile-->", tmpFile)
            # if tmpFile.find(
            #         "[1]IEEE 802.11ad-Based Radar: An Approach to Joint Vehicular Communication-Radar System.") != -1:
            #     print(index)
            downLoadByDoiAndSave.downloadByDoi(dioList[index], tmpFile)
            index = index + 1
    print("final index -- " + str(index))
    print(len(dioList))
