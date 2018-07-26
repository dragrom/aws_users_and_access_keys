# Get the available IAM users
# and their access key IDs from a given Amazon Web Services account

require 'json'
require 'aws-sdk'

def get_credentials(filename)
    # Get access keys from the credentials file
    data = JSON.parse(File.read(filename))
    return data
end

def aws_client(credentials)
    # Connect to a aws system accoun with connection_keys.
    # This function return a client object
    client = Aws::IAM::Client.new(
       access_key_id: credentials['aws_access_key_id'],
       secret_access_key: credentials['aws_secret_access_key'],
       region: 'us-east-1'
    )
    return client
end

def get_users_with_access_keys(client)
    # Get the users and their access keys.
    # This method print information to stdout in a valid JSON format
    puts "{"
    client.list_users.users.each do |user|
        name=user.user_name
	    puts "#{name}:["
        client.list_access_keys({user_name: name}).access_key_metadata.each do |key|
            if key == client.list_access_keys({user_name: name}).access_key_metadata.last
                # If is the last element in the array, don't put the comma after access key ID
      	        puts "#{key.access_key_id}"
            else
                # Else put comma after access key ID
                puts "#{key.access_key_id},"
	        end
        end
        if user == client.list_users.users.last
            # If is the last element in the array, don't put the comma after ]
	        puts "]"
        else 
            # Else put comma after ]
	        puts "],"
	    end
    end
    puts "}"
end

if __FILE__ == $0
    aws_client = aws_client(get_credentials('credentials.json'))
    get_users_with_access_keys(aws_client)
end
