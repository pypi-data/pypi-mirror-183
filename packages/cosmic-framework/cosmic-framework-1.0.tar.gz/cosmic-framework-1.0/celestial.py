import socket
from view import render as rd
from controller import requests as rq
from error import *
import os
import json
import signal

def parse_request(request):
    print(request)
    if request == "":
        return "GET", "/", ""
    lines = request.split("\n")
    method, path, headers = lines[0].split(" ")
    headers = dict(line.split(": ") for line in lines[1:-2])
    return method, path, headers

def parse_form(headers):
    if "Content-Type" not in headers:
        return {}
    if headers["Content-Type"] != "application/x-www-form-urlencoded":
        return {}
    return dict(pair.split("=") for pair in headers["Content-Length"].split("&"))

def get_project_name():
    meta_path = os.path.join(os.getcwd(), "meta.json")
    if not os.path.exists(meta_path):
        return False
    with open(meta_path, "r") as f:
        data = json.load(f)
        return data["project"]

def handle_sigint(signal, frame):
    # if conn:
    #     conn.close()
    # sock.close()

    print("Your server has been closed. Thanks for connecting!")

    exit(0)


signal.signal(signal.SIGINT, handle_sigint)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 8080))
sock.listen(8080)

conn = False

while True:
    print("Celestial Server is listening at port 8080...\nTo close the server, visit http://localhost:8080 and then press Ctrl-C on the terminal")
    conn, addr = sock.accept()
    request = conn.recv(1024).decode("utf-8")
    project_name = get_project_name()

    if not project_name:
        http_error = generate_error(500, "Project files not initialised")
        print("Project files not initialized")
        conn.sendall(http_error.encode("utf-8"))
        conn.close()
        break

    method, path, headers = parse_request(request)
    form = parse_form(headers)
    response = rq.handle_request(project_name, path, method, form)
    conn.sendall(response.encode("utf-8"))
    conn.close()

