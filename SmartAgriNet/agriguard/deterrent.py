import pygame
import time
import os

pygame.mixer.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def deterrent_action(label):

    try:

        if label == "person":
            filename = "siren.mpeg"

        elif label == "dog":
            filename = "tiger_roar.mpeg"

        elif label == "cow":
            filename = "alert.mpeg"

        else:
            filename = "cracker.mpeg"

        sound_path = os.path.join(BASE_DIR, "sounds", filename)

        print("Playing:", sound_path)

        pygame.mixer.music.load(sound_path)

        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(1)

    except Exception as e:
        print("Sound Error:", e)