import RPi.GPIO as GPIO
import time
import pytesseract
from PIL import Image
import os

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
def textToBraille(text):
    final_braille = []
    for char in text:
        char = char.lower()
        if char == "a": final_braille.append(charToArray["a"])
        elif char == "b": final_braille.append(charToArray["b"])
        elif char == "c": final_braille.append(charToArray["c"])
        elif char == "d": final_braille.append(charToArray["d"])
        elif char == "e": final_braille.append(charToArray["e"])
        elif char == "f": final_braille.append(charToArray["f"])
        elif char == "g": final_braille.append(charToArray["g"])
        elif char == "h": final_braille.append(charToArray["h"])
        elif char == "i": final_braille.append(charToArray["i"])
        elif char == "j": final_braille.append(charToArray["j"])
        elif char == "k": final_braille.append(charToArray["k"])
        elif char == "l": final_braille.append(charToArray["l"])
        elif char == "m": final_braille.append(charToArray["m"])
        elif char == "n": final_braille.append(charToArray["n"])
        elif char == "o": final_braille.append(charToArray["o"])
        elif char == "p": final_braille.append(charToArray["p"])
        elif char == "q": final_braille.append(charToArray["q"])
        elif char == "r": final_braille.append(charToArray["r"])
        elif char == "s": final_braille.append(charToArray["s"])
        elif char == "t": final_braille.append(charToArray["t"])
        elif char == "u": final_braille.append(charToArray["u"])
        elif char == "v": final_braille.append(charToArray["v"])
        elif char == "w": final_braille.append(charToArray["w"])
        elif char == "x": final_braille.append(charToArray["x"])
        elif char == "y": final_braille.append(charToArray["y"])
        elif char == "z": final_braille.append(charToArray["z"])
        elif char == " ": final_braille.append(charToArray[" "])
        elif char.isdigit(): final_braille.append(charToArray[" "])
    return final_braille

GPIO.setmode(GPIO.BCM)

pin1 = 7
pin2 = 8
pin3 = 14
pin4 = 15
pin5 = 18
pin6 = 23
button_pin = 26

# SETUP

GPIO.setup(pin1,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.setup(pin3,GPIO.OUT)
GPIO.setup(pin4,GPIO.OUT)
GPIO.setup(pin5, GPIO.OUT)
GPIO.setup(pin6,GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)





# INITIALIZE PWM

a = GPIO.PWM(pin1, 50)
b = GPIO.PWM(pin2, 50)
c = GPIO.PWM(pin3, 50)
d = GPIO.PWM(pin4, 50)
e = GPIO.PWM(pin5, 50)
f = GPIO.PWM(pin6, 50)

# START PWM

a.start(7.5)
b.start(7.5)
c.start(7.5)
d.start(7.5)
e.start(7.5)
f.start(7.5)

class Servo:
    def __init__(self, pwm_sig):
        self.pwm_sig = pwm_sig
    def off(self):
        self.pwm_sig.ChangeDutyCycle(2.5)
        time.sleep(0.1)
    def on(self):
        self.pwm_sig.ChangeDutyCycle(7.5)
        time.sleep(0.1)
    def stop(self):
        self.pwm_sig.stop()

global a1
global a2
global a3
global b1
global b2
global b3

a1 = Servo(a)
a2 = Servo(b)
a3 = Servo(c)
b1 = Servo(d)
b2 = Servo(e)
b3 = Servo(f)


def output(mystring, big_array):
    os.system("clear")
    large_string = mystring
    x = 0
    for letters in big_array:
        print(large_string[x])
        print(letters)
        if letters[0][0] == 0:
            a1.off()
        if letters[0][0] == 1:
            a1.on()
        if letters[0][1] == 0:
            b1.off()
        if letters[0][1] == 1:
            b1.on()
        if letters[1][0] == 0:
            a2.off()
        if letters[1][0] == 1:
            a2.on()
        if letters[1][1] == 0:
            b2.off()
        if letters[1][1] == 1:
            b2.on()
        if letters[2][0] == 0:
            a3.off()
        if letters[2][0] == 1:
            a3.on()
        if letters[2][1] == 0:
            b3.off()
        if letters[2][1] == 1:
            b3.on()
        time.sleep(1.5)
        a1.off()
        a2.off()
        a3.off()
        b1.off()
        b2.off()
        b3.off()
        time.sleep(1.5)
        x = x + 1
        os.system("clear")
    a1.off()
    a2.off()
    a3.off()
    b1.off()
    b2.off()
    b3.off()
    a1.stop()
    a2.stop()
    a3.stop()
    b1.stop()
    b2.stop()
    b3.stop()
    GPIO.cleanup()



def take_read_pic():
    os.system("fswebcam test.jpg")
    old_string = str(pytesseract.image_to_string(Image.open('test.jpg')).encode("utf-8"))
    new_string = ''.join(ch for ch in old_string if ch.isalnum())
    print(new_string)
    output(new_string, textToBraille(new_string))

a1.off()
a2.off()
a3.off()
b1.off()
b2.off()
b3.off()

while True:
    try:
        input_state = GPIO.input(26)
        if input_state == False:
            take_read_pic()
