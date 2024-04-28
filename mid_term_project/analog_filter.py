import numpy as np,

def adjust_temperature(image, adjustment):
    b, g, r = cv2.split(image)
    if adjustment > 0:
        r = cv2.add(r, adjustment)
        b = cv2.subtract(b, adjustment)
    else:
        r = cv2.subtract(r, -adjustment)
        b = cv2.add(b, -adjustment)
    return cv2.merge([b, g, r])

def decrease_saturation(image, amount):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    s = cv2.subtract(s, amount)
    return cv2.cvtColor(cv2.merge([h, s, v]), cv2.COLOR_HSV2BGR)

def add_noise(image, mean=0, var=300):
    row, col, ch = image.shape
    sigma = var ** 0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch)).astype(np.float32)
    noisy = cv2.add(image.astype(np.float32), gauss)1
    noisy = np.clip(noisy, 0, 255)
    return noisy.astype(np.uint8)

image = cv2.imread('./image/Lenna.png', cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 오류")

toned_image = adjust_temperature(image, adjustment=10)
less_saturated_image = decrease_saturation(toned_image, amount=50)
final_image = add_noise(less_saturated_image)

cv2.imshow('Original Image', image)
cv2.imshow('analog_filter', final_image)
cv2.waitKey(0)
