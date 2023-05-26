# import pdfkit
# 这个方法可以将网页保存成pdf格式
# path_wk = r'D:\programe\environment\Python\pycharm\Plugins\wkhtmltopdf\bin\wkhtmltopdf.exe'
# config = pdfkit.configuration(wkhtmltopdf=path_wk)
# url = "https://moscow.bban.top/2506/a55d125e543234542dbed0a563e81e41/poffenbarger1976.pdf#navpanes=0&view=FitH"
# url2="www.baidu.com"
# pdfkit.from_url(url, './test.pdf', configuration=config)
import re


def getTitle(input_str):
    # 根据输入的字符串获取名字
    # 只获取非书籍和非online的参考资料
    # todo： 处理online的情况
    numRe = r'(\[\d+\])'
    titleRe = r"[“|\"]{1}([\w| |\-|:|,]+),[”|\"]{1}"
    OnlineRe = r"\[Online\].*Available:(.*)"
    numListLen = len(re.findall(titleRe, input_str))
    titleListLen = len(re.findall(numRe, input_str))
    OnlineListLen = len(re.findall(OnlineRe, input_str))
    if numListLen == 1 and titleListLen == 1 and OnlineListLen == 0:
        return re.findall(numRe, input_str)[0] + re.findall(titleRe, input_str)[0]
    elif OnlineListLen == 1:
        return 
    return None


# 获取搜索名称和文件名称
def getFileNameAndSearchName(file):
    nameList = []
    searchList = []
    with open(file, 'rb') as f:
        content = f.read()
    unProcessNameList = content.decode('utf-8').split("\r\n")
    for item in unProcessNameList:
        name = getTitle(item)
        if name is not None:
            nameList.append(name)
            searchList.append(item)
    return nameList, searchList


# 返回名称
def getFileName(file):
    nameList = []
    with open(file, 'rb') as f:
        content = f.read()
    NameListTxt = content.decode('utf-8').split("\r\n")
    for item in NameListTxt:
        if item is not None:
            nameList.append(item)
    return nameList


def writeTxtByNameList(name_list, filename):
    with open(filename, 'w') as f:
        for item in name_list:
            f.write(item)
            f.write("\n")
    print("写入完成....")


if __name__ == '__main__':
    nameList, searchList = getFileNameAndSearchName("txt/paperTitle.txt")
    writeTxtByNameList(nameList, "txt/titleOutput.txt")
    writeTxtByNameList(searchList, "txt/SearchOutput.txt")
