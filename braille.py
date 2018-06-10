
#!/usr/local/bin/python3
# -*- coding: utf8 -*-

# Written by Aadit Trivedi
# June 6, 2018
# Braille Library

# # Dependencies
# 1) sudo apt-get install pyaudio
# 3) sudo apt-get install espeak 
# 2) pip3 install SpeechRecognition
# 3) pip3 install numpy
# 4) pip3 install pillow
# 5) sudo apt-get install pytesseract
# 6) sudo apt-get install opencv-python
# 7) pip3 install opencv
# 8) pip3 install matplotlib

# Upload to GitHub

import speech_recognition as sr
import numpy as np
import os
from PIL import Image
from pytesseract import image_to_string
import matplotlib.pyplot as plt
import PIL

wit_api_key = 'MRC3OPBK2T366ILOXGCSOCXOFAVA7CXH'

global void
global a
global b
global c
global d
global e
global f
global g
global h
global i
global j
global k
global l
global m
global n
global o
global p
global q
global r
global s
global t
global u
global v
global w
global x
global y
global z

charToArray = {
    " " : [[0,0],[0,0],[0,0]],
    "a" : [[1,0],[0,0],[0,0]],
    "b" : [[1,0],[1,0],[0,0]],
    "c" : [[1,1],[0,0],[0,0]],
    "d" : [[1,1],[0,1],[0,0]],
    "e" : [[1,0],[0,1],[1,0]],
    "f" : [[1,1],[1,0],[0,0]],
    "g" : [[1,1],[1,1],[0,0]],
    "h" : [[1,0],[1,1],[0,0]],
    "i" : [[0,1],[1,0],[1,0]],
    "j" : [[0,1],[1,1],[0,0]],
    "k" : [[1,0],[0,0],[1,0]],
    "l" : [[1,0],[1,0],[1,0]],
    "m" : [[1,1],[0,0],[1,0]],
    "n" : [[1,1],[0,1],[1,0]],
    "o" : [[1,0],[0,1],[1,1]],
    "p" : [[1,1],[1,0],[1,0]],
    "q" : [[1,1],[1,1],[1,0]],
    "r" : [[1,0],[1,1],[1,0]],
    "s" : [[0,1],[1,0],[1,0]],
    "t" : [[0,1],[1,1],[1,0]],
    "u" : [[1,0],[0,0],[1,1]],
    "v" : [[1,0],[1,0],[1,1]],
    "w" : [[0,1],[0,1],[1,1]],
    "x" : [[1,1],[0,0],[1,1]],
    "y" : [[1,1],[0,1],[1,1]],
    "z" : [[1,0],[0,1],[1,1]]
}

ascii_braille = {}

asciicodes = [' ','!','"','#','$','%','&','','(',')','*','+',',','-','.','/',
          '0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
          'r','s','t','u','v','w','x','y','z','[','\\',']','^','_']

brailles = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢',
        '⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅',
        '⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵','⠪','⠳','⠻','⠘','⠸']

arrayLength = len(asciicodes)
counter = 0

while counter < arrayLength:
    ascii_braille[asciicodes[counter]] = brailles[counter]
    counter = counter + 1

letterToImgPath = {
    "a": "/Users/aadittrivedi/Desktop/braille/a.png",
    "b": "/Users/aadittrivedi/Desktop/braille/b.png",
    "c": "/Users/aadittrivedi/Desktop/braille/c.png",
    "d": "/Users/aadittrivedi/Desktop/braille/d.png",
    "e": "/Users/aadittrivedi/Desktop/braille/e.png",
    "f": "/Users/aadittrivedi/Desktop/braille/f.png",
    "g": "/Users/aadittrivedi/Desktop/braille/g.png",
    "h": "/Users/aadittrivedi/Desktop/braille/h.png",
    "i": "/Users/aadittrivedi/Desktop/braille/i.png",
    "j": "/Users/aadittrivedi/Desktop/braille/j.png",
    "k": "/Users/aadittrivedi/Desktop/braille/k.png",
    "l": "/Users/aadittrivedi/Desktop/braille/l.png",
    "m": "/Users/aadittrivedi/Desktop/braille/m.png",
    "n": "/Users/aadittrivedi/Desktop/braille/n.png",
    "o": "/Users/aadittrivedi/Desktop/braille/o.png",
    "p": "/Users/aadittrivedi/Desktop/braille/p.png",
    "q": "/Users/aadittrivedi/Desktop/braille/q.png",
    "r": "/Users/aadittrivedi/Desktop/braille/r.png",
    "s": "/Users/aadittrivedi/Desktop/braille/s.png",
    "t": "/Users/aadittrivedi/Desktop/braille/t.png",
    "u": "/Users/aadittrivedi/Desktop/braille/u.png",
    "v": "/Users/aadittrivedi/Desktop/braille/v.png",
    "w": "/Users/aadittrivedi/Desktop/braille/w.png",
    "x": "/Users/aadittrivedi/Desktop/braille/x.png",
    "y": "/Users/aadittrivedi/Desktop/braille/y.png",
    "z": "/Users/aadittrivedi/Desktop/braille/z.png",
    " ": "/Users/aadittrivedi/Desktop/braille/void.png",
}

def addImages(list_im):
    imgs = [ PIL.Image.open(i) for i in list_im ]
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
    imgs_comb = PIL.Image.fromarray(imgs_comb)
    imgs_comb.save('output.jpg')  
 
def writeImage(b_string):
    images = []
    for letter in b_string:
        images.append(letterToImgPath[letter])
    addImages(images)    
    img = Image.open('output.jpg')
    img.show()

def writeText(b_string):
    final_string = ''
    for letters in b_string:
        final_string = final_string + ascii_braille[letters.lower()]
    print(final_string)

def speechToText():
    rec = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        rec.adjust_for_ambient_noise(source)
        audio = rec.listen(source)
        return(str(rec.recognize_wit(audio, wit_api_key)))

def textToBraille(text):
    for char in text:
        char = char.lower()
        if char == "a": 
            print(char + " " + str(charToArray["a"]))
        elif char == "b": 
            print(char + " " + str(charToArray["b"]))
        elif char == "c":
            print(char + " " + str(charToArray["c"]))
        elif char == "d":
            print(char + " " + str(charToArray["d"]))
        elif char == "e": 
            print(char + " " + str(charToArray["e"]))
        elif char == "f": 
            print(char + " " + str(charToArray["f"]))
        elif char == "g": 
            print(char + " " + str(charToArray["g"]))
        elif char == "h": 
            print(char + " " + str(charToArray["h"]))
        elif char == "i": 
            print(char + " " + str(charToArray["i"]))
        elif char == "j": 
            print(char + " " + str(charToArray["j"]))
        elif char == "k": 
            print(char + " " + str(charToArray["k"]))
        elif char == "l": 
            print(char + " " + str(charToArray["l"]))
        elif char == "m": 
            print(char + " " + str(charToArray["m"]))
        elif char == "n": 
            print(char + " " + str(charToArray["n"]))
        elif char == "o":
            print(char + " " + str(charToArray["o"]))
        elif char == "p": 
            print(char + " " + str(charToArray["p"]))
        elif char == "q": 
            print(char + " " + str(charToArray["q"]))
        elif char == "r": 
            print(char + " " + str(charToArray["r"]))
        elif char == "s": 
            print(char + " " + str(charToArray["s"]))
        elif char == "t": 
            print(char + " " + str(charToArray["t"]))
        elif char == "u": 
            print(char + " " + str(charToArray["u"]))
        elif char == "v": 
            print(char + " " + str(charToArray["v"]))
        elif char == "w": 
            print(char + " " + str(charToArray["w"]))
        elif char == "x": 
            print(char + " " + str(charToArray["x"]))
        elif char == "y": 
            print(char + " " + str(charToArray["y"]))
        elif char == "z":
            print(char + " " + str(charToArray["z"]))
        elif char == " ":
            print(char + " " + str(charToArray[" "]))

def speechToBraille():
    textToBraille(speechToText())

def textToSpeech(text):
    os.system("espeak '" + str(text) + "'")

def brailleToTextArray(array):
    new_chars = ''
    for key in array:
        for a_key in charToArray:
            if charToArray[a_key] == key:
                new_chars = new_chars + str(a_key)
    return new_chars

def brailleToSpeechArray(array):
    textToSpeech(brailleToTextArray(array))

def brailleToSpeechImg(imgs):
    for img in imgs:
        for chars in letterToImgPath:
            if img == letterToImgPath[chars]:
                print(chars)

def imageToText(img):
    return image_to_string(Image.open(img))

def imageToSpeech(img):
    textToSpeech(imageToText(img))

def imageToBraille(img):
    textToBraille(imageToText(img))
#new file