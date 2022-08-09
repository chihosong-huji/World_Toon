from googletrans import Translator

def traslate():
    f = open("translated.txt", "w")
    fread = open("outputOCR.txt", "r")
    translator = Translator()
    file_content = fread.readlines()
    for content in file_content:
        result = translator.translate(content, src='ko', dest='en')
        f.write(result.text + "\n")
    fread.close()
    f.close()

