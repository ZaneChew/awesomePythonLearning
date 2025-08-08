str1 = "i'm A good man,你\t好 \nda"
int1 = 10
float1 = 3.14

print(str1[0])
print(str1[0:2])
print(str1[0:])
print(str1[:])
print(str1[:8])
print(str1[0:8:2])
print(str1[-4:-1])
print(str1[::-1])
print(str1[-1:-8:-2])
print(str1[-2:])
print(str1[:-3])

print(str1.__str__())
print(type(int1.__str__()))
print(type(float1.__str__()))

print(str1.find("oo",0,9))
print(str1.__class__)
print(str1.count("o",0,9))
print(str1.lower())
print(str1.capitalize())
print(str1.title())
print(str1.upper())
print(str1.isupper())
print(str1.islower())
print(str1.isdigit())
print(str1.isnumeric())
print(str1.isalpha())
print(str1.isalnum())
print(str1.isspace())
print(str1.casefold()) #更强力地转为小写（适合多语言，比如德语、土耳其语）
print(str1.center(20, '*'))
print(str1.rjust(20, '*'))
print(str1.ljust(20, '*'))
print(str1.encode("utf-8"))
print(str1.endswith("man,你好",0,))
print(str1.expandtabs(tabsize=0))
print("{}dsada{}asdadsa{}dasda".format(1,2,3))

template = "Hello, {name}! You are {age} years old."
data = {"name": "Alice", "age": 20}
print(template.format_map(data))

print(str1.isascii())
print(str1.index("o",0,9))

s1 = "sdad"
print(s1.isidentifier()) #用来判断一个字符串是否是有效的 Python 标识符（变量名）

print(s1.isprintable()) #✅ 字母、数字、标点、空格（' '）都算可打印
print(str1.isprintable()) #❌ 控制字符（比如换行符 \n、制表符 \t）不算可打印
print(".".join("as"))
print(str1.lstrip("i"))
print(str1.rstrip("好")) #如果不给参数，默认删除左边的空白字符（空格、\t、\n 等）,如果给了参数 chars，会删除所有在这个字符串里的字符，直到遇到不在里面的为止
print(str1.istitle())
print(str1.maketrans("imago","12345"))
print(str1.translate(str1.maketrans("imago","12345")))  #str.maketrans() 创建一个“字符映射表”，给 translate() 用，来批量替换字符串中的字符
print(str1.partition("oo")) #partition(sep) 会把字符串按 sep 分成三部分：分隔符左边、分隔符本身、分隔符右边。
print(str1.removeprefix("i'm")) #removeprefix(prefix) 用来移除字符串开头的指定前缀，如果有的话。
print(str1.rpartition("oo"))
print(str1.split("oo"))
print(str1.removesuffix("你\t好")) #removesuffix(suffix) 用来移除字符串结尾的指定后缀，如果有的话。
print(str1.splitlines()) #splitlines() 把字符串按“行”分开，返回一个行组成的列表
print(str1.swapcase())
print(str1.startswith("i'm"))
print(str1.zfill(21)) #zfill(width) 返回一个指定宽度的字符串，不够宽度就在左边补 0
print(str1.replace("i'm", "I'm"))

print(str1.__add__(s1))  #拼接字符串

def A(a:int ,b: str):
    return "sdadas"
print(A.__annotations__)

print(str1.__contains__("i'm")) #__contains__(self, item) 定义了对象是否包含某个元素，用来支持 item in obj 这样的语法。

class Person:
    def __init__(self, name:str, age:int):
        self.name = name
        self.age = age
    def __delattr__(self,attr):
        print("delattr",attr)
alx = Person("alx",20)
del alx.age

print(alx.__dict__)
print(Person.__dict__) #__dict__ 是一个字典，存储了对象（或类）当前的所有“实例属性”或“类属性”。

print(str1.__dir__()) #__dir__(self) 决定了当你对一个对象调用 dir(obj) 时，返回的属性和方法列表。
print(str1.__eq__("i'm"))   # ==
print(str1.__ne__("i'm"))   # !=
print(str1.__le__("i'm"))   # <=
print(str1.__lt__("i'm"))   # <
print(str1.__ge__("i'm"))   # >=
print(str1.__gt__("i'm"))   # >
# print(str1.__format__())
print(str1.__len__())
print(str1.__sizeof__())  # in bytes
print(str1.__hash__()) #__hash__() 返回一个整数，用于表示字符串的哈希值（在字典、set 等地方使用）。
print(str1.__repr__())
it = str1.__iter__() #__iter__() 会返回一个“迭代器”，让你能逐个访问字符串中的字符。用next（）
print(next(it))
print(next(it))
print(str.__module__) #__module__ 表示该对象（通常是类或函数）定义所在的模块名称。

print(str.__doc__) #__doc__ 是类、函数、模块等的文档字符串，用来说明它们的作用和用法。
def add(a, b):
    """返回两个数字的和"""
    return a + b

print(add.__doc__)

# print(str1.__mod__()) #__mod__ 实现了字符串的格式化操作，也就是用 % 来格式化字符串时，背后调用的就是它。
# s = "Hello, %s!"
# print(s % "Zeyha")          # 用 % 格式化 Hello, Zeyha!
# print(s.__mod__("Zeyha"))   # 等价于上面 Hello, Zeyha!

print(str1.__mul__(3))  #__mul__(self, n) 返回字符串自身重复 n 次的新字符串。
print(str1.__rmul__(3))
print(str1.__subclasshook__())
# print(str1.__reduce__()) #__reduce__() 返回一个元组，告诉 pickle 模块如何“拆解”和“重建”这个对象。








