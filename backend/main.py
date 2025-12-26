# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from camera import capture_photos
# from collage import create_collage
from printer import print_image
#
# app = FastAPI()
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],   # kiosk/local use
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
# @app.post("/start")
# def start_photobooth():
#     capture_photos()
#     collage_path = create_collage()
#     print_image(collage_path)
#     return {"status": "printed"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from camera import capture_photos
from collage import create_collage

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/start")
def start_booth():
    capture_photos()          # camera opens ONLY here
    collage_path = create_collage()
    print_image(collage_path)
    return {"status": "ok", "collage": collage_path}
