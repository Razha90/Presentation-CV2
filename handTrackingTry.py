import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraws = mp.solutions.drawing_utils

cTime = 0
pTime = 0
img_scale = 1.5
label = ""

while True:
    success, img = cap.read()
    if not success:
        continue
    
    imgRgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRgb)

    if result.multi_hand_landmarks:
        for landms in result.multi_hand_landmarks:
            if landms.landmark[0].x < landms.landmark[5].x:
                label = "Kiri"
            else:
                label = "Kanan"
            left_top = (int(landms.landmark[0].x * img.shape[1]), int(landms.landmark[0].y * img.shape[0]))
            right_bottom = (int(landms.landmark[5].x * img.shape[1]), int(landms.landmark[5].y * img.shape[0]))
            
            for id,lm in enumerate(landms.landmark):
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                cv2.circle(img, (cx,cy), 5, (255,0,255), cv2.FILLED)
                
            cv2.rectangle(img, left_top, right_bottom, (0, 255, 0), 4)
            mpDraws.draw_landmarks(img, landms, mpHands.HAND_CONNECTIONS)
            cv2.putText(img, label, (left_top[0], left_top[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}',(10,70), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,255),3 )

    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    
cap.release()
cv2.destroyAllWindows