import cv2

cam=cv2.VideoCapture(0)

for i in range(30):
 if cam.isOpened():
    print("working")
    status, frame=cam.read()

    if i==9:
        cv2.imwrite('face.jpg' , frame)
    else:
        continue
    if cv2.waitKey(1) or 0xFF==ord('q'):
        break

cv2.destroyAllWindows()
cam.release()
