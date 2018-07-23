# Project Title

Get the available IAM users and their access key IDs from a given Amazon Web Services account

## License

This project  is licensed under the Apache-2.0 License

## Getting Started

Install git on your machine:
- on Ubuntu:
```
apt-get install git
```
- on CentOS:
```
yum install git
```
- on MacOS:
```
 http://mac.github.com
```

- on Windows:
```
http://git-scm.com/download/win
```
Clone the repository to local machine:
https://github.com/dragrom/aws_users_and_access_keys.git

Go to aws_users_and_access_keys directory:
```
cd aws_users_and_access_keys
```

### Prerequisites

Python: https://www.python.org/getit/
Pip: https://pip.pypa.io/en/stable/installing/
boto3 module: pip install boto3

### Usage

Go to aws_users_and_access_keys directory (use cd aws_users_and_access_keys)
Create credentials.json file, with the wollowing structure:

```
{
    "aws_access_key_id": your_access_key,
    "aws_secret_access_key": your_secret_key
}
```
Run the script, using the following command: python get_aws_users_keys.py

The script will return an output like this:
```
{ 
"User1" : [
"AKIAEXAMPLEKEY3" 
], 
"User3" : [ 
"AKIAEXAMPLEKEY2", 
"AKIAEXAMPLEKEY4" 
], 
"User2" : [ 
"AKIAEXAMPLEKEY1" 
] 
} 
```

### Coding style tests

pylint get_aws_users_keys.py

```
No config file found, using default configuration

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```

## Built With

This tool was built with Python 2.7.15rc1, using boto3 python mudule

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/dragrom/aws_users_and_access_keys/tags). 

## Author

* **Dragos Crisan** - *Initial work* - [aws_users_and_access_keys] (https://github.com/dragrom/aws_users_and_access_keys)
