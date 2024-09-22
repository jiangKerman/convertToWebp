from PIL import Image
import os
import io
import glob


def convert_to_webp(image_path: str):
    # 打开图片
    img = Image.open(image_path)

    # 使用io.BytesIO()来创建一个临时的二进制流，用于保存图片
    # 这样我们可以在不写入磁盘的情况下估算文件大小
    temp_lossy = io.BytesIO()
    temp_lossless = io.BytesIO()

    # 保存为有损WebP格式到临时流
    img.save(temp_lossy, 'webp', quality=75)
    # 获取有损压缩的大小
    lossy_size = temp_lossy.tell()

    # 保存为无损WebP格式到临时流
    img.save(temp_lossless, 'webp', lossless=True)
    # 获取无损压缩的大小
    lossless_size = temp_lossless.tell()
    # print(f'{lossy_size}    {lossless_size}')
    模式=""
    if lossy_size < lossless_size:
        # 有损压缩文件更小，使用有损压缩保存
        # 由于已经保存过一次有损压缩，只需将流中的数据写入文件
        with open(f'{image_path.rsplit(".", 1)[0]}.webp', 'wb') as file:
            temp_lossy.seek(0)  # 确保从文件开头开始写入
            file.write(temp_lossy.read())
        模式='有损压缩'
        # print("选择了有损压缩，文件大小：{} 字节".format(lossy_size))
    else:
        with open(f'{image_path.rsplit(".", 1)[0]}.webp', 'wb') as file:
            temp_lossless.seek(0)  # 确保从文件开头开始写入
            file.write(temp_lossless.read())
        # print("无损压缩，文件大小：{} 字节".format(lossless_size))
        模式='无损压缩'
    # 关闭临时流
    temp_lossy.close()
    temp_lossless.close()
    return 模式

def convert_to_webp_from_folder(folder_path:str):
    img_paths = []
    # 定义图片格式列表（不包括webp）
    image_formats = ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.bmp']
    # 遍历 img/*.png,  img/*.jpg等
    for fmt in image_formats:
        img_paths.extend(glob.glob(f"{folder_path}/**/{fmt}",recursive=True))
    # print(img_paths)

    for imgpath in img_paths:
        压缩模式 = convert_to_webp(imgpath)
        print(imgpath,压缩模式)

convert_to_webp_from_folder(r'C:\jiangkermans\blogHexoSource\source\_posts\我好像已经在galgame上花费了很多时间，但是我不会改')
