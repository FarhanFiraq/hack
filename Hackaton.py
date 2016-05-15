#############################################################################
###################################Carlite###################################
#################################By Firaq & Rajesh###################################


import numpy as np
import cv2
import time
import numpy as np
import pyaudio  
import wave
import sys
print '                                 MUSIC SYSTEM          '
print '####################################################################'
print '--------------------------------Honk Activate---------------------- '
print '####################################################################'
cap = cv2.VideoCapture(1)                            #capture frame via webcam thats my Reciever
def horn():

          CHUNK = 6024
          #opening the horn audio file
         
          wf = wave.open('center.wav', 'rb')

          # instantiate PyAudio library
          f = pyaudio.PyAudio()

          # opening the audio stream 
          bitstream = f.open(format=f.get_format_from_width(wf.getsampwidth()), #getting channel,rate,frame rate
                          channels=wf.getnchannels(),
                          rate=wf.getframerate(),
                          output=True)

          # read audio chunks
          data = wf.readframes(CHUNK)

          # play horn
          while len(data) > 0:
              bitstream.write(data)
              data = wf.readframes(CHUNK)
              time.sleep(0.05)
              start()

def start():
            ret, img = cap.read()                    # Capture frame-by-frame            
            x, y, color = img.shape                  # it returns an array of Blue, Green, Red values
            B,G,R = img[x/2,y/2]                     #tuple array Extracted

            
            if R>200:                                #Threshold for high intensity Laser beam from transmitter       
                    print 'honk..!Vehicle Behind you '
                    horn()
                    
            else:
                          main()
def main():
    while(1):                                        #initialised 
        ret, img = cap.read()
        x, y, color = img.shape
        B,G,R = img[x/2,y/2]                        # frame for testing light intensity
        if R>250:
                    
            start()

main()

    
    

############################################
## Close and exit
cv2.destroyAllWindows()
############################################
    


