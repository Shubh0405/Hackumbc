'''
!apt-get install poppler-utils
# %pip install pdf2image
!pip install opencv-python
!sudo apt install tesseract-ocr
!pip install pytesseract
!pip install pillow
'''
#modules to be imported

# Commented out IPython magic to ensure Python compatibility.
import cv2
import pytesseract
from pdf2image import convert_from_bytes,convert_from_path
# from google.colab.patches import cv2_imshow
# import matplotlib.pyplot as plt
# %matplotlib inline
import urllib.request

def image_processing(img):
    # get grayscale image
    img1 =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # noise removal
    img2 = cv2.medianBlur(img1,5)
    #thresholding
    #return cv2.threshold(img2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    return cv2.adaptiveThreshold(img2, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)

def ocr_to_text(img):
    custom_config = r'--oem 1 --psm 6'
    return pytesseract.image_to_string(img, config=custom_config)

def text_generation(x_data):
  text = []
  for x in x_data:
      a = image_processing(x)
      b = ocr_to_text(a)
      text.append(b)
  return text

def pdf_to_images(pdfs):
      #pdfs = 'try1.pdf'
      # pages = convert_from_path(pdfs, 500)
      pages = convert_from_bytes(pdfs.read())
      x_data = []
      i = 1
      for page in pages:
          image_name = "Page_a" + str(i) + ".jpg"
          page.save(image_name, "JPEG")
          image = cv2.imread(image_name)
          x_data.append(image)
          i = i+1
      text = []
      text = text_generation(x_data)
      for t in text:
          #print(t)
          f = open("text1.txt", "a+")
          f.write(t)
          f.close()

      return text

def main_url(download_url):

    # from urllib.request import urlretrieve, urlopen
    #urlretrieve(download_url, "document.pdf")
    # response = urllib.request.urlopen(download_url)
    # f1 = open("document.pdf", 'wb')
    # f1.write(response.read())
    # f1.close()
    # print(response)
    text = []
    pdfs = download_url
    text = pdf_to_images(pdfs)
    return text
