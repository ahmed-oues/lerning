
import os
from gtts import gTTS 
'''
we have to import vocalizer library 
import the nessery biblio for sleep timer 
'''


'''
run all the program evry 10 min 
'''
f = os.popen('upower -i /org/freedesktop/UPower/devices/battery_BAT0')
rs = f.read()
rs = rs.splitlines()
for line in rs:
    if line.__contains__("percentage:"):
        per =line.split("          ")[1]
        print(line.split("          ")[1])
        
        if int(per.replace("%","") )<= 20:
            print ("charge you pc plz!")
            
            # we are going to take the result of 'per' and run it with vocalizer 
          
            language = 'en'
            speech = gTTS(text = "charge you pc plz!", lang = language, slow = False)
            speech.save("text.mp3")
            os.system("vlc text.mp3")
        else:
            print ("ok!")
            language = 'en'
            speech = gTTS(text = "its fine for now ", lang = language, slow = False)
            speech.save("text.mp3")
            os.system("vlc text.mp3")
        os.system("rm text.mp3")    
        