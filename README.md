# Project Title

Get the available IAM users and their access key IDs from a given Amazon Web Services account. For this project, I created 2 scripts: one in python and one in ruby. Boothe scripts return the same result, users can use any of them.

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

- If you want to use python script:
  - Python: https://www.python.org/getit/
  - Pip: https://pip.pypa.io/en/stable/installing/
  - boto3 module: pip install boto3
- If you want to use ruby script:
  - ruby: 
    - On Debian (Debian, Ubuntu): sudo apt-get install ruby-full
    - On CentOS: sudo yum install ruby
    - On OS X: brew install ruby
  - aws-sdk gem: gem install aws-sdk

### Usage

Go to aws_users_and_access_keys directory (use cd aws_users_and_access_keys)
Create credentials.json file, with the wollowing structure:

```
{
    "aws_access_key_id": your_access_key,
    "aws_secret_access_key": your_secret_key
}
```
Run the script, using the following command: 
 - python script: python get_aws_users_keys.py
 - ruby script: ruby get_aws_users_keys.rb

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
- For python: pylint get_aws_users_keys.py

```
No config file found, using default configuration

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)
```
- For ruby: ruby -c get_aws_users_keys.rb 

```
Syntax OK
```

## Built With

The python script was built with Python 2.7.15rc1, using boto3 python mudule
The ruby script was build with ruby 2.5.1p57, using aws-sdk 

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/dragrom/aws_users_and_access_keys/tags). 

## Author

* **Dragos Crisan** - *Initial work* - [aws_users_and_access_keys] (https://github.com/dragrom/aws_users_and_access_keys)
