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

## Programming Languages

The goal of this repository is to create a basic implementation in various different programming languages.
Currently, implemented languages include:

- [x] Python (tested on Python 3.10+)

## Running

To run the code, you can execute the main script in each folder. For example, for python, you can execute
`python main.py` from within the `python/` folder.

Moreover, each implementation will take in command line flags for configuration. For example, with python,
you can execute `python main.py --host=127.0.0.1 --port=8080` to start the server. This is the default configuration.
