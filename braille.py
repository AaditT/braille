
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
    a: "/Users/aadittrivedi/Desktop/braille/a.png",
    b: "/Users/aadittrivedi/Desktop/braille/b.png",
    c: "/Users/aadittrivedi/Desktop/braille/c.png",
    d: "/Users/aadittrivedi/Desktop/braille/d.png",
    e: "/Users/aadittrivedi/Desktop/braille/e.png",
    f: "/Users/aadittrivedi/Desktop/braille/f.png",
    g: "/Users/aadittrivedi/Desktop/braille/g.png",
    h: "/Users/aadittrivedi/Desktop/braille/h.png",
    i: "/Users/aadittrivedi/Desktop/braille/ipng",
    j: "/Users/aadittrivedi/Desktop/braille/j.png",
    k: "/Users/aadittrivedi/Desktop/braille/k.png",
    l: "/Users/aadittrivedi/Desktop/braille/l.png",
    m: "/Users/aadittrivedi/Desktop/braille/m.png",
    n: "/Users/aadittrivedi/Desktop/braille/n.png",
    o: "/Users/aadittrivedi/Desktop/braille/o.png",
    p: "/Users/aadittrivedi/Desktop/braille/p.png",
    q: "/Users/aadittrivedi/Desktop/braille/q.png",
    r: "/Users/aadittrivedi/Desktop/braille/r.png",
    s: "/Users/aadittrivedi/Desktop/braille/s.png",
    t: "/Users/aadittrivedi/Desktop/braille/t.png",
    u: "/Users/aadittrivedi/Desktop/braille/u.png",
    v: "/Users/aadittrivedi/Desktop/braille/v.png",
    w: "/Users/aadittrivedi/Desktop/braille/w.png",
    x: "/Users/aadittrivedi/Desktop/braille/x.png",
    y: "/Users/aadittrivedi/Desktop/braille/y.png",
    z: "/Users/aadittrivedi/Desktop/braille/z.png",
    void: "/Users/aadittrivedi/Desktop/braille/void.png",
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