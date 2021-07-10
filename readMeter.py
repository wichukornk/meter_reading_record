import pytesseract
import glob
from PIL import Image

#listPath = [f for f in glob.glob("img/*.png")]

"""for i in listPath:
    im = Image.open(i)
    im_gray = im.convert("L")
    im_gray.save('out_gray.jpg', dpi=(300,300))
    image_path_in_colab="out_gray.jpg"
    extractedInformation = pytesseract.image_to_string(Image.open(image_path_in_colab))
    print(extractedInformation)"""

im = Image.open(r"img\0.png")
#im.show()
im_gray = im.convert("L")
im_gray.save('out_gray.jpg', dpi=(300,300))
image_path_in_colab="out_gray.jpg"
extractedInformation = pytesseract.image_to_string(Image.open(image_path_in_colab))
print(extractedInformation)