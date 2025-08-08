dic = {123: 456, True: 999, "id": 1, "name": 'sylar', "age": 18, "stu": ['帅哥', '美⼥女女'], (1, 2, 3): '麻花藤'}

print(dic[123])
print(dic[1])
print(dic['age'])
print(dic['stu'])


dic1={}
dic1['ge'] = 222
dic1["name"]= "lis"
dic1["sex"] = "male"
dic1.setdefault("age", 23) #如无age：23键值对，则包含这个
print(dic1)

dic.update(dic1)  # 把dic1中的内容更更新到dic中. 如果key重名. 则修改替换. 如果不不存在key, 则新增
print(dic)
print(dic1.get("age"))
print(dic1.get("name"))
print(dic1.keys())
print(dic1.values())

for key in dic1.keys():
    print(key)
for value in dic1.values():
    print(value)
for key,value in dic1.items():
    print(key,value)


dic1.pop("age")
print(dic1)
del dic1["sex"]
dic1.popitem()
print(dic1)
dic1.clear() #清空
print(dic1)



dic2 = {
'name':['alex',2,3,5],
'job':'teacher',
'oldboy':{'alex':['python1','python2',100]}
}

dic2['name'].append("wusir")
print(dic2['name'])

dic2['name'][0] = 'Alex'
print(dic2['name'])

dic2['oldboy']['laonanhai'] = 'linux'
print(dic2)

dic2['oldboy']['alex'].remove('python2')
print(dic2)


dic = dict.fromkeys(["jay", "JJ"], ["周杰伦", "麻花藤"]) #乘法分配率
print(dic)
