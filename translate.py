# import googletrans
from googletrans import Translator

if __name__ == '__main__':
    translator = Translator()
    korean = '일부러 살려서 보냈다'
    result = translator.translate(korean, src='ko', dest='en')
    print(result.text)