from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break

def log_file(msg):
    with open("log.txt","a") as f:
        f.write(f"{msg}{datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_eye = time()
    init_PE = time()

    watersecs=40*60
    eyesecs=30*60
    exsecs=45*60

    while True:
        if time()-init_water>watersecs:
            print("Water dranking time . Enter drank to stop the alarm")
            musiconloop("water.mp3","drank")
            init_water=time()
            log_file("Drank water at")

        if time()-init_eye>eyesecs:
            print("Eye rest time . Enter Goodeye to stop the alarm")
            musiconloop("eyes.mp3","Goodeye")
            init_eye=time()
            log_file("Take eyerest at")

        if time()-init_PE>exsecs:
            print("Exercise time . Enter Done to stop the alarm")
            musiconloop("exercise.mp3","Done")
            init_PE=time()
            log_file("Exercise done at")

