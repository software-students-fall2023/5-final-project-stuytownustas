FROM python:3.8-slim

# Set the working directory to /app
# WORKDIR /app

# Copy the current directory contents into the container 
COPY . .


# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5001

# Define environment variable
ENV MONGO_URI=""

# Run app.py when the container launches
# CMD ["python", "web_app.py"] sdfsf
CMD ["python", "app.py"]