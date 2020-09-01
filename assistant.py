import os
import pyttsx3

pyttsx3.speak("Hello, What can I do for you")
while True:
    command = input("What can I do for you: ")
    command = command.lower()

    if "run" in command or "open" in command or "play" in command or "execute" in command:
        if "chrome" in command or "browser" in command:
            pyttsx3.speak("Please Wait")
            print("On it...")
            os.system("chrome")
        elif "notepad" in command or "text editor" in command:
            pyttsx3.speak("Please Wait")
            print("On it...")
            
            os.system("notepad")
        elif "vlc" in command or "media player" in command:
            pyttsx3.speak("Please Wait")
            print("On it...")
            os.system("vlc")
        elif "firefox" in command:
            pyttsx3.speak("Please Wait")
            print("On it...")
            os.system("firefox")
        elif "pycharm" in command or "python ide" in command:
            pyttsx3.speak("Please Wait")
            print("On it...")
            os.system("pycharm")
        else:
            pyttsx3.speak("Please elaborate")
            print("Please elaborate!!!")

    elif "exit" in command or "quit" in command:
        break
    else:
        pyttsx3.speak("Sorry...Didn't get it")
        print("Sorry!!!...Didn't get it")
