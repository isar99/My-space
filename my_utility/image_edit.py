from PIL import Image
import sys
import os
import click

#File path that you provide must not contain any spaces.
file_path = sys.argv[1]

# Check if path exits
if os.path.exists(str(file_path)):
    click.echo(click.style("File exist", fg='green'))

# Get filename
click.echo(click.style("filename : " + file_path.split("/")[-1], fg='blue'))
img = Image.open(file_path)
click.echo(click.style(img.format, fg='yellow'))
click.echo(click.style(img.size, fg='yellow'))
click.echo(click.style(img.mode, fg='yellow'))
#img.show()

dim = input("Want to change dimension: ")
while dim in ['y','yes','Yes','Y','YES']:
	click.echo(click.style("Image resizing...", fg="yellow"))
	ratio = float(input("Provide the ratio in which you want to resize: "))	
	length = int(input("Len: "))
	breadth = int(length/ratio)
	size = (length, breadth)
	r_img = img.resize(size)
	click.echo(click.style(r_img.size, fg='yellow'))
	click.echo(click.style("Image successfully resized", fg="green"))
	#r_img.show()

	rot = input("Want to rotate: ")
	while rot in ['y','yes','Yes','Y', 'YES']:
		click.echo(click.style("Image rotating...", fg="yellow"))
		angle = int(input("angle: " ))
		r_img = r_img.rotate(int(angle))
		click.echo(click.style("Image successfully rotated", fg="green"))
		r_img.show()

		rot = input("Want to rotate: ")

	dim = input("Want to change dimension: ")

sv = input("Want to save: ")
while sv in ['y','yes','Yes','Y','YES']: 
	click.echo(click.style("Image saving...", fg="yellow"))
	r_img = img.resize(size, resample = Image.BILINEAR)
	#r_img = r_img.rotate(int(angle))
	r_img.save("/home/ishar/Pictures/Resized/" + "resized_img." + file_path.split(".")[-1])	
	click.echo(click.style("Image successfully saved", fg="green"))
	img = Image.open("/home/ishar/Pictures/Resized/" + "resized_img." + file_path.split(".")[-1])
	sv = "quit_saving"

	

