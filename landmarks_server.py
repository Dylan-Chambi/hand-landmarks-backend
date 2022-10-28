import tinydb as db
import uvicorn
from fastapi import FastAPI, File, UploadFile

from predictor import LandmarksSaver

class ServerAPI:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.app = FastAPI(title="Landmarks Server")
        self.app.add_api_route("/upload_photo", self.landmarks, methods=["POST"])
        self.app.add_api_route("/get_landmarks", self.get_landmarks, methods=["GET"])
        self.db = db.TinyDB("./database/db_landmarks.json")

    def landmarks(self, image_file: UploadFile = File(...)):
        try:
            predictor = LandmarksSaver()
            landmarks_dict = predictor.predict_file(image_file.file)
            self.save_landmarks(image_file.filename, landmarks_dict)
            return dict(code=200, status="OK")
        except Exception as e:
            return dict(code=500, status="Internal Server Error", error=str(e))

    def get_landmarks(self):
        return self.db.all()

    def save_landmarks(self, name, landmarks_dict):
        self.db.insert(dict(name=name, landmarks=landmarks_dict))
    

    def run(self):
        uvicorn.run(self.app, host=self.host, port=self.port)