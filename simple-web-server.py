#!C:\Program Files\Python310\

#simple web server to recieve POST requests from the chrome-extract script
from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post():
    data = request.get_json()
    with open("received_data.txt", "w") as file:
        file.write(str(data))
    return "Data received and stored"

if __name__ == '__main__':
    app.run(debug=True, host='192.168.0.19')