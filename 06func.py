def chi(name ,age ,*args,**kwargs):
    print(name)
    print(age)
    print(args[0])
    print(kwargs.get('addr'))
    print(kwargs.get('qwee'))
chi("sda",22,"adsa",addr = "adsadsdqaqweq",qwee="dassadsadasdwewqwerqwredasdfs") #*args 元组可以用元组的方法
