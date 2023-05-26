'''
    1、读取word中的内容 用正则进行分词
    2、从论文搜索网站中找到对应的dio号
    3、用dio再向网页申请  下载所有的pdf

    attention：
    1.从word中读取之后格式的问题
    2.有些Online  得额外获取
    3.处理获取不到的情况
        3.1 dio号没有
        3.2 用dio搜索论文找不到结果
    4.考虑字符串超出最长长度之后如何进行优化

    遇到的一些注意事项：
    1.docx读取过慢--尝试换一种读取方式
'''

import getDioList
import downLoadByDoiAndSave
import getPaperTitleTxt


def downLoadFile(dio_list, file_name_list):
    # 这里匹配是个问题 注意之后验证
    for i in range(0, len(dioList)):
        print(dio_list[i], file_name_list[i])
        downLoadByDoiAndSave.downloadByDoi(dio_list[i], file_name_list[i])


if __name__ == '__main__':
    # 主文件
    nameList = getPaperTitleTxt.getFileName("txt/titleOutput.txt")
    dioList = getDioList.getDioList("./citations.ris")
    downLoadFile(dioList, nameList)
