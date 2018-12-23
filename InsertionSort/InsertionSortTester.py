import InsertionSort as InsertionSort
import numpy as np
import cv2

# Intro ---------------------------------------------------------------------------------------------------------------
img = np.zeros((1000, 1000, 3), np.uint8)

font = cv2.FONT_HERSHEY_PLAIN
white = (255, 255, 255)

cv2.putText(img, 'Insertion Sort', (10, 40), font, 2, white, 2)
cv2.putText(img, 'By: Mason J. Hawver (@ https://github.com/MasonOfTheHawverFamily/SortingAlgorithms)', (10, 60), font, 1, white, 1)
cv2.putText(img, 'Press Q to continue', (10, 80), font, 1, white, 1)


cv2.imshow("Insertion Sort", img)
cv2.waitKey(0)

#  Insertion sort 80 --------------------------------------------------------------------------------------------------

IS = InsertionSort.InsertionSort

test_arr = np.arange(400)
np.random.shuffle(test_arr)

test = IS(test_arr)
test.insertionSort(3, True)
