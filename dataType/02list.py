lst = ["麻花藤", "王剑林", "马芸", "周鸿医", "向华强"]

print(lst[0])
print(lst[0:4])
print(lst[3:-1])
print(lst[1:])
print(lst[::2])
print(lst[::-1])


print(lst.index("周鸿医"))
print(lst.copy())
print(lst.count("周鸿医"))
lst.reverse() #反转列表后返回None，列表已经被反转了
print(lst)
lst.append("miss qu")
lst.insert(4, "missLI")
lst1 = ["王志文", "张一山", "苦海无涯"]
lst.extend(lst1)
lst.pop()
lst.pop(3)
lst.remove(lst[1])
lst.clear()

numls = [1, 2, 3,2321,123123,453224532]
numls.sort(reverse=True) #降序
print(numls)
print(len(numls))


