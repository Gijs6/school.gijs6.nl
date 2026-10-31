import base64
import hashlib
import os
import threading

from .config import COMPOSER_DIR

PATH = "/__livereload"
SCRIPT_PATH = os.path.join(COMPOSER_DIR, "livereload.js")
WEBSOCKET_GUID = b"258EAFA5-E914-47DA-95CA-C5AB0DC85B11"


def _accept_key(key):
    return base64.b64encode(hashlib.sha1(key.encode() + WEBSOCKET_GUID).digest())


def _text_frame(message):
    return bytes([0x81, len(message)]) + message


RELOAD_FRAME = _text_frame(b"reload")


def inject(html):
    with open(SCRIPT_PATH, "rb") as file:
        script = b"<script>\n" + file.read() + b"</script>\n"
    end = html.rfind(b"</body>")
    if end == -1:
        return html + script
    return html[:end] + script + html[end:]


class LiveReload:
    def __init__(self):
        self.lock = threading.Lock()
        self.clients = set()

    def serve(self, handler):
        key = handler.headers.get("Sec-WebSocket-Key")
        if handler.headers.get("Upgrade", "").lower() != "websocket" or not key:
            handler.send_error(400, "Expected a WebSocket upgrade")
            return

        handler.log_request(101)
        handler.wfile.write(
            b"HTTP/1.1 101 Switching Protocols\r\n"
            b"Upgrade: websocket\r\n"
            b"Connection: Upgrade\r\n"
            b"Sec-WebSocket-Accept: " + _accept_key(key) + b"\r\n\r\n"
        )
        handler.close_connection = True

        with self.lock:
            self.clients.add(handler.connection)
        try:
            handler.rfile.read(1)
        except OSError:
            pass
        finally:
            with self.lock:
                self.clients.discard(handler.connection)

    def reload(self):
        with self.lock:
            clients = list(self.clients)
        for client in clients:
            try:
                client.sendall(RELOAD_FRAME)
            except OSError:
                pass
