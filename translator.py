from tkinter import ttk
from googletrans import Translator
from ttkthemes import ThemedTk

master = ThemedTk(theme="plastik")
master.geometry('1280x990')
master.title("Translator")


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
    translated_word = translator.translate(word, dest=menu.get())
    translated_label = ttk.Label(master, text='Translated in russian: ' + str(translated_word.text) + '\n'
                                              + 'pronunciation: ' + str(translated_word.pronunciation), font=("Courier",
                                                                                                              10))
    translated_label.grid(row=1, column=3)


text = ttk.Label(master, text='Enter the word: ', font='sansSerif').grid(row=0, column=0)
# entry of word to be translated
entry = ttk.Entry(master)
entry.grid(row=0, column=1)

ttk.Label(master, text='Choose a language: ', font='sansSerif').grid(row=1, column=0)

# combo box of languages
menu = ttk.Combobox(master, values=['Choice', 'en', 'ru', 'hi', 'ur'])
menu.current(0)
menu.grid(row=1, column=1)
# buttons
btn_translate = ttk.Button(master, text='Translate', command=translate).grid(row=1, column=2)
btn_detect = ttk.Button(master, text='Detect Language', command=detect_lang).grid(row=0, column=2)

master.mainloop()
