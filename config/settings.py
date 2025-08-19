import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Rutas de datos
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_VIDEO_DIR = os.path.join(DATA_DIR, 'raw_videos')
FRAME_ACTIONS_DIR = os.path.join(DATA_DIR, 'frame_actions')
KEYPOINTS_DIR = os.path.join(DATA_DIR, 'keypoints')
NORMALIZED_SAMPLES_DIR = os.path.join(DATA_DIR, 'normalized_samples')

# Rutas de modelos
MODELS_DIR = os.path.join(BASE_DIR, 'models')
TRAINED_MODELS_DIR = os.path.join(MODELS_DIR, 'trained_models')
CHECKPOINTS_DIR = os.path.join(MODELS_DIR, 'trained_models')
VOCABULARY_DIR = os.path.join(MODELS_DIR, 'vocabulary')

# Configuraciones del modelo
SEQUENCE_LENGTH = 30
NUM_FEATURES = 1662 # MediaPipe pose Landmarkss
NUM_CLASSES = 15 # Numero de señass a reconocer

# Configuraciones de entrenamiento
BATCH_SIZE = 32
EPOCHS = 100
LEARNING_RATE = 0.001