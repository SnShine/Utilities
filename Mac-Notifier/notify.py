#!/bin/bash

import time
import os

def log_time():
    return time.strftime("[%Y-%m-%d %H:%M:%S] ")

print("\n")
print(log_time()+ "Started the program")
time.sleep(5)

# body exercise
date_now= int(time.strftime("%d"))
if date_now% 3== 0:
    # upper body
    print(log_time()+ "upper body")
    os.system(''' osascript -e 'display notification "Let me see what those hands can do today." with title "It is exercise time, baby!"' ''')
    os.system("say 'Hey master, let me see what your hands can do today!'")
    os.system("say 'What are you gonna do about your man boobs. Do you love them?'")
    time.sleep(2)
    os.system("say 'Hello master, I love watching you while your are exercising.'")
    os.system("say 'Please do it for me. Please. I can give you whatever you want. Please.'")

elif date_now% 3== 1:
    # lower body
    print(log_time()+ "lower body")
    os.system(''' osascript -e 'display notification "Let me see what you can do to get nice abs." with title "It is exercise time, baby!"' ''')
    os.system("say 'Hey master, let me see what you can do to get nice abs!'")
    time.sleep(2)
    os.system("say 'Hello master, I love watching you while your are exercising.'")
    os.system("say 'Please do it for me. Please. I can give you whatever you want. Please.'")

else:
    # middle body
    print(log_time()+ "middle body")
    os.system(''' osascript -e 'display notification "Let me see what those fucking legs can do today." with title "It is exercise time, baby!"' ''')
    os.system("say 'Hey master, let me see what your fucking legs can do today!'")
    time.sleep(2)
    os.system("say 'Hello master, I love watching you while your are exercising.'")
    os.system("say 'Please do it for me. Please. I can give you whatever you want. Please.'")

time.sleep(3)
# open video songs
print(log_time()+ "open video songs")
os.system("say 'Let me open some video songs, so you can start working out!'")
time.sleep(1)
os.system("/Applications/VLC.app/Contents/MacOS/VLC -Z ~/Documents/videos_at_startup/")


while True:
    time_now= time.strftime("%H:%M")
    day_now= time.strftime("%w")
    hour_now, min_now= time_now.split(":")
    # print(hour_now, min_now)

    if hour_now== "07" and min_now== "15" and (day_now== 2 or day_now== 3 or day_now== 4):
        # clean my room, bathing
        print(log_time()+ "clean my room, bathing at 07:15")
        os.system(''' osascript -e 'display notification "Can you just clean your room and go have a bath." with title "Take a bath, bitch!"' ''')
        os.system("say 'Can you just stop what you are doing right now and clean your room?'")
        time.slweep(5)
        os.system("say 'Have a bath right after doing that. Are you thinking of me in naked?'")

    if hour_now== "08" and min_now== "15" and (day_now== 1 or day_now== 5 or day_now== 6):
        # clean my room and bathing
        print(log_time()+ "clean my room and bathing at 08:15")
        os.system(''' osascript -e 'display notification "Can you just clean your room and go have a bath." with title "Take a bath, bitch!"' ''')
        os.system("say 'Can you just stop what you are doing right now and clean your room?'")
        time.slweep(5)
        os.system("say 'Have a bath right after doing that. Are you thinking of me in naked?'")

    # if hour_now== "18" and min_now== "30":
    #     # honey
    #     print(log_time()+ "honey")
    #     os.system(''' osascript -e 'display notification "This will help a lot in long run!" with title "It is honey time, master."' ''')
    #     os.system("say 'Find the honey, and use it. It is that simple.'")

    if hour_now== "19" and min_now== "00":
        # call mom
        print(log_time()+ "call mom")
        os.system(''' osascript -e 'display notification "Do not close this unless you call or message mon!" with title "Call mom."' ''')
        os.system("say 'Call mom or message mom. You can't close this notification unless you did so.")

    if hour_now== "23" and min_now== "45":
        if day_now== 1 or day_now== 4:
            # hair oil
            print(log_time()+ "hair oil")
            os.system(''' osascript -e 'display notification "Never ever miss this if you want black hair." with title "Dabur amla or Navaratna?"' ''')
            os.system("say 'Oh, what happened to your hair? That is it, you need to put some fucking oil to it.'")
            sleep(2)
        # eye exercise
        print(log_time()+ "eye exercise")
        os.system(''' osascript -e 'display notification "Do you want to increase the blood flow in your brain? Then do this." with title "Eye exercise."' ''')
        os.system("say 'Get you lazy ass up and do this eye exercise right now, master!'")

    if hour_now== "23" and min_now== "55":
        # write diary
        print(log_time()+ "write diary")
        os.system(''' osascript -e 'display notification "Write some random shit, already." with title "Diary, bro!"' ''')
        os.system("say 'Five years later, this is what you want very badly. Please write atlease 3 lines of what happened today?'")


    # gonna sleep
    # print(log_time()+ "gonna sleep")
    time.sleep(59.5)
