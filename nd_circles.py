# Import libraries
import cv2
import numpy as np


# Load the image, copy for output, and convert it to grayscale
image = cv2.imread('geom-figures.png')
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect circles in the image
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1.2, minDist=100)

# If the circles were found, let's show them!
if circles is not None:
    # turn the coordinates and radius of the circles into int
    circles = np.round(circles[0, :]).astype("int")
    # loop over each circle
    for (x, y, r) in circles:
        # draw a red circle in the output image
        cv2.circle(output, (x, y), r, (0, 0, 255), 4)
        # draw a blue rectangle corresponding to the center of the circle
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (255, 0, 0), -1)
    # show the output image
    cv2.imshow("output", output)
    # push any button on the keyboard to close the image and stop the program
    cv2.waitKey(0)
