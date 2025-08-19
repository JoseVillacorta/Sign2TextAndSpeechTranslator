import cv2
from config.settings import *

# Settings
SEQUENCE_LENGTH = 5 # Numero de frames
NUM_FEATURES = 1662 # MediaPipe pose Landmarks
NUM_CLASSES = 15 # numero de senias a reconocer

# Training Parameters
BATCH_SIZE = 8
EPOCHS = 500
TARGET_FPS = 12

# UI Parameters
FONT = cv2.FONT_HERSHEY_PLAIN
FONT_SIZE = 1.5
FONT_POS = (5,30)

# Vocabulary mappinig
words_text = {
    "hola": "HOLA",
    "adios": "ADIÓS",
    "buenos_dias": "BUENOS DÍAS",
    "buenas_tardes": "BUENAS TARDES",
    "buenas_noches": "BUENAS NOCHES",
    "como_estas": "COMO ESTÁS",
    "bien": "BIEN",
    "mal": "MAL",
    "mas_o_menos": "MAS O MENOS",
    "gracias": "GRACIAS",
    "disculpa": "DISCULPA",
    "me_ayudas": "ME AYUDAS",
    "por_favor": "POR FAVOR"
}