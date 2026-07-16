import cv2
import numpy as np

N = 256
img = cv2.imread("images/nature.jpg", cv2.IMREAD_GRAYSCALE)

print(img)

def T(r):
    return N - 1 - r

while True:
    cv2.imshow("Image", img)

    transformed_image = img.copy()

    for i, row in enumerate(transformed_image):
        for j, r in enumerate(row):
            s = T(r)
            transformed_image[i][j] = s

    cv2.imshow("Negated Image", transformed_image)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break
