# This is a sample Python script.
import pytesseract
import OCR, translate
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def main(URL):
    # pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
    # print(pytesseract.image_to_string(r'Test.png'))
    OCR.OCR("test2.png")
    translate.traslate()



# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    main("www.naver.com")
