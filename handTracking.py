import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraws = mp.solutions.drawing_utils

cTime = 0
pTime = 0

while True:
    success, img = cap.read()
    if not success:
        continue
    
    imgRgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRgb)
    #print(result.multi_hand_landmarks)

    if result.multi_hand_landmarks:
        for landms in result.multi_hand_landmarks:

            for id,lm in enumerate(landms.landmark):
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                #if id == 0:
                    #cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)
                cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)

            mpDraws.draw_landmarks(img, landms, mpHands.HAND_CONNECTIONS)
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}',(10,70), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,255),3 )

    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows