# HTTP 1.1 Server

This repository contains a basic implementation for an HTTP Server. It is very basic in the sense that it
doesn't provide all the features you would expect from a full HTTP Server. This server currently only supports
GET requests, and for static resources defined in the server. However, with a basic infrastructure in place,
it should be easy to add support for dynamic routes and more advanced features.

## Features

- [x] GET Requests
- [x] Serve static resources (HTML, PNG, CSS)
- [x] Perform redirects
- [x] Serve 404 pages on missing resources
- [x] Basic validation for malformed requests

## Running

To run the code, you can execute the main script in each folder. For example, you can execute `python main.py` to 
start the server. The code was tested on Python 3.10+. Moreover, the implementation allows passing command line flags 
for configuration. For example, `python main.py --host=127.0.0.1 --port=8080`. This is also the default configuration.
