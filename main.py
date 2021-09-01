import numpy as np
import time
import cv2
from cvzone.HandTrackingModule import HandDetector
import pyglet


cap =cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

window = pyglet.window.Window()
detector =HandDetector(detectionCon=0.8)

keys=[["C","D",'E',"F","G","A","B","C","D","E","F","G","A","B"],["C#","D#","F#","G#","A#","C#","D#","F#","G#","A#"]]

class Button():
    def __init__(self,pos,text,size,color):
        self.pos=pos
        self.size=size
        self.text=text
        self.color=color
buttonList=[]
for i in range(len(keys)):
    for j,key in enumerate(keys[i]):   
        if i==0:
            buttonList.append(Button([38*j+15,80],key,[35,100],(255,255,255)))
        else:
            buttonList.append(Button([(40+j)*j+25,80],key,[35,50],(0,0,0)))    

def playkeys(button):
    if button.text=="A":
            
        effectA=pyglet.resource.media("A.wav",streaming=False)
        effectA.play()
                
                
    elif button.text=="B":
            
        effectB=pyglet.resource.media("B.wav",streaming=False)
        effectB.play()
                
    elif button.text=="C":
            
        effectC=pyglet.resource.media("C.wav",streaming=False)
        effectC.play()
    elif button.text=="D":
            
        effectD=pyglet.resource.media("D.wav",streaming=False)
        effectD.play()
    elif button.text=="E":
            
        effectE=pyglet.resource.media("E.wav",streaming=False)
        effectE.play()
        

    elif button.text=="F":
            
        effectF=pyglet.resource.media("F.wav",streaming=False)
        effectF.play()
    elif button.text=="G":
            
        effectG=pyglet.resource.media("G.wav",streaming=False)
        effectG.play()                  


def drawAll(img,buttonList):
    for button in buttonList:
        x,y=button.pos
        w,h=button.size
        colorr=button.color
        cv2.rectangle(img,button.pos,(x+w,y+h),colorr,cv2.FILLED)
        cv2.putText(img,button.text,(x+10,y+h-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(214,0,220),2)
    return img    

while True:
    success,img=cap.read()



    img= detector.findHands(img)
    lmlist,bboxInfo=detector.findPosition(img)
    img=drawAll(img,buttonList)
    if lmlist:        #hand is there
        for button in buttonList:
            x,y=button.pos
            w,h=button.size
            
            for f in [4,8,12,16,20]:

                 if x<lmlist[f][0]<x+w and y<lmlist[f][1]<y+h:
                     l,_,_=detector.findDistance(f,f-3,img,draw=False)
                     if l<120:
                         #cv2.rectangle(img,button.pos,(x+w,y+h),(80,9,78),cv2.FILLED)
                         playkeys(button)

                         

                     



    


    cv2.imshow("IMAGE",img)
    cv2.waitKey(1)
   



