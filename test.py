import glob

folder_path=r"C:\jiangkermans\blogHexoSource\source\_posts\我好像已经在galgame上花费了很多时间，但是我不会改"
# img_paths = []
# # 定义图片格式列表（不包括webp）
# image_formats = ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.bmp']
# # 遍历 img/*.png,  img/*.jpg等  ,  同时还要遍历子文件夹下的图片
# for fmt in image_formats:
#     img_paths.extend(glob.glob(f"{folder_path}/{fmt}",recursive=True))
# print(img_paths)

a= glob.glob(f"{folder_path}/**/*.jpg",recursive=True)
1