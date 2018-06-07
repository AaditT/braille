
#!/usr/local/bin/python3
# -*- coding: utf8 -*-

# Written by Aadit Trivedi
# June 6, 2018
# Braille Library

# # Dependencies
# 1) pip3 install SpeechRecognition
# 2) pip3 install numpy

# Upload to GitHub


import speech_recognition as sr
import numpy as np

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

void = [[0,0],[0,0],[0,0]]
a = [[1,0],[0,0],[0,0]]
b = [[1,0],[1,0],[0,0]]
c = [[1,1],[0,0],[0,0]]
d = [[1,1],[0,1],[0,0]]
e = [[1,0],[0,1],[1,0]]
f = [[1,1],[1,0],[0,0]]
g = [[1,1],[1,1],[0,0]]
h = [[1,0],[1,1],[0,0]]
i = [[0,1],[1,0],[1,0]]
j = [[0,1],[1,1],[0,0]]
k = [[1,0],[0,0],[1,0]]
l = [[1,0],[1,0],[1,0]]
m = [[1,1],[0,0],[1,0]]
n = [[1,1],[0,1],[1,0]]
o = [[1,0],[0,1],[1,1]]
p = [[1,1],[1,0],[1,0]]
q = [[1,1],[1,1],[1,0]]
r = [[1,0],[1,1],[1,0]]
s = [[0,1],[1,0],[1,0]]
t = [[0,1],[1,1],[1,0]]
u = [[1,0],[0,0],[1,1]]
v = [[1,0],[1,0],[1,1]]
w = [[0,1],[0,1],[1,1]]
x = [[1,1],[0,0],[1,1]]
y = [[1,1],[0,1],[1,1]]
z = [[1,0],[0,1],[1,1]]

# Update dictionary based on GitHub file path skeleton
letterToImgPath = {
    a: "braille/images/a.png",
    b: "braille/images/b.png",
    c: "braille/images/c.png",
    d: "braille/images/d.png",
    e: "braille/images/e.png",
    f: "braille/images/f.png",
    g: "braille/images/g.png",
    h: "braille/images/h.png",
    i: "braille/images/ipng",
    j: "braille/images/j.png",
    k: "braille/images/k.png",
    l: "braille/images/l.png",
    m: "braille/images/m.png",
    n: "braille/images/n.png",
    o: "braille/images/o.png",
    p: "braille/images/p.png",
    q: "braille/images/q.png",
    r: "braille/images/r.png",
    s: "braille/images/s.png",
    t: "braille/images/t.png",
    u: "braille/images/u.png",
    v: "braille/images/v.png",
    w: "braille/images/w.png",
    x: "braille/images/x.png",
    y: "braille/images/y.png",
    z: "braille/images/z.png",
    void: "braille/images/void.png",
}

def textToBraille(c_string):
    for char in c_string:
        char = char.lower()
        if char == "a": print(a)
        elif char == "b": print(b)
        elif char == "c": print(c)
        elif char == "d": print(d)
        elif char == "e": print(e)
        elif char == "f": print(f)
        elif char == "g": print(g)
        elif char == "h": print(h)
        elif char == "i": print(i)
        elif char == "j": print(j)
        elif char == "k": print(k)
        elif char == "l": print(l)
        elif char == "m": print(m)
        elif char == "n": print(n)
        elif char == "o": print(o)
        elif char == "p": print(p)
        elif char == "q": print(q)
        elif char == "r": print(r)
        elif char == "s": print(s)
        elif char == "t": print(t)
        elif char == "u": print(u)
        elif char == "v": print(v)
        elif char == "w": print(w)
        elif char == "x": print(x)
        elif char == "y": print(y)
        elif char == "z": print(z)
        elif char == " ": print(void)

def detectWhileSpeaking():
    rec = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        rec.adjust_for_ambient_noise(source)
        audio = rec.listen(source)
        return(str(rec.recognize_wit(audio, wit_api_key)))

def speechToBraille():
    textToBraille(detectWhileSpeaking())
