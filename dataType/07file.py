import os


f = open("file.txt", mode="r", encoding="utf-8")  #r只读

content = f.read(9) #9个字符
content2 = f.readline() #一次读一行
lst = f.readlines() #每行都是列表中的一个元素
print(content)
print(content2)
print(lst)
f.close()

a = open("file.txt", mode="br")  #rb只读，bytes类型
b = a.read(9) #9个bytes字符
print(b)
a.close()

#==================================================================================


# f = open("file.txt", mode="w", encoding="utf-8") #可写不可读
# f.write("⾦金金⽑毛狮王")
# f.flush() # 刷新. 养成好习惯
# # f.read() #报错
# f.close()

# f = open("file.txt", mode="wb") #只写，bytes类型
# f.write("⾦金金⽑毛狮王".encode("utf-8"))
# f.flush()
# f.close()


# f = open("file.txt", mode="a", encoding="utf-8") #追加
# f.write("麻花藤的最爱")
# f.flush()
# f.close()

# f = open("file.txt", mode="r+", encoding="utf-8") #先读再写
# content = f.read()
# f.write("麻花藤的最爱")
# print(content)
# f.flush()
# f.close()



# f = open("file.txt", mode="w+", encoding="utf-8") #先写后读，所以会清空之前的内容
# f.write("哈哈")
# content = f.read()
# print(content)
# f.flush()
# f.close()



# f = open("file.txt", mode="r+", encoding="utf-8")
# f.seek(0) # 光标移动到开头,单位是bytes
# content = f.read() # 读取内容, 此时光标移动到结尾
# print(content)
# f.seek(0) # 再次将光标移动到开头
# f.seek(0, 2) # 将光标移动到结尾
# content2 = f.read() # 读取内容. 什什么都没有
# print(content2)
# f.seek(0) # 移动到开头
# f.write("张国荣") # 写⼊入信息. 此时光标在9 中⽂3 * 3个 = 9
# print(f.tell()) # 光标位置9
# f.truncate() # 删掉光标后⾯面的所有内容
# f.flush()
# f.close()


#文件修改，创建新文件，修改，删掉旧文件

# with open("file.txt", mode="r", encoding="utf-8") as f1,\
#         open("file1.txt", mode="w", encoding="UTF-8") as f2:
#             content = f1.read()
#             new_content = content.replace("冰糖葫芦", "⼤大⽩白梨梨")
#             f2.write(new_content)
# os.remove("file.txt") # 删除源⽂文件
# os.rename("file1.txt", "file.txt") # 重命名新⽂文件


with open("file.txt", mode="r", encoding="utf-8") as f1,\
        open("file1.txt", mode="w", encoding="UTF-8") as f2:
            for line in f1:
                new_line = line.replace("⼤大⽩白梨梨", "冰糖葫芦")
                f2.write(new_line)
os.remove("file.txt") # 删除源⽂文件
os.rename("file1.txt", "file.txt") # 重命名新⽂文件












