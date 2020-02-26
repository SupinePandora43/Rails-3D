"""
Rails-3D help script
* generating specular maps
* merging models
"""
from PIL import Image
import os
colors = {
	"outer":(179, 179, 179),
	"inner":(102, 102, 102)
}
path="./assets/minecraft/textures/block/rail_s.png"
def image():
	return Image.new("RGB", (16,16), (0,0,0))
def rail():
	img = image()
	for x in range(0,16):     # only values [0-15]
		for y in range(0,16): # only values [0-15]
			if x==2 or x==13:
				img.putpixel((x,y),colors["outer"])
			elif x==3 or x==12:
				img.putpixel((x,y),colors["inner"])
	return img
def rail_corner():
	img = image()
	def outer(x,y):
		return (y>11 and x == 2) or (y>=14 and x==13) or (x>11 and y == 2) or (x>13 and y==13) \
		or(12>y>9 and x==3) \
		or(10>y>7 and x==4) \
		or((x==5 and y==7)or(x==6 and y==6)or(x==7 and y==5)) \
		or(12>x>9 and y==3) \
		or(10>x>7 and y==4)
	def inner(x,y):
		return (y>11 and x == 3) or (y>=14 and x==12) or (x>11 and y == 3) or (x>13 and y==12) \
		or(12>y>9 and x==4) \
		or(10>y>7 and x==5) \
		or((x==6 and y==7)or(x==7 and y==6)) \
		or(12>x>9 and y==4) \
		or(10>x>7 and y==5) \
		or((x,y)==(13,13))
	for x in range(0,16):     # only values [0-15]
		for y in range(0,16): # only values [0-15]
			if outer(x,y):
				img.putpixel((x,y),colors["outer"])
			elif inner(x,y):
				img.putpixel((x,y),colors["inner"])
	return img
def powered_rail():
	img = rail()
	for y in range(0,16):
		img.putpixel((4,y), colors["inner"])
		img.putpixel((11,y), colors["inner"])
	return img
activator_rail=rail
def detector_rail():
	img = rail()
	for x in range(6,10):
		for y in range(6,10):
			img.putpixel((x,y), colors[(x==9 or y==9) and "inner" or "outer"])
	return img
rails = [
	{
		"path": "./assets/minecraft/textures/block/%s_s.png",
		"textures": [
			{
				"file": "rail",
				"func": rail
			},
			{
				"file": "rail_corner",
				"func": rail_corner
			},
			{
				"file": "powered_rail",
				"func": powered_rail
			},
			{
				"file": "activator_rail",
				"func": activator_rail
			},
			{
				"file": "detector_rail",
				"func": detector_rail
			}
		]
	}
]
for railgroup in rails:
	for texture in railgroup["textures"]:
		specular_image = texture["func"]()
		os.makedirs(os.path.dirname(railgroup["path"]%texture["file"]),exist_ok=True)
		specular_image.save(railgroup["path"]%texture["file"])
