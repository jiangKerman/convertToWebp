# 定义文件名列表
filenames = ['a.png', 'b.c.png', 'example.archive.zip']

# 遍历文件名列表，提取最后一个点之前的所有内容
for filename in filenames:
    # 使用rsplit()方法从右侧开始分割，并指定最大分割次数为1
    name_without_extension = filename.rsplit('.', 1)[0]
    print(name_without_extension)

print("a.b.c.d".rsplit(".",1))