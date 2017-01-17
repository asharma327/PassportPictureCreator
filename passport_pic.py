import numpy as np
import cv2
import math

# Read Image
'''USER INPUT: Specify Image name in directory'''
img = cv2.imread('Mamma_PP.png')

# Resize Image to Smaller Acceptable size
'''USER INPUT: Depending on starting file size, fx & fy will have to be changed.
Both fx & fy correspond to ratio that picture will be resized'''
shrunk_image = cv2.resize(img, None, fx = 0.4, fy=0.4, interpolation=cv2.INTER_AREA)

# Crop image to a 600 by 600 pixel square
'''USER INPUT: Change the cropping square to pixels that fully capture the face.
shrunk_image[y1:y2, x1:x2] is the format where y1 & x1 are the starting and y2 & x2 are ending pixels'''
img_crop = shrunk_image[400:1000, 700:1300]
img_crop_2 = np.copy(img_crop)
img_crop_3 = np.copy(img_crop)

# Concatenate the cropped passport sized image into a 4 by 6 picture size
img_row = np.concatenate((img_crop, img_crop_2, img_crop_3), axis=1)
img_row_2 = np.copy(img_row)
img_total = np.concatenate((img_row, img_row_2), axis=0)

# Output and Write Passport Photo
'''USER INPUT: Change output file names. The files will be placed in the directory'''
cv2.imwrite('Mamma_PP_Photo.png', img_crop)
# Output and Write 4 by 6 photo containing 6 Passport Photos
cv2.imwrite('Full_photo_Mamma_PP.png', img_total)
