from PIL import Image
import PIL
import os
import glob

'''im = Image.open("D:\Work\Codes\yolo-colab-simple-main\yolo_colab\img\pr_1 (6034).jpg")
print(f"The image size dimensions are: {im.size}")
file_name = "pr_1 (6034).jpg"

ism = im.save(file_name,optimize=True,quality=30)  
'''

import PIL
import os
import os.path
from PIL import Image

f = r'D:\Work\Codes\image_extraction\images'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.save(file,optimize=True, quality = 60)
