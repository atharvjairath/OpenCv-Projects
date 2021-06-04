import cv2
import numpy as np


# Load the image where we need to look waldo for
image = cv2.imread('./Images/WaldoBeach.jpg')
cv2.imshow('Where is Waldo?', image)
cv2.waitKey(0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Load the template of waldo to find
template = cv2.imread('./Images/waldo.jpg',0)

#using matchTemplate

result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
# cords of the result to create a box 
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

#Create Bounding Box
top_left = max_loc
bottom_right = (top_left[0] + 50, top_left[1] + 50)
cv2.rectangle(image, top_left, bottom_right, (0,0,255), 5)

cv2.imshow('Where is Waldo?', image)
cv2.waitKey(0)
cv2.destroyAllWindows()