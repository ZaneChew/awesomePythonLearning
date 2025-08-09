import requests

print(requests.__author__)
print(requests.__author_email__)
print(requests.__version__)
print(requests.__copyright__)
print(requests.__license__)
print(requests.__cake__)

print(requests.request(method = "get",url = "https://www.baidu.com/"))
print(requests.get(url = "https://www.baidu.com/", params = {"kw" : "python"})) #发起 GET 请求，params 会拼接到 URL 末尾。https://www.baidu.com/?kw=python
print(requests.session())
print(requests.head(url = "https://www.baidu.com/"))
print(requests.put(url = "https://www.baidu.com/"))
print(requests.delete(url = "https://www.baidu.com/"))
print(requests.post(url = "https://www.baidu.com/"))
print(requests.patch(url = "https://www.baidu.com/"))
print(requests.options(url = "https://www.baidu.com/"))
