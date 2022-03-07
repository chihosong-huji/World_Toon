# This is a sample Python script.
import pytesseract
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.




# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.1.1/bin/tesseract'
    print(pytesseract.image_to_string(r'Test.png'))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
