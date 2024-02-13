
from Function import texttospeech
from googletrans import Translator
file="new"
i="5"



# def convertTeng(str):
#     translator = Translator()
#     translation = translator.translate(str,dest="en")
#     print(translation.text)

# var = input()
# print(var,type(var))
# listen_hi(var)
translator = Translator()

str = 'Bahar nikale'
#speak_hi(str)
translation = translator.translate("मेलचा विषय आहे",dest="en")
texttospeech(translation.text,file+i)

