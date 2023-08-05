from pathlib import Path
import numpy as np
import cv2
from image_montage.settings import SHEET_SIZES_IN_PIXELS


class Image:

    def __init__(self, image):
        nparr = np.fromstring(image.read(), np.uint8)
        self.array = cv2.imdecode(nparr, cv2.IMREAD_COLOR)


class Sheet:

    def __init__(self, size='A4'):
        self._size = str(size).upper()
        self.width = SHEET_SIZES_IN_PIXELS[self._size]['width']
        self.height = SHEET_SIZES_IN_PIXELS[self._size]['height']
        self.array = np.full((self.height, self.width, 3), 255)
