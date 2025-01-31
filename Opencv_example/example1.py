import numpy as np
import cv2

image = np.zeros((200, 400), np.uint8) 
// uint8 = 배열의 데이터 타입을 8비트인 unsiguned integer로 설정하여 픽셀값이 0-255 값을 가지도록 함
image[:] = 200
// 이미지의 모든 픽셀값을 200인 회색으로 설정한다

title1, title2 = 'Position1', 'Position2'
// title1, title2를 각각 Positoin1, Position2로 설정
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)
// WINDOW_AUTOSIZE는 창의 사이즈를 자동으로 조정하도록 설정함
cv2.namedWindow(title2)
cv2.moveWindow(title1, 150, 150)
cv2.moveWindow(title2, 400, 50)

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.waitKey(0)
// 사용자가 키를 누르기 전까지 무한 대기, 0은 무한 대기라는 의
cv2.destroyWindow()
// destoryWindow는 창을 닫는 함수, 인자를 지정하지 않았기 때문에 아무 창도 닫지 않는다
