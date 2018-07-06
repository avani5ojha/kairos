import cv2

def detect():
    cam=cv2.VideoCapture(0)
    face_c=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    while cam.isOpened():
        x, f=cam.read()
        face=face_c.detectMultiScale(f, scaleFactor=1.05, minNeighbors=5)

        for x,y,w,h in face:
            cv2.rectangle(f,(x,y),(x+w,y+h),(255,0,0),3)

        cv2.imshow("webcam",f)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
        if cv2.waitKey(1) & 0xFF==ord('w'):
            capture_image()
    cv2.destroyAllWindows()
    cam.release()




def capture_image():
    cam=cv2.VideoCapture(0)

    for i in range(30):
     if cam.isOpened():
        print("working")
        status, frame=cam.read()

        if i==9:
            cv2.imwrite('face.jpg' , frame)
            detect()
        else:
            continue
        if cv2.waitKey(1) or 0xFF==ord('q'):
            break

    cv2.destroyAllWindows()
    cam.release()


detect()
