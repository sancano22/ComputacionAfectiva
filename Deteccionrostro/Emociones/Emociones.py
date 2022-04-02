#https://pypi.org/project/fer/
# 
from fer import FER
import json
import cv2

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

img = cv2.imread("img.png")
detector = FER(mtcnn=True)

variable=detector.detect_emotions(img)
print(variable)


#JSON
id=1
data={'userID':id,'emotions':variable[0]["emotions"]}
print(data)