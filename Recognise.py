import cv2
import smtplib
#import numpy as np;
import xlwrite
#import firebase
import time
#import sys
#from playsound import playsound

start = time.time()
period = 8
face_cas = cv2.CascadeClassifier(
    'D:\python\FaceRecog2\pythonProject\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0);

recognizer = cv2.face.LBPHFaceRecognizer_create();
recognizer.read('D:\python\FaceRecog2\pythonProject\Trainer\Trainer.yml.txt');
flag = 0;
id = 0;
filename = 'filename';
dict = {
    'item1': 1
}
 #font = cv2.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 5, 1, 0, 1, 1)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cap.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = face_cas.detectMultiScale(gray, 1.3, 7);
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2);
        id, conf = recognizer.predict(roi_gray)

        if (conf > 50):
            if (id == 1):
                id = 'Vallabh'
                if ((str(id)) not in dict):
                    filename = xlwrite.output('attendance', 'class1', 1, id, 'yes');
                    dict[str(id)] = str(id);
                    Rec_email = "vallabhbhat612@gmail.com"

            elif (id == 2):
                id = 'Sakshi'
                if ((str(id)) not in dict):
                    filename = xlwrite.output('attendance', 'class1', 2, id, 'yes');
                    dict[str(id)] = str(id);
                    Rec_email = "Vallabhavbhat@gmail.com"

            elif (id == 3):
                id = 'vijay'
                if ((str(id)) not in dict):
                    filename = xlwrite.output('attendance', 'class1', 3, id, 'yes');
                    dict[str(id)] = str(id)

            elif (id == 4):
                id = 'Deepa'
                if ((str(id)) not in dict):
                    filename = xlwrite.output('attendance', 'class1', 4, id, 'yes');
                    dict[str(id)] = str(id)
        else:
            id = 'Unknown, can not recognize'
            flag = flag + 1
            break
        cv2.putText(img, str(id) , (250,450), font, 1, (120, 255, 120), 2)
        #cv2.putText(img, str(id) + "" +'Present For Class', (x, y - 10), font, 0.55, (120, 255, 120), 1)
        # cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,0,255));
    cv2.imshow('frame', img);
    # cv2.imshow('gray',gray);

    if time.time() > start + period:
        break;
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break;

cap.release();
cv2.destroyAllWindows();

if (conf > 50):
    Sender_email = str("pythondammy123@gmail.com")
    Password = str("python_dammy@1")
    #input(str("Please enter your password : "))
    message = str("Student you were present for the class today ")

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(Sender_email,Password)
    print("Login Successful")
    server.sendmail(Sender_email,Rec_email, message)
    print("Email regarding your presence has been sent to", Rec_email)
    server.quit()

else:
    print("Cannot send mail because you were absent for the class today")
