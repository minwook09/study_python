from PIL import Image
import os 
gwang=os.getcwd()
files =os.listdir(gwang + '/images')

for i in files:
    img = Image.open('images/'+i).convert('L')
    img.thumbnail((500,2500))
    img.save('new_'+ i)