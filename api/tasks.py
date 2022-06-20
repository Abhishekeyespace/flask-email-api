import logging
import os
import time

import boto3
from botocore.exceptions import ClientError

# send email using SES
def send_email(email, body):
    ses_client = boto3.client("ses", region_name="us-west-2")
    CHARSET = "UTF-8"
    try:
        response = ses_client.send_email(
            Destination={
                "ToAddresses": [
                    email,
                ],
            },
            Message={
                "Body": {
                    "Text": {
                        "Charset": CHARSET,
                        "Data": body,
                    }
                },
                "Subject": {
                    "Charset": CHARSET,
                    "Data": "AWS SES Email API",
                },
            },
            Source="abhishek@eye.space",
        )
        return response["MessageId"]
    except ClientError as e:
        logging.error(e.response["Error"]["Message"])
        return None
