import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Data paths
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_VIDEO_DIR = os.path.join(DATA_DIR, 'raw_videos')
FRAME_ACTIONS_DIR = os.path.join(DATA_DIR, 'frame_actions')
KEYPOINTS_DIR = os.path.join(DATA_DIR, 'keypoints')
NORMALIZED_SAMPLES_DIR = os.path.join(DATA_DIR, 'normalized_samples')

# Model paths
MODELS_DIR = os.path.join(BASE_DIR, 'models')
TRAINED_MODELS_DIR = os.path.join(MODELS_DIR, 'trained_models')
CHECKPOINTS_DIR = os.path.join(MODELS_DIR, 'trained_models')
VOCABULARY_DIR = os.path.join(MODELS_DIR, 'vocabulary')

# Project-specific paths
DATA_JSON_PATH = os.path.join(DATA_DIR, "data.json")
MODEL_PATH = os.path.join(TRAINED_MODELS_DIR, f"actions_15.keras")
WORDS_JSON_PATH = os.path.join(VOCABULARY_DIR, "words.json")