
str1 = "I'm a good man,你好"
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


print(str1.capitalize())
print(str1.isupper())
print(str1.islower())
print(str1.isdigit())
print(str1.isalpha())
print(str1.isalnum())
print(str1.isspace())
print(str1.isnumeric())
print(str1.lower())
print(str1.upper())
print(str1.title())
print(str1.swapcase())


print(str1.center(22,"*"))
print(str1.strip("好"))  #去两端的
print(str1.replace("good","been"))
print(str1.split("a")) #删去a，并以此分割
print(str1.startswith("I"))
print(str1.endswith("好"))
print(str1.find("a"))
print(str1.count("a"))
print(len(str1))