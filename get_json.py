# Use boto3 to access AWS resources
import boto3
import json
from pprint import pprint


def get_credentials (credentialFilename):
    with open(credentialFilename) as json_file:
        key = json.load(json_file)
    pprint(key["access_key_id"])

get_credentials('credentials.json')

