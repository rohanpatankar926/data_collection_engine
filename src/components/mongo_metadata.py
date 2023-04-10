import os
import sys
sys.path.append(os.getcwd())
from src.utils.database_handler import MongodbClient


class MetaDataStore:
    def __init__(self):
        self.root = os.path.join(os.getcwd(), "data")
        self.images = os.path.join(self.root, "caltech-101")
        self.labels = os.listdir(self.images)
        self.mongo = MongodbClient()

    def register_labels(self):
        try:
            records = {}
            for idx, label in enumerate(self.labels):
                records[f"{idx}"] = label
            self.mongo.database['labels'].insert_one(records)

        except Exception as e:
            return {"Created": False, "Reason": e}
    
    def run_step(self):
        try:
            self.register_labels()
        except Exception as e:
            return {"Created": False, "Reason": e}


if __name__ == "__main__":
    meta = MetaDataStore()
    meta.run_step()
