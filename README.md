![Docker CI/CD](https://github.com/software-students-fall2023/5-final-project-stuytownustas/actions/workflows/docker-image.yml/badge.svg)

# Final Project

## Project Description: Task Management Tool
The Task Management Tool is designed to help individuals organize, assign, and track tasks efficiently. It's particularly suited for tech-savvy individuals looking for a simple yet effective way to manage their workflow.

### Subsystem 1: Terminal-Based Python Application
- **Functionality:** 
  - **Task Management:** Create, view, edit, and delete tasks. Each task will have attributes title, description, priority, status, and deadline.
- **Implementation:** 
  - **Language:** Python.
  - **Design:** Interactive webpage for for user input and content display. Output displayed in a formatted and readable manner.
  - **Tests:** Pytest is used to test >80% of the code.

### Subsystem 2: MongoDB Database
- **Functionality:** 
  - **Data Storage:** Stores all task-related data, including task details.
  - **Scalability:** Capable of scaling to handle a larger number of tasks as the user's demands grows.
- **Implementation:** 
  - **MongoDB Collections:** Separate collections for tasks, users, and possibly task history for tracking changes.
  - **Integration:** Connects with the Python application through a driver like `pymongo`.
 
## Project Members
[Luke Bernstein](https://github.com/lnbernstein)

[Charles Hu](https://github.com/comeom)

[James Luo](https://github.com/jamesluo802)

[Kevin Li](https://github.com/kevinli2260)


### Configuration Instructions

Pull Docker Image from Dockerhub: https://hub.docker.com/r/lukedocker12/finalproject.

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


