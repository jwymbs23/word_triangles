from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from PIL import ImageOps
import random

font_location = '/usr/share/fonts/truetype/freefont/FreeSans.ttf'

def make_triangle(w1,w2,w3,s1,s2,s3):
    triangle = Image.open("./triangle.jpg")
    im1 = Image.open("./downloads/" + w1+'_'+str(random.randint(1,2))+".jpg")
    im2 = Image.open("./downloads/" + w2+'_'+str(random.randint(1,2))+".jpg")
    im3 = Image.open("./downloads/" + w3+'_'+str(random.randint(1,2))+".jpg")
    size1 = im1.size
    size2 = im2.size
    size3 = im3.size
    print(size1)
    set_width = 200
    set_height = 150
    im1 = im1.resize((set_width,size1[1]*set_width/size1[0]))
    im2 = im2.resize((size2[0]*set_height/size2[1],set_height))
    im3 = im3.resize((size3[0]*set_height/size3[1],set_height))
    triangle.paste(im1,(180,10))
    triangle.paste(im2,(730,470))
    triangle.paste(im3,(100,700))
    draw = ImageDraw.Draw(triangle)
    font = ImageFont.truetype(font_location, 30)
    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text((440, 120),w1,(0,0,0),font = font)
    draw.text((700, 650),w2,(0,0,0),font = font)
    draw.text((100, 650),w3,(0,0,0),font = font)
    
    txt=Image.new('L', (500,50))
    d = ImageDraw.Draw(txt)
    d.text( (0, 0), s1,  font=font, fill = 255) #word 13
    w=txt.rotate(58,  expand=1)
    triangle.paste(ImageOps.colorize(w, (255,255,255), (0,0,0)),(290,60), w)
    
    
    txt=Image.new('L', (500,50))
    d = ImageDraw.Draw(txt)
    d.text( (0, 0), s2,  font=font, fill = 255) #word 12
    w=txt.rotate(-60,  expand=1)
    triangle.paste(ImageOps.colorize(w, (255,255,255), (0,0,0)),(530,400), w)
    
    
    txt=Image.new('L', (500,50))
    d = ImageDraw.Draw(txt)
    d.text( (0, 0), s3,  font=font, fill = 255) #word 23
    w=txt.rotate(0,  expand=1)
    triangle.paste(ImageOps.colorize(w, (255,255,255), (0,0,0)),(400,600), w)
    imagename = './triangles/'+s1+'_'+s2+'_'+s3+".jpg"
    triangle.save(imagename)
    return imagename

