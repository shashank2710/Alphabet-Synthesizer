import os
from PIL import Image, ImageDraw, ImageFont
import string

##########################################################################################
chars = string.ascii_uppercase + '0123456789'
fontDirectory = '/home/ssatyanarayana/fonts/ofl'
targetDirectory= '/home/ssatyanarayana/tf2classifier/new_data'
counter=0
image_width=128
image_height=128
font_size=96
###########################################################################################
for file in os.listdir(fontDirectory):
    for fntFiles in os.listdir(fontDirectory+'/'+file):
        # Select Font Type Here
        if fntFiles.endswith("-Regular.ttf"):
            font = ImageFont.truetype(fontDirectory + '/' + file + '/' + fntFiles, font_size)
            counter+=1
            for i in range (len(chars)):
                # Select Background Color Here
                image = Image.new('RGB', (image_width,image_height), color=(255, 255, 255))
                draw = ImageDraw.Draw(image)
                w, h = draw.textsize(chars[i])
                #Draw Image Here, You can Choose image color and perform text centering
                draw.text(((image_width-w)/2,(image_height-h)/2), chars[i], font=font, fill=(0,0,0))
                if not os.path.exists(targetDirectory+'/'+chars[i]):
                    os.makedirs(targetDirectory+'/'+chars[i])
                image.save(targetDirectory+'/'+chars[i]+ '/' + chars[i] +'_'+str(counter)+'.jpg')