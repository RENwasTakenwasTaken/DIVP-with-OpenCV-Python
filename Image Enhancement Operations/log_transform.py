import cv2
import numpy as np
import requests

choice = int(input("Read input from web or local (0 / 1): "))
url = "https://contrastly.com/wp-content/uploads/shadows-photography.jpg"

if choice == 0:
    response = requests.get(url)
    raw_image = response.content

    np_img = np.frombuffer(raw_image, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_GRAYSCALE)
else:
    img = cv2.imread("images/nature.jpg", cv2.IMREAD_GRAYSCALE)

print(img)

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

while True:
    cv2.imshow("Image", img)

    transformed_image = img.copy()

    for i, row in enumerate(transformed_image):
        for j, r in enumerate(row):
            s = T(r)
            transformed_image[i][j] = s

    cv2.imshow("Log Transformed Image", transformed_image)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break
