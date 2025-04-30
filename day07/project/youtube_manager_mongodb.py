from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://ytmanager:Saurabh@cluster0.c2wkoy2.mongodb.net/youtube_manager", tlsAllowInvalidCertificates=True)

db = client["youtube_manager"]
video_collection = db["videos"]

print(video_collection)

def add_videos(name, time):
    video_collection.insert_one({"name": name, "time": time})

def list_videos():
    for video in video_collection.find():
        print(f"ID: {video["_id"]}, Name: {video["name"]} and Time: {video["time"]}")

def update_videos(video_id, new_name, new_time):
    video_collection.update_one({"_id": ObjectId(video_id)},{"$set": {"name": new_name, "time": new_time}})

def delete_videos(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})

def main():
    while True:
        print("\n Youtube manager App with MongoDB")
        print("1. List all videos")
        print("2. Add a new videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exist the app")
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                list_videos()
            case "2":
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_videos(name, time)
            case "3":
                video_id = input("Enter the video id to update: ")
                new_name = input("Enter the updated video name: ")
                new_time = input("Enter the updated video time: ")
                update_videos(video_id, new_name, new_time)
            case "4":
                video_id = input("Enter the video id to delete: ")
                delete_videos(video_id)
            case "5": 
                break
            case _:
                print("Invalid choice")
            
if __name__ == "__main__":
    main()