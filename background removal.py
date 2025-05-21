from rembg import remove
from PIL import Image

input_path = 'img 1.jpg'
output_path = 'img 1.png'

img = Image.open(input_path)
output = remove(img)
output.save(output_path)
