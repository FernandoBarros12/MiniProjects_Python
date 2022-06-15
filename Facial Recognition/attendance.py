'''
An attendance system that uses the camera to take a picture and compare the person in the photo with a database of employees
'''
from cv2 import cv2
from functions import *

# Creating the data
l_images, l_employees_names, l_employees= create_database()
l_encoded_employees=encode(l_images)


# Take a picture with a webcam and validate it
validation(l_encoded_employees, l_employees_names)







