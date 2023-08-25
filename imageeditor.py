from PIL import Image, ImageEnhance, ImageFilter
import os

# path = r'images';
# pathOut = r'editedImages'
script_dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(script_dir, 'images')
pathOut = os.path.join(script_dir, 'editedImages')
for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(360)
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    clean_name = os.path.splitext(filename)[0]

    edit.save(f"{pathOut}/{clean_name}_edited.jpg")