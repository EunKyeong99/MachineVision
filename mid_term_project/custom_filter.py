import numpy as np, cv2

def LensDistortionImage(img, exp=2, scale=1):
    rows, cols = img.shape[:2]

    mapy, mapx =np.indices((rows, cols), dtype=np.float32)

    mapx = 2 * mapx / (cols - 1) - 1
    mapy = 2 * mapy / (rows - 1) - 1

    r, theta = cv2.cartToPolar(mapx, mapy)

    r[r < scale] = r[r < scale] ** exp

    mapx, mapy = cv2.polarToCart(r, theta)

    mapx = ((mapx + 1) * cols - 1) / 2
    mapy = ((mapy + 1) * rows - 1) / 2

    result = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
    return result


image = cv2.imread('Lenna.png')
if image is None: raise Exception("영상 파일 읽기 오류")

convex = LensDistortionImage(image, exp=2)

cv2.imshow('original', image)
cv2.imshow('convex_filter', convex)
cv2.waitKey()