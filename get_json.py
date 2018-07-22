# Use boto3 to access AWS resources
import boto3
import json
from pprint import pprint


def getCredentials (credentialFilename):
    with open(credentialFilename) as json_file:
        key = json.load(json_file)
    return key

def connectToAws (connection_keys):
    session = boto3.Session(connection_keys["aws_access_key_id"],connection_keys["aws_secret_access_key"])
    client = session.client('iam')
    return client

def getUsersList (client):
    return client.list_users()['Users']

def getUserName (user):
    return user['UserName']

def getAccessKey (client, user_name):
    return client.list_access_keys(UserName=user_name)['AccessKeyMetadata']

def getUsersKeys (client, users_list):
    users_keys = {} # Create an empty dictinary
    for user in users_list:
        user_name = user['UserName']
        keys = [] # For each user create a list of keys
        for access_key in getAccessKey(client,user_name):
            keys.append(access_key['AccessKeyId'])
        users_keys[user_name] = keys
        # and return the dictionary. The output will be: user_name:acces_keys_list
    return users_keys

def print_json (users_dictionary):
    json_object = json.dumps(users_dictionary)
    parsed = json.loads(json_object)
    print json.dumps(parsed, indent=4, sort_keys=True)


connectionKeys = getCredentials('credentials.json')
iamClient = connectToAws(connectionKeys)
usersList = getUsersList(iamClient)
print_json(getUsersKeys(iamClient, usersList))

