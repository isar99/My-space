from PIL import Image, ImageOps
import os
import click

logo_file_path = input("Input path of logo file: ")
img_dir = input("Input directory of image: ")
sv_dir = input("Input directory in which you want to save image: ")
border = int(input("Border you want to provide: "))
fill = input("Choose color you want to fill border with: ")

filepaths = os.listdir(img_dir)
filepath = []
for fp in filepaths:
	filepath.append(os.path.join(img_dir, fp))
for filename in filepath:
	if not (filename.endswith('.png') or (filename.endswith('.jpg')) or filename == 'logo_file'):
		continue
	img = Image.open(filename)
	width, height = img.size

	logo_file = Image.open(logo_file_path)
	logo_width, height_width = logo_file.size
	res_log_wid = int(width/10)
	res_log_hgt = int(height/10)

	logo_img = logo_file.resize((res_log_wid,res_log_hgt))
	img.paste(logo_img,(0,0),logo_img)
	add_border = 'y'
	while add_border in ['y','yes','Yes','Y','YES']:
		img_with_border = ImageOps.expand(img, border=border, fill=fill)
		print("why?")
		img_with_border.show()
		save_img = input("Want to save image? ")
		if save_img in ['y','yes','Yes','Y','YES']:
			for fp in filepaths:
				img_with_border.save(os.path.join(sv_dir,fp))
			break
		add_border = input("Want to add border? ")

	img_with_border.show()