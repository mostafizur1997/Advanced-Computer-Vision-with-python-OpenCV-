import cv2
import mediapipe as mp
import time

# For frame number 1
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
# create a hands object
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


while True:
    success, img = cap.read()
    # hands object only works with RGB images
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)
    
    # if multi_hand_landmarks is True
    if results.multi_hand_landmarks:
        #muliple hands extract each hand one by one
        for handLMS in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLMS)
            
            
    
    

    

    cv2.imshow("Image", img)
    cv2.waitKey(0)