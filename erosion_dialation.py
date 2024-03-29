import numpy as np
import cv2
from copy import deepcopy


#input the image
img = cv2.imread("erosion_dialation.png")

cv2.imshow("input", img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#convert to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(thresh,binary) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
#cv2.imshow("binary", binary)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#filter size 5x5
filterK = np.ones((5,5))
#print(filterK)


#shape of image and kernel
S = binary.shape
F = filterK.shape

#convert into 0 and 1
binary = binary/255
#copy for dialation
binary2 = deepcopy(binary)




#for padding get row and column
R = S[0]+F[0]-1
C = S[1]+F[1]-1

#get the new padding image in only zeros
N = np.zeros((R,C))


#insert the image with padding
for i in range(S[0]):
    for j in range(S[1]):
        N[i+np.int((F[0]-1)/2),j+np.int((F[1]-1)/2)] = binary[i,j]
        

#use the filter for erosion
for i in range(S[0]):
    for j in range(S[1]):
        k = N[i:i+F[0],j:j+F[1]]
        result = (k == filterK)
        final = np.all(result == True)
        if final:
            binary[i,j] = 1
        else:
            binary[i,j] = 0
#output image of erosion
cv2.imshow("erosion", binary)
#cv2.imwrite("erosion_output.png", binary)
#cv2.imwrite("erosion", binary)

#use filter for dialation
for i in range(S[0]):
    for j in range(S[1]):
        k = N[i:i+F[0],j:j+F[1]]
        result = (k == filterK)
        final = np.any(result == True)
        if final:
            binary2[i,j] = 1
        else:
            binary2[i,j] = 0
            
#output image of dialation
cv2.imshow("dialation", binary2)
#cv2.imwrite("dialation_output.png", binary)
#cv2.imwrite("dialation", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()