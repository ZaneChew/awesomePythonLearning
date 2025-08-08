lst = ["麻花藤", "王剑林林", "⻢马芸", "周鸿医", "向华强"]

print(lst[0])
print(lst[0:4])
print(lst[3:-1])
print(lst[1:])
print(lst[::2])
print(lst[::-1])

lst.append("miss qu")
lst.insert(4, "missLI")
print(lst)

lst1 = ["王志⽂文", "张⼀一⼭山", "苦海海⽆无涯"]
lst.extend(lst1)
print(lst)

lst.pop()
print(lst)

lst.pop(3)
print(lst)

lst.remove(lst[1])
print(lst)

lst.clear()
print(lst)



numls = [1, 2, 3,2321,123123,453224532]
numls.sort(reverse=True) #降序
print(numls)

print(len(numls))
