# REST API with Django using Python

![Untitled design (1)](https://github.com/redis/redis/assets/66990093/1b700804-6371-4732-9e9d-49908e33b6aa)
## Technical Details

The main focus will be to create a maintainable and highly testable architecture.
<br>
Following are the features of this project:

* **Programming Language:** The project is developed using Python, a powerful and flexible language known for its simplicity and readability.

* **Framework:** Django Rest Framework (DRF) is utilized to build the RESTful API. It provides a powerful toolkit for building Web APIs with ease and efficiency.

* **Containerization:** Docker is employed to containerize the application, ensuring that the software will behave the same way, regardless of where it is deployed.

* **uWSGI:** The project employs uWSGI as the application server. It serves as a bridge between the web server and the application, efficiently managing and routing requests.

* **Docker Compose:** The project uses Docker Compose for defining and running multi-container Docker applications. It provides an efficient way to run the application and its dependencies with a single command.

* **API Documentation:** Swagger is integrated for API documentation, making it easier for developers to understand and use the API endpoints effectively.

* **Caching:** Redis, an in-memory data structure store, is used to cache the results for improved performance and reduced database load.

* **Continuous Integration & Deployment:** The project uses GitHub Actions for CI/CD, automating the software delivery process.

* **Testing:** 
  - **Unit Testing:** Individual units of the project are tested to ensure they work as expected.
  - **Integration Testing:** Different units are combined and tested as a group to ensure they work together seamlessly.

* **Single Responsibility Principle:** The `FibonacciCalculator` class is implemented to ensure that each class has only one responsibility, improving modularity and readability.

* **Dependency Inversion:** To achieve the Dependency Inversion Principle, the project uses `redis_cache` and `cache_interface`. This ensures high-level modules are not dependent on low-level modules but both depend on abstractions.

* **Code Structure:** The project follows a clear directory structure, separating various functionalities like caching (`cache_interface.py`, `redis_cache.py`), utilities (`fibonacciCalculator.py`), and others for better maintainability.

* **Type Safety & Code Quality:** While Python is dynamically typed, tools like flake8 are used to enforce coding standards, ensuring consistent code quality throughout the project.

## How to Build and Run This Project

#### Build and Run using Docker Compose [**Recommended Method**]
  - **Setup**: 
    * Ensure you have Docker and Docker Compose installed on your machine.
      - [Detailed Installation Instructions for Docker and Docker Compose](https://docs.docker.com/install/)
  - **Build the Application**:
    * Navigate to the repository directory in your terminal.
    * Execute the command:
      ```
      docker-compose build
      ```
  - **Start the Application**:
    * After building, you can start the application with:
      ```
      docker-compose up
      ```
    * Once everything is up and running, access the API at: [http://localhost:8000/api/docs](http://localhost:8000/api/docs)
  - **Run Tests**:
    * Use the following command to run the tests within the Docker container: 
      ```
      docker-compose run --rm app sh -c "python manage.py test"
      ```

## API Examples

### GET `/n/`

This endpoint returns a number based on the input parameter `n`.

#### Request

```bash
curl -X 'GET' \
  'http://localhost:8000/5' \
  -H 'accept: */*'
```
#### Response
5

Status code: 200 OK

### GET `/n/` for values above 1000

If you request this endpoint with a value of 1000 or higher, the server will respond with a `400 Bad Request` status.

#### Request

```bash
curl -X 'GET' \
  'http://localhost:8000/1001' \
  -H 'accept: */*'
```
#### Response

Status code: 400 Bad Request


### API Documentation and Schema

API comes with built-in schema generation and interactive documentation. Here's how you can access and use them:

#### API Schema (`api/schema/`)

This endpoint provides a machine-readable description of the API, detailing its endpoints, responses, requests, and more, all presented in the form of an OpenAPI schema.

http://localhost:8000/api/schema/


Or, you can retrieve it programmatically:

```bash
curl -X 'GET' \
  'http://localhost:8000/api/schema/' \
  -H 'accept: application/json'
```

#### Interactive API Documentation (api/docs/)

For a more user-friendly way to view and test the API endpoints, you can use the interactive documentation provided by Swagger UI.

Simply open your browser and go to:

http://localhost:8000/api/docs/

![Untitled design (1)](https://github.com/redis/redis/assets/72294866/21c53ea5-a832-437a-9117-a12a4b60f02f)
