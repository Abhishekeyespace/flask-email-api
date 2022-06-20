from flask import Flask, Response, jsonify, request

from api.tasks import send_email

from .errors import errors

app = Flask(__name__)
app.register_blueprint(errors)


@app.route("/")
def index():
    return Response("Hello, world!", status=200)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        email = request.json.get("email")
        body = request.json.get("body")
        if not email or not body:
            return jsonify({"message": "Bad request"}), 400
        response = send_email(email, body)
        if not response:
            return jsonify({"message": "Bad request"}), 400
        return jsonify({"message": "Email sent!"}), 200
    else:
        return jsonify({"message": "Hello, world!"}), 200
    

