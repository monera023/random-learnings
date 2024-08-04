import socket
import sys

def handle_request(port):
    s = socket.socket()
    try:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('', port))
        print(f"Staring server to listen on port={port}..")
        s.listen()
        # TODO: Not doing while True for s.accept right now.. lets see what happens
        while True:
            new_conn = s.accept()
            print(f"Got new conn on socket..{new_conn[1]}")
            # Socket on which to receive request
            new_socket = new_conn[0]
            resp = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 6\r\nConnection: close\r\nHello!\r\n\r\n"

            while True:
                data = new_socket.recv(4096)
                if not data:
                    # Client closed conn
                    break
                print(f"DATA = {data.decode()}")
                if b"\r\n\r\n" in data:
                    print("Done with data")
                    new_socket.sendall(resp.encode())
                    new_socket.close()
                    break
    finally:
        s.close()


if __name__ == "__main__":
    port = 28333
    if len(sys.argv) > 1:
        port = sys.argv[1]
    handle_request(port)
