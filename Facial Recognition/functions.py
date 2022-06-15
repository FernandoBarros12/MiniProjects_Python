import os
from cv2 import cv2 
from datetime import datetime
import face_recognition as fr
import numpy
import ctypes

# Create Database
def create_database():
    route='./Resources/Employees'
    l_images = []
    l_employees_names=[]
    l_employees= os.listdir(route)

    for name in l_employees:
        current_pic=cv2.imread(f'{route}\{name}')
        l_images.append(current_pic)
        l_employees_names.append(os.path.splitext(name)[0])
    
    return l_images, l_employees_names, l_employees


# Encode faces
def encode(images):
    l_encoded=[]

    # to RGB
    for image in images:

        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encoded=fr.face_encodings(image)[0]
        l_encoded.append(encoded)
        
    return l_encoded


# Register entries
def register_employees(employee):

    with open('registration_form.csv', 'r+') as file:
        l_data= file.readlines()
        registration_names=[]

        for line in l_data:
            entry= line.split(',')
            registration_names.append(entry[0])
        
        if employee not in registration_names:
            date_info = datetime.now()
            str_now = date_info.strftime('%H:%M:%S')
            file.writelines(f'\n{employee}, {str_now}')



# Take a picture with a webcam and validate it
def validation(l_encoded_employees, l_employees_names):
    screenshot=cv2.VideoCapture(0, cv2.CAP_DSHOW)
    flag, picture = screenshot.read()

    if not flag:

        print('Picture not taken')

    else:

        face_screenshot=fr.face_locations(picture)
        coded_face_screenshot=fr.face_encodings(picture, face_screenshot)

        # Search coincidences
        for coded_face, base_face in zip(coded_face_screenshot, face_screenshot):

            coincidences = fr.compare_faces(l_encoded_employees, coded_face)
            distances = fr.face_distance(l_encoded_employees, coded_face)
            match_rate= numpy.argmin(distances)

            if distances[match_rate] > 0.6:

                ctypes.windll.user32.MessageBoxW(0, "No match Found", "Error", 1)

            else:

                name= l_employees_names[match_rate]

                # Rectangle formatting
                y1, x2, y2, x1 = base_face
                cv2.rectangle(picture, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(picture, (x1, y2 - 28), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(picture, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2)
                
                register_employees(name)
                # Show image
                cv2.imshow('Webcam Image', picture)
                cv2.waitKey(0)