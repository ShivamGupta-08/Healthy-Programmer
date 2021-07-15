from pygame import mixer
import time
def adjust_vol(vol):
    return mixer.music.set_volume(vol)
def water_song_stop(wat):
    while True:
        if wat == "Drank":
            mixer.music.stop()
            mixer.music.unload()
            print("Successful")
            with open("water.txt", "a")as f:
                f.write(str([str(time.asctime())]) + "Drank water!" + "\n")
            break
        else:
            "Error"
        continue
    return mixer.music.stop()
def ey_song_stop(ey):
    while True:
        if ey == "EyDone":
            mixer.music.stop()
            mixer.music.unload()
            print("Successful")
            with open("eye.txt", "a")as e:
                e.write(str([str(time.asctime())]) + "Eye Exercise Done!" + "\n")
            break
        else:
            "Error"
        continue
    return mixer.music.stop()
def ex_song_stop(ex):
    while True:
        if ex == "ExDone":
            mixer.music.stop()
            mixer.music.unload()
            print("Successful")
            with open("exercise.txt", "a")as x:
                x.write(str([str(time.asctime())]) + "Physical Exercise Done!" + "\n")
            break
        else:
            "Error"
        continue
    return mixer.music.stop()
mixer.init()
print("\t \tThis is a program that keep you healthy")
print("Choose Your Comfortable Volume")
vol = float(input())
adjust_vol(vol)
print("Preview  (If You Are Comfortable With This Volume) If Yes Then Type Y Or If No Then Type N")
mixer.music.load("water.mp3")
mixer.music.play()
like = str(input())
while like=="N":
    mixer.music.stop()
    print("Choose Your Comfortable Volume")
    vol = float(input())
    adjust_vol(vol)
    print("Preview  (If You Are Comfortable With This Volume) If Yes Then Type Y Or If No Then Type N")
    mixer.music.play()
    like = str(input())
    continue
mixer.music.unload()
print("Your targets\nTo drink a total of 3.5-liter water after some time interval between 9-5 pm (means "
      "437.5ml/hr).\nTo "
      "do "
      "eye exercise after every 30 minutes.\nTo perform physical activity after every 45 minutes.")

print("Your Time Starts Now!")
wate = time.time()
eye = time.time()
ex = time.time()
while True:
    #------------water-----------------
    drink_time = time.time() - wate
    if drink_time>3600:
        mixer.music.load("water.mp3")
        mixer.music.play(-1)
        print("Its time for drinking water")
        print("Type ""Drank"" for stopping the music")
        wat = str(input())
        water_song_stop(wat)
    #------------------eye----------------------
    eye_time = time.time() - eye
    if eye_time > 1800:
        mixer.music.load("eyes.mp3")
        mixer.music.play(-1)
        print("Its time for eyes exercise")
        print("Type ""EyDone"" for stopping the music")
        ey = str(input())
        ey_song_stop(ey)
    #-------------ex-----------
    ex_time = time.time() - ex
    if ex_time > 2700:
        mixer.music.load("physical.mp3")
        mixer.music.play(-1)
        print("Its time for physical exercise")
        print("Type ""ExDone"" for stopping the music")
        ex = str(input())
        ex_song_stop(ex)
