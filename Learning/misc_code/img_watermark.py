from PIL import Image, ImageOps
path = input(f"Provide the path of image: ")
border = int(input(f"Border you want to provide: "))
fill = input(f"Choose color you want to fill border with: ")

img = Image.open(path)

img_with_border = ImageOps.expand(img, border=border, fill=fill)
img_with_border.show()

img_with_border.save('/home/ishar/Pictures/Webcam/isar-with-border.jpg')