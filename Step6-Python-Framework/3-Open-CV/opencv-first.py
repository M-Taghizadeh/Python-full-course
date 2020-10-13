import cv2

img = cv2.imread("C:/Users/Zanis/Desktop/test.jpg", 0)
cv2.imshow("First Image Reading with cv2", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
