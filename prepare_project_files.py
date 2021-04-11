import os
import requests
from decouple import config

os.mkdir(os.path.join(os.getcwd(), config('IMG_DIR')))
os.mkdir(os.path.join(os.getcwd(), config('MODEL_DIR')))

r = requests.get(config('MODEL_LINK'), allow_redirects=True)

open(f"{config('MODEL_DIR')}/data_model.h5",
     'wb').write(r.content)
