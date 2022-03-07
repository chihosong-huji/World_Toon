import easyocr

if __name__ == '__main__':
    reader = easyocr.Reader(['ko'])
    result = reader.readtext('test.png')
    print(result)