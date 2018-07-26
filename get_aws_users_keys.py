"""
Get the available IAM users
and their access key IDs from a given Amazon Web Services account
"""

import json
# Use boto3 to access AWS resources
import boto3

def get_credentials(credential_filename):
    """ Get access keys from the credentials file """
    with open(credential_filename) as json_file:
        key = json.load(json_file)
    return key

def connect_to_aws(connection_keys):
    """ Connect to a aws system accoun with connection_keys.
        This function return a service client instance """
    aws_access_key_id = connection_keys["aws_access_key_id"]
    aws_secret_access_key = connection_keys["aws_secret_access_key"]
    session = boto3.Session(aws_access_key_id, aws_secret_access_key)
    client = session.client('iam')
    return client

def get_users_list(client):
    """ Return the list of the users found in a a service client instance.
        Each user has payrs of keys and key_values """
    return client.list_users()['Users']

def get_user_name(user):
    """ Get the value of the UserName key for a user """
    return user['UserName']

def get_access_key(client, user_name):
    """ Get the list of AccessKeys for a user identified by user name """
    return client.list_access_keys(UserName=user_name)['AccessKeyMetadata']

def get_users_keys(client, users_list):
    """ Get a dictionary object that contain information like:
    {UserName1: [Key1,...,Key_n],....,User_n: [Key1,...,Key_n] } """
    users_keys = {} # Create an empty dictinary
    for user in users_list:
        user_name = user['UserName']
        keys = [] # For each user create a list of keys
        for access_key in get_access_key(client, user_name):
            keys.append(access_key['AccessKeyId'])
        users_keys[user_name] = keys
        # and return the dictionary. The output will be: user_name:acces_keys_list
    return users_keys

def print_json(users_dictionary):
    """ Convert the users_keys dictionary into a valid json object and print it """
    json_object = json.dumps(users_dictionary)
    parsed = json.loads(json_object)
    print json.dumps(parsed, indent=4, sort_keys=True)

def generate_users_acceskeys_json():
    """ Generate a json object with Users and their access keys and print the json """
    connection_keys = get_credentials('credentials.json')
    iam_client = connect_to_aws(connection_keys)
    users_list = get_users_list(iam_client)
    print_json(get_users_keys(iam_client, users_list))

if __name__ == "__main__":
    generate_users_acceskeys_json()
