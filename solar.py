import numpy
import cv2
img = cv2.imread("solar-system.jpg")
text="Sun"
text1 = "Mercury"
text2 = "Venus"
text3 = "Earth"
text4 = "Mars"
text5 = "Jupiter"
text6 = "Saturn"
text7 = "Uranus"
text8 = "Neptune"
cv2.putText(img,text,[50,10],fontFace=cv2.ACCESS_WRITE,fontScale=0.4,color=[255,0,255])
cv2.putText(img,text1,[130,180],fontFace=cv2.ACCESS_WRITE,fontScale=0.4,color=[0,0,255])
cv2.putText(img,text2,[220,180],fontFace=cv2.ACCESS_WRITE,fontScale=0.4,color=[0,0,255])
cv2.putText(img,text3,[300,160],fontFace=cv2.ACCESS_WRITE,fontScale=0.4,color=[0,0,255])
cv2.putText(img,text4,[380,180],fontFace=cv2.ACCESS_WRITE,fontScale=0.4,color=[0,0,255])
cv2.putText(img,text5,[490,100],fontFace=cv2.ACCESS_WRITE,fontScale=0.4,color=[0,0,255])
cv2.putText(img,text6,[720,140],fontFace=cv2.ACCESS_WRITE,fontScale=0.4,color=[0,0,255])
cv2.putText(img,text7,[940,140],fontFace=cv2.ACCESS_WRITE,fontScale=0.4,color=[0,0,255])
cv2.putText(img,text8,[1110,140],fontFace=cv2.ACCESS_WRITE,fontScale=0.4,color=[0,0,255])
cv2.imshow("Solar system",img)
cv2.waitKey(0000)