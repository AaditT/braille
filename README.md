# braille - 1st Place [winner](https://devpost.com/software/braille-h7kxzb "winner") at HarkerHacks 2018

https://devpost.com/software/braille-h7kxzb

A Python module that supports conversion between text, image, speech, and braille for developers.

### Inspiration
In the world, 36 million people are blind, and I wanted to create a project that would make blind people's life easier. I was searching for a Python library to assist braille technology, but I found nothing. So, I decided to create my own library to assist developers create projects that integrates braille technology.

### What it does
With this library, developers can simply install and import this library and perform conversions between text, image, speech, and braille.

### Installation 🛠
  Make a project directory ``$ mkdir YOUR_PROJECT_DIRECTORY``
  Install the library from GitHub ``git clone https://www.github.com/AaditT/braille``
  Make sure you work within this directory. Your importation of the braille library may not work if this installation occurs in any other folder

### braille Documentation
1) Download braille.py to a directory and create your project within this directory
2) `import braille`

1) To convert text to braille: `braille.textToBraille('string')`
2) To convert text to speech: `braille.textToSpeech('string')`
3) To convert image to text: `braille.imageToText('image_path')`
4) To convert image to speech: `braille.imageToSpeech('image_path')`
5) To convert image to braille: `braille.imageToBraille('image_path')`
6) To convert a braille array to text: `braille.brailleToTextArray('array')`
7) To convert a braille array to speech (array implementation): `braille.brailleToSpeechArray('list_of_imgs_paths')`

7) To convert a braille array to speech (image implementation): `braille.brailleToSpeechImg('list_of_imgs_paths')`
8) To convert braille images (from [here](https://github.com/AaditT/braille/tree/master/images "here")): `braille.brailleToSpeechImgs('list_of_imgs_paths')`
