import numpy as np, cv2
import dlib

def load_landmarks(image, predictor, detector):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    if len(faces) > 0:
        landmarks = predictor(gray, faces[0])
        return np.array([[p.x, p.y] for p in landmarks.parts()], dtype=np.int32)
    return None


def emphasize_eyes(image, landmarks, scale=2):
    if landmarks is None:
        return image

    output_image = image.copy()
    for i in range(36, 48):
        if i == 42:
            x, y, w, h = cv2.boundingRect(landmarks[36:42])
        else:
            x, y, w, h = cv2.boundingRect(landmarks[42:48])

        roi = image[y:y + h, x:x + w]
        roi = cv2.resize(roi, (w * scale, h * scale), interpolation=cv2.INTER_CUBIC)

        center_x, center_y = x + w // 2, y + h // 2
        new_x = max(0, center_x - w * scale // 2)
        new_y = max(0, center_y - h * scale // 2)

        output_image[new_y:new_y + h * scale, new_x:new_x + w * scale] = roi

    return output_image

image = cv2.imread('Lenna.png')
if image is None: raise Exception("영상 파일 읽기 오류")

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
landmarks = load_landmarks(image, predictor, detector)

emphasized_image = emphasize_eyes(image, landmarks)

cv2.imshow('original', image)
cv2.imshow('Emphasized Eyes', emphasized_image)
cv2.waitKey(0)
