import cv2
import scipy as sp


img = cv2.imread('images/01.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detector = cv2.FeatureDetector_create("SIFT")
#descriptor = cv2.DescriptorExtractor_create("SIFT")

#kp = detector.detect(img)
#kp, d = descriptor.compute(img, kp)

sift = cv2.xfeatures2d.SIFT_create()
kp, d = sift.detectAndCompute(img, None)

d_list = []
d_list.append(d)

#print ('Keypoints: %d',len(kp))

img = cv2.drawKeypoints(img, kp, img)

cv2.imshow("image", img)

cv2.waitKey(0)
