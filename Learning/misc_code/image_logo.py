import os
from PIL import Image
import click

sq_fit_size = 300
logo_file_path = input("Input path of logo file: ")
img_dir = input("Input directory of image: ")
logo_file = logo_file_path
logo_im = Image.open(logo_file)
logo_width, logo_height = logo_im.size
if logo_width > sq_fit_size and logo_height > sq_fit_size:
	if logo_width > logo_height:
		logo_width = int(sq_fit_size)
		logo_height = int((sq_fit_size/logo_width)*logo_height)
	elif logo_width < logo_height:
		logo_height = int(sq_fit_size)
		logo_width = int((sq_fit_size/logo_height)*logo_width)
os.makedirs('with_logo',exist_ok = True)
filepaths = os.listdir(img_dir)	
filepath = []
for fp in filepaths:
	filepath.append(os.path.join(img_dir, fp))
print(filepath)
for filename in filepath:
	if not (filename.endswith('.png') or (filename.endswith('.jpg')) or filename == 'logo_file'):
		print(list(filename))
		continue
	im = Image.open(filename)
	width, height = im.size
	click.echo(click.style(f"Resizing {filename}", fg='yellow'))
	im = im.resize((width, height))
	print("Successfully resized")
	click.echo(click.style(f"Adding logo to {filename}", fg='yellow'))
	im.paste(logo_im,(width - logo_width, height - logo_height), logo_im)
	im.show()
	#im.save(os.path.join('with_logo', filename))