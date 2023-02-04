from gtts import gTTS
import os

# Input
computer = input("Name of the user account on PC: ")
path = input("Text file you would like to convert: ")
saveFileName = input("What would you like to save the file as: ")

# Opens textfile
text_file = open("C:\\Users\\" + computer + "\\desktop\\" + path + ".txt", "r")

# Read whole file to a string
data = text_file.read()

# Passing the text and language to the engine, 
language = 'en'
myobj = gTTS(text=data, lang=language, slow=False)
 
# Saving the converted audio in a mp3 file
myobj.save(saveFileName + ".mp3")

# Playing the converted file
os.system(saveFileName + ".mp3")

