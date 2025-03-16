from PIL import Image
import sys
import os
import click

#File path that you provide must not contain any spaces.
file_path = sys.argv[1]

# Check if path exits
if os.path.exists(str(file_path)):
	click.echo(click.style(f"File exist",fg="green"))

else:
	click.echo(click.style("File doesn't exist",fg='red'))

# Get filename
click.echo(click.style("filename : " + file_path.split("/")[-1], fg='blue'))
img = Image.open(file_path)
click.echo(click.style(img.format, fg='yellow'))
click.echo(click.style(img.size, fg='yellow'))
click.echo(click.style(img.mode, fg='yellow'))
#img.show()

def do_resize():
	click.echo(click.style("Image resizing...", fg="yellow"))
	ratio = float(input("Provide the ratio in which you want to resize: "))	
	length = int(input("Len: "))
	breadth = int(length/ratio)
	size = (length, breadth)
	r_img = img.resize(size)
	click.echo(click.style(img.size, fg='yellow'))
	click.echo(click.style("Image successfully resized", fg="green"))
	return r_img

def do_rotate():
	click.echo(click.style("Image rotating...", fg="yellow"))
	angle = int(input("angle: " ))
	rot_img = img.rotate(int(angle))
	click.echo(click.style("Image successfully rotated", fg="green"))
	img_show()
	return rot_img

dim = input("Want to change dimension: ")
while dim in ['y','yes','Yes','Y','YES']:
	do_resize()
	dim = input("Want to change dimension: ")

rot = input("Want to rotate: ")
while rot in ['y','yes','Yes','Y', 'YES']:
	do_rotate()
	rot = input("Want to rotate: ")

def do_save():
	click.echo(click.style("Image saving...", fg="yellow"))
	sv_img = r_img.resize(size, resample = Image.BILINEAR)
	#sv_img = img.rotate(int(angle))
	sv_img.save("/home/ishar/Pictures/Resized/" + "resized_img." + file_path.split(".")[-1])	
	click.echo(click.style("Image successfully saved", fg="green"))
	img = Image.open("/home/ishar/Pictures/Resized/" + "resized_img." + file_path.split(".")[-1])
	sv = "quit_saving"

sv = input("Want to save: ")
while sv in ['y','yes','Yes','Y','YES']: 
	do_save()