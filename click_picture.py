import cv2



def cam():

    cap = cv2.VideoCapture(0)

    face_c=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    while cap.isOpened():
        status,frame = cap.read()

        cv2.imwrite('face.jpg',frame)
        face=face_c.detectMultiScale(frame, scaleFactor=1.05, minNeighbors=5)

        for x,y,w,h in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

        cv2.imshow('webcam',frame)
        #click q to quit
        key= cv2.waitKey(1) & 0xFF
        if key==ord('q'):
                break

        # click c to capture image
        if key==ord('c'):
             if len(face)>1:
                    print("Too many faces")
             elif len(face)==0:
                    print("No faces to capture")
             elif len(face)==1:
                    print("Successfully captured")
                    img = cv2.imread('face.jpg',1)
                    cv2.imshow('photo',img)
                    # attendence() # call this function to mark attendence
                    continue
             




    cv2.destroyAllWindows()
    cap.release()

cam()
