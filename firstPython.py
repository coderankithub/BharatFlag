import pyttsx3 
import os
print("Press 1 for chrome")
print("Press 2 for notebook")
print("Press 3 to make your name speak")
n = int(input()) 
if n == 1:
    os.system("chrome")
elif n == 2:
    os.system('notebook') 
else:
    name = input("Enter your name")
    pyttsx3.speak(name)    