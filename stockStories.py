#stockStories.py
import urllib.parse
import urllib.request
import json
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

import os

import TextBox
from textToSpeech import TextToSpeech
import Graphics

class stockStory:
    def __init__(self):
        self.accessKey = os.environ['STOCK_API_PUB']
        self.secretKey = os.environ['STOCK_API_SEC']
        self.url = 'https://api.unsplash.com/search/photos?'
        self.id = 'c5c49299'
        self.Stopwords = set(stopwords.words('english'))
        self.urlList = [] #url, index, word
        self.default = self._default()

    def _default(self):
        query_parameters = [('query', 'black'), ('client_id', self.accessKey)]
        URL = self.url + urllib.parse.urlencode(query_parameters)
        response = urllib.request.urlopen(URL)
        res = json.load(response)['results']
        default = (res[0]['urls']['full'])
        response.close()
        return default
        
    def photoSearch(self, description):
        count = 0

        first_word_unimportant = False
        importantWords = []
        importantWords.append((description.split()[0],0))
        
        for word in description.split():
            if word not in self.Stopwords:
                if count != 0:
                    first_word_unimportant = True
                    importantWords.append((word,count))
            count += 1
                
        for word,count in importantWords:
            query_parameters = [('query', word), ('client_id', self.accessKey)]
            URL = self.url + urllib.parse.urlencode(query_parameters)
            response = urllib.request.urlopen(URL)
            res = json.load(response)['results']
            if len(res) > 0:
                if first_word_unimportant == True:
                    self.urlList.append((self.default,count,word))
                    first_word_unimportant = False
                else:
                    self.urlList.append((res[0]['urls']['full'],count,word))
            else:
                self.urlList.append((self.default,count,word))
            response.close()

    def splitStory(self,story):
        audio_lines = []
        split_story = story.split()
        story_fragment = ""

        tracker = 0
        
        for i in split_story:
            if i == self.urlList[tracker][2]:
                if len(story_fragment) == 0:
                    story_fragment += i
                    tracker += 1
                else:
                    audio_lines.append(story_fragment)
                    story_fragment = ""
                    story_fragment += i
                    tracker += 1
                    
            else:             
                story_fragment += " "
                story_fragment += i
        audio_lines.append(story_fragment)
        return audio_lines
        

if __name__ == "__main__":
    test = stockStory()

    story = TextBox.text_box()
    
    test.photoSearch(story)
    images = Graphics.download_imgs(test.urlList)

    audio_lines = test.splitStory(story)
    make_audio = TextToSpeech(audio_lines)
    make_audio.text_to_speech()

    Graphics.createStory(images,make_audio.dir)
