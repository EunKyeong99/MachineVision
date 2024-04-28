import numpy as np, cv2

def add_sepia(image):
    sepia_matrix = np.array([[0.272, 0.534, 0.131],
                             [0.349, 0.686, 0.168],
                             [0.393, 0.769, 0.189]]).astype(np.float32)
    sepia_image = cv2.transform(image, sepia_matrix)
    sepia_image = np.clip(sepia_image, 0, 255).astype(np.uint8)

    return sepia_image

def add_noise(image, mean=0, var=300):
    row, col, ch = image.shape
    sigma = var**0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch)).astype(np.float32)
    noisy = cv2.add(image.astype(np.float32), gauss)
    noisy = np.clip(noisy, 0, 255)
    return noisy.astype(np.uint8)

image = cv2.imread('./image/Lenna.png')
if image is None: raise Exception("영상 파일 읽기 오류")

sepia_image = add_sepia(image)
noisy_image = add_noise(sepia_image)

cv2.imshow('Original', image)
cv2.imshow('vintage_filter', noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
