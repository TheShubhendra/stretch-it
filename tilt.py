from PIL import Image,ImageOps, ImageDraw,ImageFont
import sys


out_file=open("out.png","w+")
text = sys.argv[1]


font=ImageFont.truetype(font="arial.ttf",size=150)

img = Image.new(mode="L",size=(150*len(text),150),color="white")

draw = ImageDraw.Draw(img)
draw.text((0,0),text=text,fill="black",font=font)
width, height= img.size
img2 = img.resize((round(width/5), height*5))
img2.save(out_file,"jpeg")
img2.show()