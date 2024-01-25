import cv2

def webcam_foto(speicherort): 
    cam = cv2.VideoCapture(0)
    _, bild = cam.read()
    cv2.imwrite(speicherort, bild)
    cam.release()
# webcam_foto("webcam_bild.jpg")
