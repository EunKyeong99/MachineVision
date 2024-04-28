import numpy as np, cv2

def filter(image, mask):
    rows, cols, channels = image.shape
    dst = np.zeros_like(image, dtype=np.float32)
    xcenter, ycenter = mask.shape[1]//2, mask.shape[0]//2

    for c in range(channels):
        for i in range(ycenter, rows - ycenter):
            for j in range(xcenter, cols - xcenter):
                y1, y2 = i - ycenter, i + ycenter + 1
                x1, x2 = j - xcenter, j + xcenter + 1
                roi = image[y1:y2, x1:x2, c].astype("float32")
                tmp = cv2.multiply(roi, mask)
                dst[i, j, c] = cv2.sumElems(tmp)[0]
    return dst.astype(np.uint8)

def brightness_image(image, brightness=30, saturation=30):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv_image)

    lim = 255 - brightness
    v[v > lim] = 255
    v[v <= lim] += brightness

    lim = 255 - saturation
    s[s > lim] = 255
    s[s <= lim] += saturation

    final_hsv = cv2.merge((h, s, v))
    image_result = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return image_result

image = cv2.imread("./image/Lenna.png", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 오류")

data = [1/25, 1/25, 1/25, 1/25, 1/25,
        1/25, 1/25, 1/25, 1/25, 1/25,
        1/25, 1/25, 1/25, 1/25, 1/25,
        1/25, 1/25, 1/25, 1/25, 1/25,
        1/25, 1/25, 1/25, 1/25, 1/25]
mask = np.array(data, np.float32).reshape(5, 5)

blurred_image = filter(image, mask)
enhanced_image = brightness_image(blurred_image)

cv2.imshow("Original", image)
cv2.imshow("dreamy_filter", enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
