'''
    在线测试工具 https://regex101.com
    ?----0-1次 *---0-NAN次 +--1-NAN次 {a,b}--出现a-b次，不写为NAN
    匹配多个字符 (ab)+ 匹配ab出现1次以上
    a (cat|dog) 匹配a cat或者a dog
    [abc]+ 由abc构成的单词 (不要求顺序)
    [0-9] 数字 [^0-9]非数字
    \d  数字字符 \D 非数字字符
    \w  英文、数字、下划线 \W 非单词字符(前面那几个概念统称单词)
    \s  空白字符（包含Tab和换行） \S 非空白字符
    . 任意字符，不包换行符
    ^ 行首 $行尾
    贪婪匹配和懒惰匹配 前者尽可能匹配多  后者尽可能匹配少
    <.+> 贪婪匹配 会全部匹配
    <.+?> 懒惰匹配 这样才能匹配html标签
    \b 匹配字符边界
'''
import re

regex = r"DO  - ([\w|.].*)"

def getDioList(file):
    # 可以匹配到所有的dio号
    # 测试完成
    with open(file, 'r',encoding='utf-8') as f:
        content = f.read()
    dioList = re.findall(regex, content)
    return dioList
