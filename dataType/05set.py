import copy

set1 = {2, 3, 4, 5, 6, 7, 8, 9}
set1.add(10)
print(set1)

set1.pop() #删第一个
print(set1)
set2=set1.copy() #浅拷贝
set3 = set1 #指向set1的内存地址，会跟着变

a = copy.deepcopy(set1) #深拷贝
set1.clear()
print(set1)
print(set2)
print(set3)
print(a)




li = ["李嘉诚", "麻花藤", "⻩黄海峰", "刘嘉玲"]
s = "e".join(li) #变字符串
print(s)
b= s.split("e")
print(b)

#列表只能从后往前删的，在循环删除的情况下
for i in range(len(li)):
    li.pop()
print(li)


s = {"刘嘉玲", '关之琳', "王祖贤"}
s.update('麻花藤') # 迭代更更新,分开后加
s.remove('麻') #删
s.clear() #清空
print(s)


a = [1, 2]
a[1] = a
print(a[1])
