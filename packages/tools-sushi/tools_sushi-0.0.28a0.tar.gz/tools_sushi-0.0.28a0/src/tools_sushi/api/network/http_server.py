from http.server import HTTPServer
from typing import Optional


class http_server():
    def __init__(self, handler: any, url: Optional[str] = '', port: Optional[int] = 8080, ready_function: Optional[any] = None) -> None:
        server = HTTPServer((url, port, ), handler)

        # user can execute custom function after http server start
        if ready_function != None:
            ready_function(url, port)

        try:
            server.serve_forever()
        except KeyboardInterrupt:
            server.server_close()
            exit(0)


def response(self, data: tuple[int, dict[str, str], tuple[str]]):
    self.send_response(data[0])

    for key, value in data[1].items():
        self.send_header(key, value)
    self.end_headers()

    for x in data[2]:
        self.wfile.write(str.encode(x))
