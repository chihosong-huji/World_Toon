import easyocr

def OCR(photo_name):
    f = open("outputOCR.txt", "w")
    reader = easyocr.Reader(['ko'])
    result = reader.readtext(photo_name)
    for data in result:
        f.write(data[1] + "\n")
    f.close()
    return
