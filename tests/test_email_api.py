# test_hello_add.py
from email.quoprimime import body_check
from time import sleep
from unittest.mock import patch
from api import app
from flask import json


#test the error handler
def test_error_handler():
    response = app.test_client().post(
        "/contact",
        data=json.dumps({"email": "","body": ""}),
        content_type="application/json"
    )
    assert response.status_code == 400
    assert response.json == {"message": "Bad request"}

#test the api endpoint
def test_api():
    response = app.test_client().post(
        "/contact",
        data=json.dumps({"email": "das.abhishek15@gmail.com", "body": "hello"}),
        content_type="application/json",
    )

    assert response.status_code == 200
    assert response.json == {"message": "Email sent!"}



#test the send_email function
def test_api_mock_patch():
    from unittest.mock import patch
    with patch("api.tasks.send_email") as mock_send_email:
        sleep(1)
        mock_send_email.return_value = "Email sent!"
        response = app.test_client().post(
            "/contact",
            data=json.dumps({"email": "das.abhishek15@gmail.com", "body": "hello"}),
            content_type="application/json",
        )
        assert response.status_code == 200
        assert response.json == {"message": "Email sent!"}

