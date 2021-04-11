import os
import requests
from decouple import config

r = requests.get(config('MODEL_LINK'), allow_redirects=True)

os.mkdir(os.path.join(os.getcwd(), config('MODEL_DIR')))

open(f"{config('MODEL_DIR')}/resnet50_coco_best_v2.1.0.h5",
     'wb').write(r.content)
