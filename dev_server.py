#!/usr/bin/env python3
import argparse
import os
import signal
import subprocess
import sys
import time
from pathlib import Path


SERVER_CODE = r"""
import http.server
import sys


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()


port = int(sys.argv[1])
host = sys.argv[2]
server = http.server.ThreadingHTTPServer((host, port), NoCacheHandler)
print(f"Serving HTTP on {host} port {port} with no-cache headers", flush=True)
server.serve_forever()
"""


def tracked_files(root):
    return sorted([*root.glob("*.html"), *root.glob("*.txt"), *root.glob("themes/**/*.txt")])


def snapshot(root):
    result = {}
    for path in tracked_files(root):
        try:
            result[path] = path.stat().st_mtime_ns
        except FileNotFoundError:
            continue
    return result


def start_server(root, host, port):
    return subprocess.Popen(
        [
            sys.executable,
            "-c",
            SERVER_CODE,
            str(port),
            host,
        ],
        cwd=root,
    )


def stop_server(process):
    if process.poll() is not None:
        return

    process.terminate()
    try:
        process.wait(timeout=3)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8000, type=int)
    parser.add_argument("--interval", default=0.7, type=float)
    args = parser.parse_args()

    root = Path.cwd()
    current_snapshot = snapshot(root)
    process = start_server(root, args.host, args.port)
    print(f"Serving {root} at http://{args.host}:{args.port}/")
    print("Watching root HTML/TXT files and theme TXT files for server restart.")

    def shutdown(_signum=None, _frame=None):
        stop_server(process)
        raise SystemExit(0)

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    while True:
        time.sleep(args.interval)

        if process.poll() is not None:
            print("Server exited; restarting.")
            process = start_server(root, args.host, args.port)
            current_snapshot = snapshot(root)
            continue

        next_snapshot = snapshot(root)
        if next_snapshot != current_snapshot:
            changed = sorted(
                str(path.name)
                for path in set(current_snapshot) | set(next_snapshot)
                if current_snapshot.get(path) != next_snapshot.get(path)
            )
            print(f"Restarting server after change: {', '.join(changed)}")
            stop_server(process)
            process = start_server(root, args.host, args.port)
            current_snapshot = next_snapshot


if __name__ == "__main__":
    main()
