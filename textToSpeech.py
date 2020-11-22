#textToSpeech.py
from gtts import gTTS
import os
import shutil


class TextToSpeech:
    def __init__(self, story_parts: [str]):
        self.language = "en"
        self._story = story_parts
        self.dir = self._make_directory()
        self.tens = 0
        self.ones = 0

    def text_to_speech(self):
        for part in self._story:
            sound = gTTS(text = part, lang = self.language, slow = True)
            if self.ones == 10:
                self.ones = 0
                self.tens += 1
            file_name = str(self.tens) + str(self.ones) + ".mp3"
            file = os.path.join(self.dir, file_name)
            sound.save(file)
            self.ones += 1

    def _make_directory(self) -> os.path :
        #C:\Users\jiali\Desktop
        dir = f"{os.getcwd()}\\StockStory"
        if not os.path.exists(dir):
            os.mkdir(dir)
            #print("\nThe directory has been created")
        else:
            shutil.rmtree(dir)
            #os.rmdir(dir)
            #print("\nThe directory has been removed")
            os.mkdir(dir)
            #print("The directory has been created again")

        #print("this is dir: ", dir)
        return dir

if __name__ == '__main__':
    a.text_to_speech()
