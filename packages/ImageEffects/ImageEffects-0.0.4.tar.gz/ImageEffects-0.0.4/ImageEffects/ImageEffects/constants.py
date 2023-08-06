import os

# paths
CONST_FILE_DIR = os.path.abspath(__file__)
IMAGE_EFFECTS_DIR = os.path.split(CONST_FILE_DIR)[0]
SRC_DIR = os.path.split(IMAGE_EFFECTS_DIR)[0]
ROOT_DIR = os.path.split(SRC_DIR)[0]
RESOURCES_DIR = os.path.join(ROOT_DIR, "resources")
FONTS_DIR = os.path.join(RESOURCES_DIR, 'fonts')
EMOJIS_DIR = os.path.join(RESOURCES_DIR, 'emojis')
