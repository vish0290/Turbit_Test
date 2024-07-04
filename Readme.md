
# MongoDB and API Development Exercise



Objective:
Develop a pipeline that involves setting up a MongoDB database using Docker Compose, retrieving and storing data from an external API, and exposing this data through FastAPI.

Implementation

1. Setup MongoDB with Docker Compose
Docker Compose is used to set up a MongoDB database and link it with the FastAPI application. The docker-compose.yml file configures both the MongoDB and FastAPI services.

2. Data Retrieval and Loading into MongoDB
Data is retrieved from jsonplaceholder.typicode.com and stored in MongoDB using Python and the pymongo library.

3. Create a RESTful API with FastAPI
A FastAPI application is developed to provide access to the Mongo data. The application includes endpoints to report the total number of posts from each user and comments for each post, as well as endpoints to add, modify, and delete a user.

4. Test Cases with pytest
Pytest test cases have been added to ensure the functionality of the API endpoints. These tests help in verifying that the API performs as expected.

API Reference

Health Check
- **GET /**: Basic health check endpoint to ensure the API is running.

Data Load
- **GET /load_data**: Loads data from an external API (jsonplaceholder.typicode.com) into MongoDB.

Posts & Comments
- **GET /get_post_count/{user_id}**: Retrieves the count of posts and comments based on the user ID or post ID from the database.
- **GET /get_comments/{post_id}**: Retrieves the comments based on the post ID from the database.

Users
- **GET /get_users**: Retrieves all users from the database.
- **GET /get_user/{user_id}**: Retrieves a user based on the user ID from the database.
- **POST /create_user**: Creates a new user in the database.
- **PUT /update_user/{user_id}**: Updates an existing user in the database.
- **DELETE /delete_user/{user_id}**: Deletes a user from the database.

Usage
1. Set up MongoDB and FastAPI with Docker Compose
   - Ensure Docker and Docker Compose are installed on your machine.
   - Navigate to the project directory and run:
     ```sh
     docker-compose up
     ```

2. Load Data into MongoDB
   - Once the Docker containers are running, data can be loaded into MongoDB by accessing the /load_data endpoint.

3. Access FastAPI Endpoints
   - The FastAPI application will be available at http://127.0.0.1:8000.
   - Use a tool like curl or Postman to interact with the API endpoints.

4. Run Tests
   - To run the pytest test cases, use the following command:
     ```sh
     pytest
     ```

Dependencies
- Docker
- Docker Compose
- Python
- FastAPI
- Pymongo
- pytest

Files
- docker-compose.yml: Configures and sets up the MongoDB and FastAPI services.
- main.py: Contains the FastAPI application code (there are other depedent files).
- test.py: Contains the pytest test cases for the FastAPI application.
