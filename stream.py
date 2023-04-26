import cv2
vid = cv2.VideoCapture(0)
while(True):
    ret,frame=vid.read()
    cv2.imshow('live video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("I'm here")
        pass
vid.release()
cv2.destroyAllWindows()