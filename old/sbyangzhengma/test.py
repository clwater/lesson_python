
import pytesseract
from PIL import Image


image = Image.open('./yanzhengma.jpg')
vcode = pytesseract.image_to_string(image)
print (vcode)