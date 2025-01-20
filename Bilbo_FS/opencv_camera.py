import cv2

webCam = cv2.VideoCapture(0)

while True:
    ret, frame = webCam.read()

    cv2.imshow('WebCam', frame)
    if cv2.waitKey(1) == ord('q'):
        break

webCam.release()
cv2.destroyAllWindows()
