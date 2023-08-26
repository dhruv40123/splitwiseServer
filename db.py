from pymongo import MongoClient
import ssl


# DB_URL = "mongodb://127.0.0.1:27017"
DB_URL = "mongodb+srv://dhruv4023:Azbxcz123@cluster0.imexjta.mongodb.net/"
# DB_URL = settings.DB_URL
# adding not adding the security by Secure Socket Layer
client = MongoClient(DB_URL)

# DB_URL = "mongodb://localhost:27017"

print("database connected successfully")

db = client["SplitWise"]

# all collections
users = db["users"]
groups = db["groups"]
groupData = db["gropuData"]
