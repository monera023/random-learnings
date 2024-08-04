import socket
import sys

def http_request(host):
    s = socket.socket()
    try:
        s.connect((host, 28333))

        http_get_request = "GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n"
        s.sendall(http_get_request.encode())

        resp = b""
        while True:
            data = s.recv(4096)
            if not data:
                break
            resp += data
            print(f"Resp = {resp.decode()}")
    finally:
        s.close()


if __name__ == "__main__":
    """
    
    """
    host = sys.argv[1]
    print(f"Doing http request for == {host}")
    http_request(host)

