import cv2
from hand import handDetector

# Start video capture
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

detector = handDetector()

while cap.isOpened():
    lmList = []
    success, image = cap.read()
    if not success:
        print("Camera error!!")
        break

    image = detector.findHands(image)
    lmList = detector.findPosition(image)  # [node, x, y]
    closedFinger = 0
    if len(lmList) != 0:
        # check finger long
        for i in range(1, 5):
            if lmList[4 + i*4][2] > lmList[4 + i*4 - 2][2]:
                closedFinger += 1
        # check finger big
        if lmList[4][1] < lmList[4 - 1][1]:
            closedFinger += 1
            # Display image on screen
    cv2.putText(image, str(5 - closedFinger), (140, 140),
                cv2.FONT_HERSHEY_PLAIN, 10, (0, 0, 255), 5)  # (B, G, R)
    cv2.imshow("Hand Detector", image)

    # Exit loop if 'q' key is pressed
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
