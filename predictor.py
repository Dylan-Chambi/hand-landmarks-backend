import cv2
import mediapipe as mp
import numpy as np
from PIL import Image

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

class LandmarksSaver:
    def __init__(self):
        self.mp_draw = mp.solutions.drawing_utils
        self.holistic = mp.solutions.holistic.Holistic(
            static_image_mode=True,
            model_complexity=2,
            enable_segmentation=True,
            refine_face_landmarks=True)
    
    def predict_file(self, file):
        img = np.array(Image.open(file))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = self.holistic.process(img)

        landmarks_dict = {}

        if results.face_landmarks:
            face_landmarks = results.face_landmarks.landmark
            face_landmarks_dict = {}
            for idx, landmark in enumerate(face_landmarks):
                face_landmarks_dict[idx+1] = dict(x=landmark.x, y=landmark.y, z=landmark.z, visibility=landmark.visibility)
            landmarks_dict["face_landmarks"] = face_landmarks_dict

        if results.pose_landmarks:
            pose_landmarks = results.pose_landmarks.landmark
            pose_landmarks_dict = {}
            for idx, landmark in enumerate(pose_landmarks):
                pose_landmarks_dict[idx+1] = dict(x=landmark.x, y=landmark.y, z=landmark.z, visibility=landmark.visibility)
            landmarks_dict["pose_landmarks"] = pose_landmarks_dict


        if results.left_hand_landmarks:
            left_hand_landmarks = results.left_hand_landmarks.landmark
            left_hand_landmarks_dict = {}
            for idx, landmark in enumerate(left_hand_landmarks):
                left_hand_landmarks_dict[idx+1] = dict(x=landmark.x, y=landmark.y, z=landmark.z, visibility=landmark.visibility)
            landmarks_dict["left_hand_landmarks"] = left_hand_landmarks_dict


        if results.right_hand_landmarks:
            right_hand_landmarks = results.right_hand_landmarks.landmark
            right_hand_landmarks_dict = {}
            for idx, landmark in enumerate(right_hand_landmarks):
                right_hand_landmarks_dict[idx+1] = dict(x=landmark.x, y=landmark.y, z=landmark.z, visibility=landmark.visibility)
            landmarks_dict["right_hand_landmarks"] = right_hand_landmarks_dict

        return landmarks_dict