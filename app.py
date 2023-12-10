import os
import pymongo
import argparse
MONGO_URI= "mongodb://mongodb:27017"
client = pymongo.MongoClient(os.getenv("MONGODB_URI"))
task_database = client[os.getenv("MONGODB_DATABASE")]
tasks = task_database[os.getenv("MONGODB_TASKS_COLLECTION")]

# Currently not implementing a user collection. But can do this to make it more complex
# users = task_database[os.getenv("MONGODB_USERS_COLLECTION")]
# Create new user
# def insert_user(name):
#   users.insert_one({"name": name})

# tasks.drop() # Keep this line if you want to get rid of previous history

# Insert one task into the task database
def insert_task(title, description, priority, status, deadline, user):
  tasks.insert_one({"title": title, "description": description, "priority": priority, "status": status, "deadline": deadline, "user": user})

# Display tasks to the user. 
# Choose whether to sort by title, priority, status, or deadline.
# Choose whether to only display tasks for a specific user.
def display_tasks(sort=None, user=None):
    # Filter by user if specified
    query = {}
    if user:
        query["user"] = user

    # Set up sorting
    sort_order = pymongo.ASCENDING
    sort_field = "_id"  # default sort by MongoDB's internal ID
    if sort in ["title", "priority", "status", "deadline"]:
        sort_field = sort

    # Execute the query with sorting
    try:
        task_count = tasks.count_documents(query)
        if task_count == 0:
          print("No tasks found.")
          return
        
        task_list = tasks.find(query).sort(sort_field, sort_order)
        tasks_string = ""
        for task in task_list:
          tasks_string += (f"Title: {task['title']}, Description: {task['description']}, Priority: {task['priority']}, Status: {task['status']}, Deadline: {task['deadline']}, Assigned to: {task['user']}")
          tasks_string += "\n"
        return tasks_string
    except Exception as e:
        print(f"An error occurred while retrieving tasks: {e}")

# Main function to interact with user. Currently testing that functions work here
def main():
  insert_task("App interface", "Create the app interface", 2, "in progress", "Dec 15", "James")
  insert_task("Mongo Database", "Initialize mongo database", 3, "in progress", "Dec 15", "Charles")
  insert_task("Pick Nose", "Pick my nose", 1, "in progress", "Dec 15", "Charles")

  print(display_tasks(sort='priority', user="Charles"))
  # print(display_tasks())

if __name__ == "__main__":
    main()