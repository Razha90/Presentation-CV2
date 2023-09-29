import cv2
import mediapipe as mp
import time
import handTrackingModule as htm
from keyboardReact import macros

cap = cv2.VideoCapture(0)
cTime = 0
pTime = 0
detector = htm.handDetector()
while True:
        
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img) 
    if len(lmList) !=0:
        tengahAtas = lmList[12]
        tengahBawah = lmList[9]
        telunjukAtas = lmList[8]
        telunjukBawah = lmList[5]
        manisAtas = lmList[16]
        manisBawah = lmList[13]
        kelingkingAtas = lmList[20]
        kelingkingBawah = lmList[17]
        jempolAtas = lmList[4]
        jempolBawah = lmList[1]
        if (tengahAtas[2] < tengahBawah[2] and
            telunjukAtas[2] < telunjukBawah[2] and
            manisAtas[2] > manisBawah[2] and
            kelingkingAtas[2] > kelingkingBawah[2] and
            jempolAtas[1] > jempolBawah[1]):
            print("Tengah Atas:", tengahAtas[2])
            print("Tengah Bawah:", tengahBawah[2])
            print("Manis Atas:", manisAtas[2])
            print("Manis Bawah:", manisBawah[2])
            print("Kelingking Atas:", kelingkingAtas[2])
            print("Kelingking Bawah:", kelingkingBawah[2])
            print("Telunjuk Atas:", telunjukAtas[2])
            print("Telunjuk Bawah:", telunjukBawah[2])
            print("Jempol Atas:", jempolAtas[1])
            print("Jempol Bawah:", jempolBawah[1])
            print('kanan')
            macros.rightarrow()
            
        if(tengahAtas[2] > tengahBawah[2] and
           manisAtas[2] > manisBawah[2] and 
           kelingkingAtas[2] < kelingkingBawah[2] and
           telunjukAtas[2] < telunjukBawah[2] and 
           jempolAtas[1] > jempolBawah[1]):
           print("Tengah Atas:", tengahAtas[2])
           print("Tengah Bawah:", tengahBawah[2])
           print("Manis Atas:", manisAtas[2])
           print("Manis Bawah:", manisBawah[2])
           print("Kelingking Atas:", kelingkingAtas[2])
           print("Kelingking Bawah:", kelingkingBawah[2])
           print("Telunjuk Atas:", telunjukAtas[2])
           print("Telunjuk Bawah:", telunjukBawah[2])
           print("Jempol Atas:", jempolAtas[1])
           print("Jempol Bawah:", jempolBawah[1])
           print('kiri')
           macros.leftarrow()
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}',(10,70), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,255),3 )
        
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break