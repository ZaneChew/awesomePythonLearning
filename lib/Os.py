import os

# | 方法                       | 作用       | 示例                                                       |
# | ------------------------ | -------- | -------------------------------------------------------- |
# | `os.path.join(a, b)`     | 拼接路径     | `os.path.join("folder", "file.txt") → 'folder/file.txt'` |
# | `os.path.abspath(path)`  | 获取绝对路径   | `os.path.abspath("file.txt")`                            |
# | `os.path.basename(path)` | 获取文件名部分  | `'a/b/c.txt' → 'c.txt'`                                  |
# | `os.path.dirname(path)`  | 获取目录名部分  | `'a/b/c.txt' → 'a/b'`                                    |
# | `os.path.exists(path)`   | 判断路径是否存在 | `os.path.exists("test.txt")`                             |
# | `os.path.isfile(path)`   | 判断是否是文件  | `os.path.isfile("a.txt")`                                |
# | `os.path.isdir(path)`    | 判断是否是文件夹 | `os.path.isdir("folder/")`                               |
# | `os.path.splitext(path)` | 分离扩展名    | `'a.txt' → ('a', '.txt')`                                |

print(os.path.abspath('.'))


# | 方法                    | 作用            | 示例                            |
# | --------------------- | ------------- | ----------------------------- |
# | `os.listdir(path)`    | 返回目录下所有文件/目录名 | `os.listdir(".")`             |
# | `os.mkdir(path)`      | 创建单个目录        | `os.mkdir("new_folder")`      |
# | `os.makedirs(path)`   | 创建多级目录        | `os.makedirs("a/b/c")`        |
# | `os.remove(path)`     | 删除文件          | `os.remove("file.txt")`       |
# | `os.rmdir(path)`      | 删除空目录         | `os.rmdir("empty_folder")`    |
# | `os.removedirs(path)` | 删除多级空目录       | `os.removedirs("a/b/c")`      |
# | `os.rename(src, dst)` | 重命名/移动文件或文件夹  | `os.rename("a.txt", "b.txt")` |
# | `os.chdir(path)`      | 切换当前工作目录      | `os.chdir("/home/user")`      |
# | `os.getcwd()`         | 获取当前工作目录      | `os.getcwd()`                 |

# os.mkdir('../Ai')