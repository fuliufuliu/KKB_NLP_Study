import re
import jieba
from collections import Counter
import pandas as pd
# from functools import reduce
# from operator import add, mul
# import matplotlib.pyplot as plt
# import numpy
# import random

def defaultArticles():
    filename = "sqlResult_1558435.csv"
    content = pd.read_csv(filename, encoding='gb18030')
    articles = content['content'].tolist()
    return articles

class ProbabilitySelector:
    words = []
    word2s = []
    wordsCount: Counter = None
    word2Counter: Counter = None

    # articles 语料库，格式是 str[]
    def __init__(self, articles:[] = None, words:[] = None, word2s:[] = None):
        if articles != None :
            for i, article in enumerate(articles):
                if article != article:
                    continue
                self.words += jieba.cut(''.join(re.findall('\w+', article)))
                if i % 1000 == 0:
                    print(i)
            self.save(self.words, "words.txt")
            self.wordsCount = Counter(self.words)

            print("生成 WiWi+1 的词对数组。。。")
            self.word2s = ["".join(self.words[i:i + 2]) for i in range(len(self.words[0:-1]))]
            self.save(self.word2s, "word2s.txt")
            self.word2Counter = Counter(self.word2s)
            print("初始化完成！")
        elif words != None and word2s != None:
            self.words = words
            self.word2s = word2s
            self.wordsCount = Counter(words)
            self.word2Counter = Counter(word2s)
        else:
            print("初始化必须提供articles 或者 words, word2s")

    def save(self, wordList, fileName):
        with open(fileName, "w") as f:
            for a in wordList:
                f.write(a+"\n")

    def independentProb(self, word):
        return self.wordsCount[word] / len(self.words)

    # 出现 word2 后出现 word1的概率
    def conditionProb(self, word1, word2):
        ww = word1 + word2
        if ww in self.word2s:
            return self.word2Counter[''.join([word1, word2])] / self.wordsCount[word2]
        else:
            return 1 / len(self.word2s)

    def sentenceProb(self, sentence):
        prob = 1
        words = [w for w in jieba.cut(''.join(re.findall('\w+', sentence)))]
        for i, word in enumerate(words[:-1]):
            prob *= self.conditionProb(word, words[i+1])

        prob *= self.independentProb(words[-1])
        return prob
