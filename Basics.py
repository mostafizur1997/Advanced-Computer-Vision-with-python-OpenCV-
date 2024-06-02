import cv2
import mediapipe as mp
import time

# For frame number 1
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
    success, img = cap.read()

    

    cv2.imshow("Image", img)
    cv2.waitKey(0)