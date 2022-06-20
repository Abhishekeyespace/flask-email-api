from flask import Blueprint, Response

errors = Blueprint("errors", __name__)

#handle diffent error codes
@errors.errorhandler(400)
def bad_request(error):
    return Response("Bad request", status=400)

@errors.errorhandler(500)
def server_error(error):
    return Response("Server error", status=500)


