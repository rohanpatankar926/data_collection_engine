import pymongo
import os
from dotenv import load_dotenv
load_dotenv()

class MongodbClient:
    client = None
    
    def __init__(self,database=os.getenv("MONGODB_URL"),database_name="cluster") -> None:
        if MongodbClient.client is None:
            MongodbClient.client = pymongo.MongoClient(database)
        self.client = MongodbClient.client
        self.database = self.client[database_name]
        self.database_name = database_name
