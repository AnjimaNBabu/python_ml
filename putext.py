import cv2
vid = cv2.VideoCapture(0)
while True :
    ret,frame = vid.read()
    Image = cv2.putText(frame, 'Welcome to MI class',(50,60), cv2.FONT_HERSHEY_SIMPLEX,1,(256,100,200),2)
    cv2.imshow('live video', Image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()