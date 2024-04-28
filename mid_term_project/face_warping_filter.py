import cv2
import dlib
import numpy as np

def highlight_features(image, landmarks):
    output = image.copy()
    # 각 랜드마크에 대해 원을 그려 강조
    for (x, y) in landmarks:
        cv2.circle(output, (x, y), 2, (0, 255, 0), -1)  # 녹색 원으로 표시
    return output

def load_landmarks(image, predictor, detector):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    if len(faces) > 0:
        landmarks = predictor(gray, faces[0])
        return np.array([[p.x, p.y] for p in landmarks.parts()], dtype=np.int32)
    return None

# 이미지 및 모델 로드
image_path = './image/Lenna.png'
model_path = './model/shape_predictor_68_face_landmarks.dat'
image = cv2.imread(image_path)
if image is None:
    raise Exception("영상 파일 읽기 오류")

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(model_path)

# 랜드마크 탐지
landmarks = load_landmarks(image, predictor, detector)

if landmarks is not None:
    # 특징점 강조
    highlighted_image = highlight_features(image, landmarks)

    # 결과 표시
    cv2.imshow('Original Image', image)
    cv2.imshow('Highlighted Features', highlighted_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No faces detected.")


