<h1 align="center">Flask & Redis - Multi container application</h1>

<p align="center">
  <img src="countervideo.gif" alt="Counter Video"/>
</p>

## Objective
The goal is to create a **multi-container application** that consists of a simple **Python Flask web application** and a **Redis database**. The Flask application will interact with Redis to store and retrieve a visit count.

## Requirements

### **Flask Web Application**
- A Flask app with two routes:
  - `/`: Displays a simple welcome message.
  - `/count`: Increments and displays a visit count stored in Redis.

### **Redis Database**
- Use **Redis** as a key-value store to track the visit count.

### **Dockerise Both Services**
- **Flask App**: Dockerize the Flask web application using a `Dockerfile`.
- **Redis**: Use the official Redis image and configure it with a `Dockerfile`.
- Use **Docker Compose** to orchestrate both the Flask and Redis containers.

## Test the Application

Access the Welcome Page:

Open your browser and go to http://localhost:5000 to see the welcome message. Test the Visit Count:

Navigate to http://localhost:5000/count to see the visit count increment each time you refresh the page!
