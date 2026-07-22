from __future__ import annotations

import argparse
import json
import mimetypes
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from solver import load_presets, optimize_positions, solve_spectrum


ROOT = Path(__file__).resolve().parent
STATIC = ROOT / "static"


class Handler(BaseHTTPRequestHandler):
    server_version = "EBPStudio/1.0"

    def _json(self, payload, status=200):
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/api/presets":
            return self._json(load_presets())
        relative = "index.html" if path == "/" else path.lstrip("/")
        target = (STATIC / relative).resolve()
        if STATIC.resolve() not in target.parents and target != STATIC.resolve():
            return self.send_error(403)
        if not target.is_file():
            return self.send_error(404)
        content = target.read_bytes()
        content_type = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
        self.send_response(200)
        self.send_header("Content-Type", content_type + ("; charset=utf-8" if content_type.startswith("text/") else ""))
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def do_POST(self):
        path = urlparse(self.path).path
        try:
            length = int(self.headers.get("Content-Length", "0"))
            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            if path == "/api/solve":
                return self._json(solve_spectrum(payload))
            if path == "/api/optimize":
                settings = payload.pop("optimization", {})
                return self._json(optimize_positions(payload, **settings))
            return self.send_error(404)
        except (ValueError, KeyError, TypeError) as exc:
            return self._json({"error": str(exc)}, 400)

    def log_message(self, fmt, *args):
        print("[EBP] " + fmt % args)


def main():
    parser = argparse.ArgumentParser(description="EBP Vibration Studio")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()
    address = (args.host, args.port)
    server = ThreadingHTTPServer(address, Handler)
    url = f"http://{args.host}:{args.port}"
    print(f"EBP Vibration Studio disponible en {url}")
    print("Presione Ctrl+C para cerrar.")
    if not args.no_browser:
        threading.Timer(0.7, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()

