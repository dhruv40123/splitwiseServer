  # Import the db object
from splitserver.settings import db  # Import the db object

# databse 
# import ssl
from pymongo import MongoClient


# DB_URL = config('DB_URL')

DB_URL = "mongodb+srv://dhruv4023:Azbxcz123@cluster0.imexjta.mongodb.net"
# # DB_URL="mongodb://127.0.0.1:27017"
# client = MongoClient(DB_URL, ssl_cert_reqs=ssl.CERT_NONE)
client = MongoClient(DB_URL)
db = client["SplitWise"]

print("database connected successfully")

# all collections
users = db["users"]
groups = db["groups"]
groupData = db["gropuData"]
