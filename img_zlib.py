from PIL import Image

a_image = Image.open('C:\\Users\\Administrator\\Downloads\\a.jpg')
r, g, b = a_image.split()
print(list(a_image.getdata())) # 转换为list类型
