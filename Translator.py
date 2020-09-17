from translate import Translator
error = 1

while(error == 1):
    try:
        print("1-Spanish  2-Portuguese  3-Bahasa Melayu")
        lang = int(input("Please Select a Language (select a number): "))
        error = 0
    except ValueError:
        print("You have entered an invalid input, please input a number (1,2,3)")
        error = 1

if(lang == 1):
    lang = 'es'
elif(lang == 2):
    lang = 'pt'
elif(lang == 3):
    lang = 'ms'
else:
    lang = 'en'

try:
    with open('./Sample text.txt',mode='r') as f:
        txt = f.read()
        translator = Translator(to_lang=lang)
        translation = translator.translate(txt)
        with open('./Translated text.txt',mode='w') as f2:
            f2.write(translation)
except UnicodeDecodeError:
    print("Characters in the text document are not supported by the translator.\n "
          "Remove the characters from the text document. \n Languages with latin characters are preferred")
