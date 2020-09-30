import urllib.parse
import urllib.request
import json

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

import time
import pygame
import os
from os import listdir
from PIL import Image

class stockStory:
    def __init__(self):
        self.accessKey = 'a33594f6ddaadec27d13d7e0465f85da7aacaf1c2e8efbae53f58e94ddfb4f44'
        self.secretKey = '94d9144543d293bc6a868a1e031958ec788e9ce78c31a2bb5d2f2da834ffce8d'
        self.url = 'https://api.unsplash.com/search/photos?'
        self.id = 'c5c49299'

    def photoSearch(self, description):
        print(self.accessKey)
        print(self.secretKey)
        query_parameters = [('query', description), ('client_id', self.accessKey)]
        URL = self.url + urllib.parse.urlencode(query_parameters)
        response = urllib.request.urlopen(URL)

        for i in json.load(response)['results']:
            print(i['urls']['full'])
        response.close()
        print(nouns)

    def loadImages(self, path):
        images = []
        for filename in os.listdir(path):
            images.append((os.path.join(path,filename)))
        return images

if __name__ == "__main__":
    test = stockStory()
    sentence = input('Enter sentence: ')
    nouns = []  # empty to array to hold all nouns

    for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
        if (pos == 'NN' or pos == 'NNP' or pos == 'NNS' or pos == 'NNPS'):
            nouns.append(word)

    key_words = ""
    for word in nouns:
        key_words = key_words + word + " "
    key_words = key_words[:-1]
    test.photoSearch(key_words)


#im = Image.open(img)
#im.show()
