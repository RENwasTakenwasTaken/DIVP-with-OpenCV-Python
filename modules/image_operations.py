import cv2
import numpy as np

class ImageOperations:    
    @staticmethod
    def read_image(filepath, color=0):
        '''
        Args:
            color: 0 -> Gray, 1 -> Colored
        '''
        return cv2.imread(filepath, color)

    @staticmethod
    def image_negative(image):
        N = 256

        def T(r):
            return N - 1 - r
        
        for i, row in enumerate(image):
            for j, r in enumerate(row):
                s = T(r)
                image[i][j] = s

        return image

    @staticmethod
    def log_transform(image):
        def T(r):
            '''
            Textbook formula:

            result = c * log(1 + r)

            sometimes, r may be 0. To ensure that log(0) = Inf. does not happen, 1 + r is done.

            Next, c is simply scales the result to some readable value. Otherwise, all would become dark (since the image itself is darks)
            '''
            c = 255 / np.log(256)
            # c = 10 # Middle value of range.
            result = c * np.log(1 + r)

            if result >= 255:
                result = 255

            if result <= 0:
                result = 0

            return result

        for i, row in enumerate(image):
            for j, r in enumerate(row):
                s = T(r)
                image[i][j] = s

        return image
