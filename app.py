from flask import Flask
from waitress import serve
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    # return "Hello World!"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    myip = s.getsockname()[0]
    myname = socket.gethostbyaddr(socket.gethostname())[0]
    s.close()
    greeting = 'Hello World from {}.\n'.format(myname) # 1.1
    return greeting


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
