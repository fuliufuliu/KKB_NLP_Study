import SyntaxTree
import ProbabilitySeletor
import os.path

# 我要讲一个故事/笑话，大家注意听，哎呀！不好意思，我放了一个P/我时间不够了/我要上班去了
myGammer = """
myGammer = 谁要干嘛 大家要干嘛 惊讶 道歉  说明原因
谁要干嘛 = 谁 要 干嘛（讲） ，
大家要干嘛 = 大家 干嘛（做） ，
惊讶 = 哎呀！ | 卧槽！ | 我买噶！ | 天哪！
道歉 = 司咪吗斯诶， | I  Am  Sorry！ | 不好意思， | 对不起，
说明原因 = 谁 怎么了
谁 = 你 | 我 | 他 | 我们 | 他们 | 你们 | 老师
干嘛（讲） = 干 几个  什么
干 = 讲 | 唱 | 念
几个 = 数字 量词
数字 = 一 | 二 | 三 | 四 |  
什么 = 故事 | 笑话 | 文章 | 歌
量词 = 个 | 首 | 篇
干嘛（做） = 注意听 | 举手 | 别打电话 | 别吃零食
怎么了 = 放了一个P | 时间不够了 | 要上班去了
"""


if __name__ == "__main__":
    if os.path.isfile("words.txt") and os.path.isfile("word2s.txt"):
        words = []
        word2s = []
        for i, line in enumerate((open("words.txt"))):
            words += line
        for i, line in enumerate((open("word2s.txt"))):
            word2s += line
        probabilitySeletor = ProbabilitySeletor.ProbabilitySelector(words=words, word2s=word2s)
    else:
        probabilitySeletor = ProbabilitySeletor.ProbabilitySelector(ProbabilitySeletor.defaultArticles())
    print(probabilitySeletor)

    print("\n", myGammer)

    grammer = SyntaxTree.createGrammer(myGammer, "=")
    for j in range(10):
        sentences = []
        maxI = 0
        maxProb = 0
        maxSentence = ""
        for i in range(20):
            sentence = SyntaxTree.generate(grammer, "myGammer")
            sentences.append(sentence)
            prob = probabilitySeletor.sentenceProb(sentence)
            print(" ---------", i, "  ", sentence,
                  "   Prob : ", prob)
            if prob > maxProb:
                maxI = i
                maxProb = prob
                maxSentence = sentence
        print(" 选择--》", maxI, " ", maxSentence, "   Prob : ", prob)