# 根据dio号在网上进行pdf的下载
# 注意考虑搜索不到的情况
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import re
import os


# 根据dio号和下载到文件名为file_name的pdf，输出路径在output下
def downloadByDoi(doi, file_name):
    url = 'https://www.sci-hub.ren/' + doi
    html = askUrl(url)  # 得到html
    pdfUrl = parseHtml(html, file_name)
    downLoadPdf(pdfUrl, file_name)


def parseHtml(html, file_name):
    try:
        bs = BeautifulSoup(html, "html.parser")
        t_list = bs.select('#pdf')
        rePdfUrl = r'src="(.*?)"'
        pdfUrl = re.findall(rePdfUrl, str(t_list[0]))[0]
        return pdfUrl
    except:
        print("paper-->" + file_name + " not found!")
        with open("./not_found.txt", "a", encoding='utf-8') as f:
            f.write(file_name)
            f.write("\n")
        return None


def askUrl(url):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52',
        "Cookie": 'UM_distinctid=17a29eaff3f963-071e9fe5226b6-7a697d6e-144000-17a29eaff40fd; __gads=ID=3b7918afdf2b673c:T=1624200904:S=ALNI_MbaN4K1VfpLCOqpVRrExY11AKe_MA; _a_d3t6sf=dumciURjNgzwzSDQ5cNhTwWI; CNZZDATA1276057484=1027570305-1624198255-|1632096741'
    }
    DoiRequest = urllib.request.Request(url, headers=headers)
    html = ''
    try:
        response = urllib.request.urlopen(DoiRequest)
        html = response.read().decode('utf-8')
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    return html


def downLoadPdf(url, file_name):
    if url is not None:
        # <embed type="application/pdf" src="(.*?)" id="pdf"> 格式很多类似的 但是src和id是固定的
        rootPath = r"./output/"
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52',
            "Cookie": 'UM_distinctid=17a29eaff3f963-071e9fe5226b6-7a697d6e-144000-17a29eaff40fd; __gads=ID=3b7918afdf2b673c:T=1624200904:S=ALNI_MbaN4K1VfpLCOqpVRrExY11AKe_MA; _a_d3t6sf=dumciURjNgzwzSDQ5cNhTwWI; CNZZDATA1276057484=1027570305-1624198255-|1632096741'
        }
        try:
            DoiRequest = urllib.request.Request(url, headers=headers)
            response = urllib.request.urlopen(DoiRequest)
        except ValueError as e:
            if "unknown url type" in str(e):
                DoiRequest = urllib.request.Request("http:" + url, headers=headers)
                response = urllib.request.urlopen(DoiRequest)
        html = response.read()  # 这里别整utf-8转码
        # 命名不对 无法保持  有:不行
        file_name = file_name.replace(":", "")
        path_name = file_name[:file_name.rfind("/")]
        final_path_name = rootPath + path_name
        if not os.path.exists(final_path_name):
            if not os.path.exists(final_path_name[:final_path_name.rfind("/")]):
                os.mkdir(final_path_name[:final_path_name.rfind("/")])
            if not os.path.exists(final_path_name):
                os.mkdir(final_path_name)
        with open(rootPath + file_name + ".pdf", "wb") as f:
            # 写文件用bytes而不是str，所以要转码
            f.write(html)


#
if __name__ == '__main__':
    downloadByDoi("10.1109/tit.2014.2354403", "test/gg")
