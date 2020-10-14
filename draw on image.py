import numpy as np
import cv2

#img = cv2.imread("lena.jpg",1)
img = np.zeros([500,500,3], np.uint8)

img = cv2.line(img, (0,0),(300,300),(0,0,225), 5) #177,250,29 from google"rgb colour code and reverse
img = cv2.arrowedLine(img, (0,300),(300,300),(0,225,0), 5)
img = cv2.rectangle(img, (360,0),(200,200),(0,0,220), 5)
img = cv2.circle(img, (300,300),50,(225,0,0), 5)
font = cv2.FONT_ITALIC
img = cv2.putText(img, "OpenCV", (0,450), font,3, (177,250,29), cv2.LINE_AA)

cv2.imshow("image",img)

cv2.waitKey(0)
cv2.destroyAllWindows()