# Rutas de archivos
import os
from .settings import *

def create_directories():
    directories = [
        RAW_VIDEO_DIR,
        FRAME_ACTIONS_DIR,
        KEYPOINTS_DIR,
        NORMALIZED_SAMPLES_DIR,
        TRAINED_MODELS_DIR,
        CHECKPOINTS_DIR,
        VOCABULARY_DIR
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Directorio creado: {directory}")

if __name__ == "__main__":
    create_directories()