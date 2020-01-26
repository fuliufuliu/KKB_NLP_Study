from sklearn.linear_model import LinearRegression
from matplotlib import pyplot

pyplot.plot()

class TestClass:
    a:int = 5
    dic = {}
    def __init__(self):
        self.a = 6
        self.dic = {}


A = TestClass()
B = TestClass()
A.a = 10
A.dic[1] = '123'
B.dic[1] = '333'
print(A.dic )
print(B.dic )

