import cv2
from django.db.models.fields import EmailField 
def get_filtered_image(img, action):

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if action == "NO_FILTER":
        filtered = img
    elif action == "COLORIZED":
        filtered = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    elif action =="INVERT":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, img = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        filtered = cv2.bitwise_not(img)
        


    return filtered