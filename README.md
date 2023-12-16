![example workflow](https://github.com/github/docs/actions/workflows/docker-image.yml/badge.svg)

# Final Project

Run the task management tool using the below command.
```
docker compose up --build
```


Helpful tip: If your docker is not working for some reason, run the following command to check docker storage usage.
```
docker system df
```
If it is necessary to free up space, AND YOU ARE OK WITH DELETING ALL CURRENT DOCKER IMAGES AND VOLUMES, run the following commands:
```
docker system prune
docker volume prune
```

An exercise to put to practice software development teamwork, subsystem communication, containers, deployment, and CI/CD pipelines. See [instructions](./instructions.md) for details.
Certainly! Let's delve into a more detailed description of the **Task Management Tool** project, adapting the first subsystem to be a terminal-based Python application.

### Project Overview: Task Management Tool

The Task Management Tool is designed to help teams organize, assign, and track tasks efficiently. It's particularly suited for small to medium-sized project teams looking for a simple yet effective way to manage their workflow.

#### Subsystem 1: Terminal-Based Python Application
- **Functionality:** 
  - **Task Management:** Create, view, edit, and delete tasks. Each task will have attributes like title, description, priority, status (e.g., pending, in-progress, completed), and deadlines.
  - **User Management:** Add and manage team members. Assign tasks to specific members and track their progress.
  - **Filtering and Searching:** Filter tasks based on different criteria (e.g., deadline, priority, assignee) and search for specific tasks.
  - **Notifications:** Send reminders for upcoming deadlines or pending tasks.
- **Implementation:** 
  - **Language:** Python.
  - **Libraries:** Libraries like `click` or `argparse` for creating the command-line interface, `datetime` for handling dates, and possibly `sqlite3` for local data storage if needed before integration with MongoDB.
  - **Design:** Command-line arguments and interactive prompts for user input. Output displayed in a formatted and readable manner.
  - **Tests:** There should be pytests to test >80% of the code.

#### Subsystem 2: MongoDB Database
- **Functionality:** 
  - **Data Storage:** Stores all task-related data, including task details and user information.
  - **Relationships:** Manages relationships between tasks and users, such as task assignments.
  - **Scalability:** Capable of scaling to handle a larger number of tasks and users as the team grows.
- **Implementation:** 
  - **MongoDB Collections:** Separate collections for tasks, users, and possibly task history for tracking changes.
  - **Data Modeling:** Schema design to efficiently store and retrieve task-related information.
  - **Integration:** Connects with the Python application through a driver like `pymongo`.

