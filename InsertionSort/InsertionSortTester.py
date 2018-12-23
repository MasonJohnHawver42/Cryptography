import InsertionSort as InsertionSort
import numpy as np
import cv2

# Intro ---------------------------------------------------------------------------------------------------------------
img = np.zeros((1000, 1000, 3), np.uint8)

font = cv2.FONT_HERSHEY_PLAIN
white = (255, 255, 255)

cv2.putText(img, 'Insertion Sort', (10, 40), font, 2, white, 2)
cv2.putText(img, 'By: Mason J. Hawver (@ https://github.com/MasonOfTheHawverFamily/SortingAlgorithms)', (10, 60), font, 1, white, 1)


cv2.imshow("Insertion Sort", img)
cv2.waitKey(0)

#  Insertion sort 80 --------------------------------------------------------------------------------------------------

IS = InsertionSort.InsertionSort

test_arr = np.arange(80)
np.random.shuffle(test_arr)

test = IS(test_arr)
test.insertionSort(12.5, True)

# Transition (Is 1000?) -----------------------------------------------------------------------------------------------

img = np.zeros((1000, 1000, 3), np.uint8)

font = cv2.FONT_HERSHEY_PLAIN
white = (255, 255, 255)

cv2.putText(img, 'Wow that was fast, but can Insertion sort handle', (10, 40), font, 2, white, 2)
cv2.putText(img, '1000 items?', (10, 80), font, 3, white, 2)
cv2.putText(img, 'PS: The first time I did this I was sure my computer would crash', (10, 110), font, 1, white, 1)


cv2.imshow("Insertion Sort", img)
cv2.waitKey(0)

# Insertion Sort 1000--------------------------------------------------------------------------------------------------

test_arr = np.arange(1000)
np.random.shuffle(test_arr)

test = IS(test_arr)
test.insertionSort(1, True)

# Transition (Is 10000?) ----------------------------------------------------------------------------------------------
img = np.zeros((1000, 1000, 3), np.uint8)

font = cv2.FONT_HERSHEY_PLAIN
white = (255, 255, 255)

cv2.putText(img, 'But how about', (10, 40), font, 2, white, 2)
cv2.putText(img, 'Ten Thousand Items', (10, 80), font, 3, white, 2)

cv2.imshow("Insertion Sort", img)
cv2.waitKey(0)

# Next ----------------------------------------------------------------------------------------------------------------

img = np.zeros((1000, 1000, 3), np.uint8)

font = cv2.FONT_HERSHEY_PLAIN
white = (255, 255, 255)

cv2.putText(img, 'Yeah Nope', (10, 40), font, 2, white, 2)
cv2.putText(img, 'Insertion sort can handle 10000 items, but visualizing that destroys my computer', (10, 60), font, 1, white, 1)
cv2.putText(img, 'So mabey in the future', (10, 80), font, 1, white, 1)

cv2.imshow("Insertion Sort", img)
cv2.waitKey(0)

# END -----------------------------------------------------------------------------------------------------------------

img = np.zeros((1000, 1000, 3), np.uint8)

font = cv2.FONT_HERSHEY_PLAIN
white = (255, 255, 255)

cv2.putText(img, 'Thanks for Watching Insertion Sort!!!', (10, 40), font, 2, white, 2)
cv2.putText(img, 'Make sure to go to my github page to understand how it all works', (10, 60), font, 1, white, 1)

cv2.imshow("Insertion Sort", img)
cv2.waitKey(0)
