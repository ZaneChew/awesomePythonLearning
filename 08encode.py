
s = "我是帅哥"

a= s.encode("utf-8") #编码
print(a)

n=a.decode("utf-8")
print(n)


b = "我是帅哥"

print(s is b)  #除非有特殊字符+-*/等，小数据池, 数字是 -5~256是真的,判断地址是否相等
print(s == b) #判断两值是否相等