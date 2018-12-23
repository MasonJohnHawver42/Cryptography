import numpy as np
import cv2

class InsertionSort:
    def __init__(self, arr=np.array([])):
        self.unsortedArr = arr
        self.MAX = np.amax(self.unsortedArr)
        self.done = False

    def insertionSortOnce(self, index, scale, visualize):
        val = self.unsortedArr[index]
        i = index
        while i > 0:
            i -= 1
            comparing_val = self.unsortedArr[i]
            if comparing_val < val:
                i += 1
                break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.done = True

        self.unsortedArr[i + 1: index + 1] = self.unsortedArr[i: index]
        self.unsortedArr[i] = val

        if visualize:
            arr = self.toImg(scale)
            cv2.imshow("Insertion Sort", arr)
            cv2.waitKey(1)

    def insertionSort(self, scale, visualize):
        for i in range(self.unsortedArr.shape[0]):
            self.insertionSortOnce(i, scale, visualize)
            if self.done:
                break

    def toImg(self, scale=10):
        arr = np.zeros((self.unsortedArr.shape[0], self.MAX))
        for i in range(self.unsortedArr.shape[0]):
            val = self.unsortedArr[i]
            arr[i] = ((np.arange(self.MAX) < val) * 140) + ((np.arange(self.MAX) == val) * 0) + ((np.arange(self.MAX) > val) * 240)


        arr = arr.repeat(3).reshape((self.unsortedArr.shape[0], self.MAX, 3))
        arr = cv2.resize(arr, dsize=(int(arr.shape[1] * scale), int(arr.shape[0] * scale)), interpolation=0)
        arr = np.rot90(arr)

        return arr.astype(np.uint8)

