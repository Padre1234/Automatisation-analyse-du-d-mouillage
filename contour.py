import numpy as np
import argparse
import cv2

ref_point = []
cropping = False
def shape_selection(event, x, y, flags, param):
  # grab references to the global variables
  global ref_point, cropping

  # if the left mouse button was clicked, record the starting
  # (x, y) coordinates and indicate that cropping is being
  # performed
  if event == cv2.EVENT_LBUTTONDOWN:
    ref_point = [(x, y)]
    cropping = True

  # check to see if the left mouse button was released
  elif event == cv2.EVENT_LBUTTONUP:
    # record the ending (x, y) coordinates and indicate that
    # the cropping operation is finished
    ref_point.append((x, y))
    cropping = False
     # draw a rectangle around the region of interest
    cv2.rectangle(resized, ref_point[0], ref_point[1], (0, 255, 0), 2)
    

def auto_canny(image, sigma=0.33):
  # compute the median of the single channel pixel intensities
  v = np.median(crop_img)
  # apply automatic Canny edge detection using the computed median
  lower = int(max(0, (1.0 - sigma) * v))
  upper = int(min(255, (1.0 + sigma) * v))
  edged = cv2.Canny(image, lower, upper)
  # return the edged image
  return edged


# load the image, clone it, and setup the mouse callback function
image = cv2.imread('0191.bmp',0)
print('Original Dimensions : ',image.shape)
scale_percent = 50 # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)

clone = resized.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", shape_selection)

# keep looping until the 'q' key is pressed
while True:
  # display the image and wait for a keypress
  cv2.imshow("image", resized)

  key = cv2.waitKey(1) & 0xFF

  # if the 'r' key is pressed, reset the cropping region
  if key == ord("r"):
    image = clone.copy()

  # if the 'c' key is pressed, break from the loop
  elif key == ord("c"):
    break

# if there are two reference points, then crop the region of interest
# from teh image and display it
if len(ref_point) == 2:
  crop_img = clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]
  cv2.imshow("crop_img", crop_img)
  cv2.waitKey(0)
  # Find Canny edges 
edge = auto_canny(crop_img) 
cv2.waitKey(0) 
  
# Finding Contours 
# Use a copy of the image e.g. edged.copy() 
# since findContours alters the image 
contours, hierarchy = cv2.findContours(edge,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
  
cv2.imshow('Canny Edges After Contouring', edge) 
cv2.waitKey(0) 
  
print("Number of Contours found = " + str(len(contours))) 
  
# Draw all contours 
# -1 signifies drawing all contours 
#cv2.drawContours(crop_img, contours, -1, (0, 255, 0), 3) 
area = cv2.countNonZero(edge)
perimetre = area/1.6


print ("perimetre=",perimetre)

# close all open windows
cv2.destroyAllWindows()