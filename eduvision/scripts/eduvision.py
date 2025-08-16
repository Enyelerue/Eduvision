import cv2
import pyttsx3

speech_engine = pyttsx3.init()

# set speech engine Properties
speech_engine.setProperty('rate', 150)     # Speed (words per minute)
speech_engine.setProperty('volume', 1.0)   # Volume (0.0 to 1.0)

# Open camera
cap = cv2.VideoCapture(0) # opens up the camera. 0 means webcam
detector = cv2.QRCodeDetector()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect and decode
    data, bbox, _ = detector.detectAndDecode(frame)
    if data:
        print("QR Code detected:", data)

        if data == 'a':
            
            letter_a = cv2.imread("A/letter_a.jpg",1) 
            cv2.imshow("Letter A", letter_a)
            speech_engine.say("letter a")
            speech_engine.runAndWait()

        elif data == 'b':

            letter_b = cv2.imread("B/letter_b.jpg") 
            cv2.imshow("Letter B", letter_b)
            speech_engine.say("Letter b")
            speech_engine.runAndWait()
        
        elif data == 'c':

            letter_c =cv2.imread("C/letter_c.jpg")
            cv2.imshow("Letter C", letter_c)
            speech_engine.say("letter c")
            speech_engine.runAndWait()

        elif data == 'd':

            letter_d =cv2.imread("D/letter_d.jpeg")
            cv2.imshow("Letter D", letter_d)
            speech_engine.say("letter d")
            speech_engine.runAndWait()
            

    # Show camera feed
    cv2.imshow("QR Code Scanner", frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
