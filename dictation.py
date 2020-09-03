# **********************************************************************************************************************
# dictation program
# **********************************************************************************************************************
import time
import random
import pyttsx3
from pyttsx3.drivers import sapi5  # this line is important
from tkinter import *
import os

# ----------------------------------------------------------------------------------------------------------------------
# Set up
# ----------------------------------------------------------------------------------------------------------------------
file = "words"  # 必须在当前目录下
engine = pyttsx3.init()
engine.setProperty('rate', 90)  # the speed of reading a word

first_pause = 2  # pause time
second_pause = 3

word_dictation = "english"  # the language that computer read aloud for word dictation
phase_dictation = "chinese"  # the language that computer read aloud for phase dictation

# ----------------------------------------------------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------------------------------------------------
def get_languages_id(language: str):
    """
    get language id for changing speeching language
    :param language:
    :return:
    """
    voices = engine.getProperty('voices')
    for v in voices:
        if language.lower() in v.name.lower():
            return v.id


def read_from_file(file: str):
    """
    read words from file,classified to words and phases
    :return: 2 lists, one contains all words, one contains all phases
    """
    words = []
    phases = []
    f = open(file, 'r', encoding='utf8')
    lines = f.readlines()
    f.close()
    for line in lines:
        line = line.strip()
        if len(line.split(' ')) <= 2:
            words.append(line)
        else:
            phases.append((line))
    return words, phases


def read_aloud(dictation: list, language: str):
    """
    each word is read twice, pause 'first_pause' second after the first time, pause 'second_pause' second
     after the second time
    :param dictation: words that should be read
    :return:
    """
    engine.setProperty('voice', language)
    for word in dictation:
        engine.say(word)
        engine.runAndWait()
        time.sleep(first_pause)
        engine.say(word)
        engine.runAndWait()
        time.sleep(second_pause)


## main
words, phases = read_from_file(file)

# shuffling the sequence
random.shuffle(words)
random.shuffle(phases)

eng = []
chi = []

# single word dictation
for w in words:
    if len(w.split(' ')) == 2:
        eng.append(w.split(' ')[0])
eng_id = get_languages_id(word_dictation)
read_aloud(eng, eng_id)

# phases dictation
for p in phases:
    chi.append(p.split(' ')[-1])
chi_id = get_languages_id(phase_dictation)
read_aloud(chi, chi_id)

# give answer
input("Press Enter to see answer")
# with open(file, 'w', encoding='utf8') as w:
#     for i in words:
#         print(i.decode('utf-8').encode('gbk'))
#         w.write(i + '\n')
#     for i in phases:
#         print(i.decode('utf-8').encode('gbk'))
#         w.write(i + '\n')
answer = ''
ans = []
index = 0
loop = 1
for i in range(len(words)):
    ans.append(str(i+1) + '. {:<50}'.format(words[i]))
for i in range(len(phases)):
    ans.append(str(i+1) + '. {:<50}'.format(phases[i]))
while len(ans) > 50:
    if index >= 50:
        index = 0
    loop = loop + 1
    ans[index] = ans[index] + ans.pop(50)
    index = index + 1

for i in ans:
    answer = answer + i + '\n'

master = Tk()  # Create the main window
master.title('Answer')
lbl = Label(master, text=answer, relief = FLAT, width = loop*43, height = len(ans), anchor = NW, justify=LEFT).pack()
master.mainloop()
exit()
