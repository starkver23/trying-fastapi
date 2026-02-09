python works on backend
react on frontend
postgresql as database

know about the working of python



Client request server and server responds -> File server
Client request server and server responds using html/json -> Web server

So when we have frontend and database so what we do is get processed data and we use the backend to interact in between the frontend and database.
So, frontend request backend which sends a quyery to database which in response returns data to backend and then it returns it to frontend as html page (with or without data (only layout comes)).
the response is json data

REST (REPRESENTATIONAL STATE TRANSFER)
Client sends request for data to server the server responds with response (current state)
This state has to be in REPRESENTATIONAL format hence REST

In order for client to reach to the server: 
    The server opens some endpoints. eg: /api/products, /api/payments etc
    To build these endpoints we use API (APPLICATION PROGRAMMING INTERFACE)
    To access the server we need to access the API

How will the server accept the client's request?

We have https for web applications

HTTP gives certain methods: 
    GET: READING FROM THE SERVER
    POST: CREATE 
    PUT: UPDATE
    DELETE: DELETE






setup:

1. check if python is installed or not?
2. node js for frontend
3. git installed for push and pull in repo
4. web server -> uvicorn for python
5. create a venv for the particular project: python3 -m venve name-of-venv
6. go inside the venv by: . myenv/bin/activate
7. port number for server is 8000
8. run the server by going inside the venv and writing: uvicorn main:app --reload (app -> is the function call name)
9. Have pydantic -> data validation convert data from server to json
10. models.py -> holds data or represents data
11. BaseModel of pydantic helps in data validation. for example the price of a product can not be negative number so BaseModel ensures This
