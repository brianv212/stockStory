#graphics.py
import time
import pygame
import os
import shutil
from os import listdir
from PIL import Image
import urllib.request
from io import BytesIO

def loadFiles(path):
    images = []
    for filename in os.listdir(path):
        images.append((os.path.join(path,filename)))
    return images

def loadImage(image,screen):
    pygame_image = pygame.image.load(image)
    picture = pygame.transform.scale(pygame_image, (700,500))
    screen.blit(picture, (0,0))
    pygame.display.flip()

def loadSound(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play()
    while (pygame.mixer.music.get_busy() == True):
        continue

def createStory(images,sounds):
    pygame.init()

    audio_files = loadFiles(sounds)
    picture_files = loadFiles(images)
    
    screen = pygame.display.set_mode((700,500))
    for image,sound in zip(picture_files,audio_files):
        loadImage(image,screen)
        loadSound(sound)
    time.sleep(3)
    pygame.quit()

def make_directory(self) -> os.path :
    dir = f"C:{os.environ['HOMEPATH']}\\Desktop\\StockImages"
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

def download_imgs(urlList: [(str,int,str)]):
    dir = make_img_directory()
    tens = 0
    ones = 0
    
    for i in urlList:
        a = dir[:]
        if ones == 10:
            ones = 0
            tens += 1
        b = os.path.join(a,f'{tens}{ones}.jfif')
        url = i[0]
        urllib.request.urlretrieve(url, b)
        ones += 1
    return dir

def make_img_directory() -> os.path :
    #C:\Users\jiali\Desktop
    dir = f"c:{os.environ['HOMEPATH']}\\Desktop\\StockImages"
    if not os.path.exists(dir):
        os.mkdir(dir)
        #print("The directory has been created")
    else:
        shutil.rmtree(dir)
        #os.rmdir(dir)
        #print("The directory has been removed")
        os.mkdir(dir)
        #print("The directory has been created again")

    #print("this is dir: ", dir)
    return dir


if __name__ == "__main__":
    #IO Paths
    path = r"C:\Users\Brian\Desktop\Cobblestone"
    imgs = loadFiles(path)

    pygame.init()
    screen = pygame.display.set_mode((700,500)) # Whatever resolution you want.
    for img in imgs:
        image = 'https://images.unsplash.com/photo-1579109113182-17819330295f?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&ixid=eyJhcHBfaWQiOjExMzUyNX0'
        image_str = urlopen(image).read()
        image_file = BytesIO(image_str)
        image2 = pygame.image.load(image_file)
        picture = pygame.transform.scale(image2, (700, 500))
        screen.blit(picture, (0,0))
        pygame.display.set_caption('Hello')
        pygame.display.flip()
        time.sleep(1)
    pygame.quit()
