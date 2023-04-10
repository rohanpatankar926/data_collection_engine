import os
import base64
from tqdm import tqdm

def upload_bulk_data(root="caltech-101"):
    labels = os.listdir(root)
    for label in tqdm(labels):
        data = []
        images = os.listdir(root + "/" + label)
        for img in tqdm(images):
            path = os.path.join(os.getcwd(), root, label, img)
            with open(rf'{path}', "rb") as img:
                data.append(base64.b64encode(img.read()).decode())

    print("/nCompleted")


upload_bulk_data(root="caltech-101")
