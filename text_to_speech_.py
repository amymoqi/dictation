import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for v in voices:
    print("ID:", v.id)
    print("name:", v.name)

# https://stackoverflow.com/questions/58189350/installed-text-to-speech-voices-not-showing-up-in-system-speech-options-windows#:~:text=Select%20the%20Start%20button%2C%20then,%26%20Language%20%3E%20Region%20%26%20Language.&text=After%20the%20new%20language%20has,Restart%20your%20computer.