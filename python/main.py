from argparse import ArgumentParser
from server import Server

if __name__ == "__main__":
    args = ArgumentParser()
    args.add_argument("--host", "-o", default="127.0.0.1", type=str)
    args.add_argument("--port", "-p", default=8080, type=str)
    args.add_argument("--max_connections", "-c", default=32, type=int)
    args.add_argument("--buffer_size_kb", "-b", default=64, type=int)

    flags = args.parse_args()

    server = Server(
        host=flags.host,
        port=flags.port,
        max_connections=flags.max_connections,
        buffer_size_kb=flags.buffer_size_kb,
    )

    server.start_server()
    server.close_server()
