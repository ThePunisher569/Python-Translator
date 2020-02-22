import urllib.request as ur
from tkinter import ttk, StringVar, messagebox
from googletrans import Translator
from ttkthemes import ThemedTk
import json


def detect_lang():
    word = entry.get()
    if len(word) > 0:
        translator = Translator(service_urls=['translate.google.com'])
        # the detector
        detected_word = translator.detect(word)

        detected_label = ttk.Label(master, text='Language Detected: ' + str(detected_word.lang), font=("Courier", 10))
        detected_label.grid(row=0, column=3)
    else:
        messagebox.showwarning(title='Error', message='No word entered')


def translate():
    word = entry.get()
    if len(word) > 0:

        # getting translator object to translate src to des
        translator = Translator(service_urls=['translate.google.com'])
        # the translator
        translated_word = translator.translate(word, dest=swapped_data[menu_var.get()])

        textvar.set(str('Translated in ' + menu_var.get() + ':' + str(translated_word.text) + '\n'
                    + 'Pronunciation: ' + str(translated_word.pronunciation)))

        translated_label = ttk.Label(master, textvariable=textvar, font=("Courier", 10))
        translated_label.grid(row=1, column=3)
    else:
        messagebox.showwarning(title='Error', message='No word entered')


if __name__ == '__main__':
    master = ThemedTk(theme="plastik")
    master.geometry('1280x990')
    master.title("Translator")
    # the icon
    master.iconbitmap('transicon.ico')


    # internet permission
    try:
        if not (ur.urlopen('https://google.com')):
            raise ConnectionError('No Internet connection')
    except:
        # exception handling
        master.withdraw()
        messagebox.showwarning(title='Error', message='No Internet Connection')
        master.destroy()
        exit(-1)
    # reading json file
    with open('languages.json', 'r') as j:
        data = json.load(j)

    swapped_data = dict((v, k) for k, v in data.items())
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

    # variable for translated label
    textvar = StringVar(master)
    # buttons
    btn_translate = ttk.Button(master, text='Translate', command=translate).grid(row=1, column=2)
    btn_detect = ttk.Button(master, text='Detect Language', command=detect_lang).grid(row=0, column=2)

    master.mainloop()
