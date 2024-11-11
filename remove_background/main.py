from rembg import remove 
from PIL import Image

url = Image.open('./imgs/input/image.jpg')
out	= remove(url)
out.save('./imgs/output/image.png', 'PNG')