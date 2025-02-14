from .task1 import kwargsAcceptFun
from .task2 import typeBasedTransformer
from .task3 import decorator_1

kwargsAcceptFun(num=1e6, str="Testing", arr=[1, 2, 3])



data = {
    "num": 1e6,
    "dec": 0.1+0.3,
    "str": "Testing",
    "flag": True,
    "arr": [1, 2, 3],
    "tpl": ("a", "b", "c"),
    "dict": {"a": 1, "b": 2},
    "set": {1, 2, 3},
}

print(typeBasedTransformer(**data))





@decorator_1
def factorial(n=10):
    ans=1
    for i in range(1,n): ans*=i
    return ans

factorial(50)
