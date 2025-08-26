import cv2
import os
import sys

# Add the project's root directory to sys.path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.utils.constants import *
from src.utils.helpers import create_directory_if_not_exists

def capture_video_samples():
    """
    Captures samples videos of sign language
    """

    # Create a directory for frames if it doesn't exist
    create_directory_if_not_exists(FRAME_ACTIONS_DIR)

    # Initialize camera
    cap = cv2.VideoCapture(CAMERA_INDEX)

    print("Presiona 'q' para salir")
    print("Presiona 'c' para capturar una muestra")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error al leer la camara")
            break

        # Show frame
        cv2.imshow('Captura de Muestras', frame)

        # Wait for key press
        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break
        elif key == ord('c'):
            # Capture logic will be added here
            print("Función de captura - proximamente")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_video_samples()
