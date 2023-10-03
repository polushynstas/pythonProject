class MyStr(str):
    def __init__(self, value):
        super().__init__()

    def __add__(self, other):
        return MyStr(str(self) + str(other))

    def __sub__(self, other):
        if other is None:
            return self.replace('None', '')
        elif isinstance(other, str):
            return self.replace(other, '', 1)
        elif isinstance(other, int):
            other_str = str(other)
            return self.replace(other_str, '', 1)
        else:
            return self

s1 = MyStr('New')
s2 = MyStr(890)
result1 = s1 + s2
print(result1)
print(type(result1))

s3 = MyStr(1234)
result2 = s3 + 5678
print(result2)
print(type(result2))

result3 = s1 + 'castle'
print(result3)
print(type(result3))

result4 = s1 + 77
print(result4)
print(type(result4))

result5 = s1 + True
print(result5)
print(type(result5))

result6 = s1 + ['s', ' ', 23]
print(result6)
print(type(result6))

result7 = s1 + None
print(result7)
print(type(result7))


s1 = MyStr('New bala7nce')
result1 = s1 - 7
print(result1)
print(type(result1))

s2 = MyStr('New balance')
result2 = s2 - 'bal'
print(result2)
print(type(result2))


result3 = s2 - 'Bal'
print(result3)
print(type(result3))

s3 = MyStr('pineapple apple pine')
result4 = s3 - 'apple'
print(result4)
print(type(result4))

result5 = s2 - 'apple'
print(result5)
print(type(result5))

s4 = MyStr('NoneType')
result6 = s4 - None
print(result6)
print(type(result6))

s5 = MyStr(55678345672)
result7 = s5 - 7
print(result7)
print(type(result7))

