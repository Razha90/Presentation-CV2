import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False, maxHands = 2, modelComplex=1,detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplex
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplex,self.detectionCon, self.trackCon)

        
        self.mpDraws = mp.solutions.drawing_utils
        
    def findHands(self, img, draw=True):
            imgRgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            self.result = self.hands.process(imgRgb)

            if self.result.multi_hand_landmarks:
                for landms in self.result.multi_hand_landmarks:
                    if draw:    
                        self.mpDraws.draw_landmarks(img, landms, self.mpHands.HAND_CONNECTIONS)
            return img
    
    def findPosition(self, img, handNo=0, draw= True ):
        
        lmList = []
        if self.result.multi_hand_landmarks:
            myHand = self.result.multi_hand_landmarks[handNo]            

            for id,lm in enumerate(myHand.landmark):
                    #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx,cy), 5, (255,0,255), cv2.FILLED)
        
        return lmList

def main():
    cap = cv2.VideoCapture(0)
    cTime = 0
    pTime = 0
    detector = handDetector()
    while True:
        
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img) 
        if len(lmList) !=0:
            print(lmList[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}',(10,70), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,255),3 )
        
        cv2.imshow("image", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == "__main__":
    main()