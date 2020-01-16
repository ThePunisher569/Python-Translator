from tkinter import ttk, StringVar
from googletrans import Translator
from ttkthemes import ThemedTk
import json

master = ThemedTk(theme="plastik")
master.geometry('1280x990')
master.title("Translator")

# reading json file
with open('languages.json', 'r') as j:
    data = json.load(j)

swapped_data = dict((v, k) for k, v in data.items())


def detect_lang():
    word = entry.get()
    translator = Translator(service_urls=['translate.google.com'])
    detected_word = translator.detect(word)

    detected_label = ttk.Label(master, text='Language Detected: ' + str(detected_word.lang), font=("Courier", 10))
    detected_label.grid(row=0, column=3)


def translate():
    word = entry.get()
    # getting translator object to translate src to des
    translator = Translator(service_urls=['translate.google.com'])
    translated_word = translator.translate(word, dest=swapped_data[menu_var.get()])
    translated_label = ttk.Label(master, text='Translated in ' + menu_var.get() + ':' + str(translated_word.text) + '\n'
                                              + 'pronunciation: ' + str(translated_word.pronunciation), font=("Courier",
                                                                                                              10))
    translated_label.grid(row=1, column=3)


text = ttk.Label(master, text='Enter the word: ', font='sansSerif').grid(row=0, column=0)
# entry of word to be translated
entry = ttk.Entry(master)
entry.grid(row=0, column=1)

ttk.Label(master, text='Choose the language: ', font='sansSerif').grid(row=1, column=0)

# combo box of languages
menu_var = StringVar(master)

menu = ttk.Combobox(master, values=list(swapped_data.keys()), textvariable=menu_var)
menu.current(0)
menu.grid(row=1, column=1)
# buttons
btn_translate = ttk.Button(master, text='Translate', command=translate).grid(row=1, column=2)
btn_detect = ttk.Button(master, text='Detect Language', command=detect_lang).grid(row=0, column=2)

master.mainloop()
