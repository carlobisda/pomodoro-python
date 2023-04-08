
import win32com.client
import schedule
import time
import os
from progress.bar import Bar

#functions
def breakNow():
    speaker.Speak(te2)
    choice = input("Restart (Y) or (N)")
    if choice == "Y":
        print("Timer will restart")
        speaker.Speak(te1)
        bar = Bar('Timer')
        for i in range(100):
            bar.next()
            time.sleep(15)
        bar.finish()
    else:
        print("session end")
        quit()

#variables  
te1="deep work begins now"
te2="5 minute break"
speaker=win32com.client.Dispatch("SAPI.SpVoice")

#init
speaker.Speak(te1)
print("timer initiated")
schedule.every(25).minutes.do(breakNow)
bar = Bar('Timer')
for i in range(100):
    bar.next()
    time.sleep(15)
bar.finish()

while True:
    #loop running
    schedule.run_pending()
    time.sleep(1)