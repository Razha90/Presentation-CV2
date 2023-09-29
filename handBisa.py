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
    
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Koordinat landmark untuk jari tengah (id 8) dan jari telunjuk (id 12)
            x_middle = hand_landmarks.landmark[8].x
            y_middle = hand_landmarks.landmark[8].y
            x_index = hand_landmarks.landmark[12].x
            y_index = hand_landmarks.landmark[12].y
            
            # Hitung jarak antara landmark jari tengah dan jari telunjuk
            distance = ((x_middle - x_index) ** 2 + (y_middle - y_index) ** 2) ** 0.5
            
            # Anda dapat menyesuaikan ambang batas ini sesuai kebutuhan
            if distance < 0.03:  # Sesuaikan ambang batas sesuai kebutuhan
                cv2.putText(img, "Peace", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)
            else:
                cv2.putText(img, "Rock", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)

            mpDraws.draw_landmarks(img, hand_landmarks, mpHands.HAND_CONNECTIONS)
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 3)

    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
