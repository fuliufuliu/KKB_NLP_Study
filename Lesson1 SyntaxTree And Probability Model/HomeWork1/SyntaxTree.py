import random

simpleGrammar = """
sentence => noun_phrase verb_phrase
noun_phrase => Article adj* noun
adj* => null | adj | adj adj*
verb_phrase => verb noun_phrase
Article => 一个 | 这个
noun => 女人 | 篮球 | 桌子 | 小猫
verb => 看着 | 坐在 | 听着 | 看见
adj => 蓝色的 | 好看的 | 小小的
"""

adjGrammer = """
adj* => null | adj | adj adj*
adj => 蓝色的 | 好看的 | 小小的
"""

def createGrammer(grammerStr: str, nodeContentSplit="=>", lineSplit="\n"):
    grammer = {}
    lines = grammerStr.split(lineSplit)
    for line in lines:
        if line.strip() == "": continue
        nodeAndContent = line.split(nodeContentSplit)
        grammer[nodeAndContent[0].strip()] = [item.split() for item in nodeAndContent[1].split("|")]
    return grammer


"""
{'sentence': [['noun_phrase', 'verb_phrase']], 
'noun_phrase': [['Article', 'adj*', 'noun']],
 'adj*': [['null'], ['adj'], ['adj', 'adj*']], 
 'verb_phrase': [['verb', 'noun_phrase']], 
 'Article': [['一个'], ['这个']], 
 'noun': [['女人'], ['篮球'], ['桌子'], ['小猫']], 
 'verb': [['看着'], ['坐在'], ['听着'], ['看见']], 
 'adj': [['蓝色的'], ['好看的'], ['小小的']]}
"""

host = """
host = 寒暄 报数 询问 业务相关 结尾 
报数 = 我是 数字 号 ,
数字 = 单个数字 | 数字 单个数字 
单个数字 = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
寒暄 = 称谓 打招呼 | 打招呼
称谓 = 人称 ,
人称 = 先生 | 女士 | 小朋友
打招呼 = 你好 | 您好 
询问 = 请问你要 | 您需要
业务相关 = 玩玩 具体业务
玩玩 = null
具体业务 = 喝酒 | 打牌 | 打猎 | 赌博
结尾 = 吗？
"""

def generate(gram, target):
    if target not in gram: return target

    expaned = []
    for t in random.choice(gram[target]):
        # print(gram[target], t)
        expaned.append(generate(gram, t))
    return ''.join(["\n" if e == "/N" else e for e in expaned if e != 'null'])


simpel_programming = '''
programming => if_stmt | assign | while_loop
while_loop => while ( cond ) { change_line stmt change_line }
if_stmt => if ( cond )  { change_line stmt change_line } | if ( cond )  { change_line stmt change_line } else { change_line stmt change_line } 
change_line => /N
cond => var op var
op => | == | < | >= | <= | >
stmt => assign | if_stmt
assign => var = var
var =>  var _ num | words 
words => words _ word | word 
word => name | info |  student | lib | database 
nums => nums num | num
num => 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0
'''



if __name__ == "__main__":
    grammer = createGrammer(simpleGrammar)
    print(grammer)
    print(generate(gram=grammer, target='sentence'))
    for i in range(20):
        print(generate(gram=createGrammer(host, "="), target='host'))
    print(generate(gram=createGrammer(simpel_programming, "=>"), target='programming'))