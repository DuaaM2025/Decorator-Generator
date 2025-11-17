# **Python File Line Generator**

Through my research on Python generators, I explored how to efficiently read large files line by line without loading the entire file into memory.
This project demonstrates a simple generator function generate_readfile that yields each line from a file, stripped of leading and trailing whitespace.
The output will be:

Hello World
This is a task
Python generators are powerful

# **FastAPI Execution Time Logger**

Through my research on Python decorators and their use in FastAPI, I explored how to track the execution time of API endpoints efficiently.
This project demonstrates a simple log decorator that measures how long each endpoint takes to execute and prints the result to the console.

Example Output

When accessing the endpoint:

GET http://127.0.0.1:8000/


in the console:

Endpoint 'welcome' executed in 0.0012 seconds


The response from the endpoint will be:

{"message": "Welcome, FastAPI"}


This output shows the duration of the endpoint execution, helping in monitoring performance and debugging.
