require 'json'
require 'aws-sdk'

def get_credentials(filename)
    data = JSON.parse(File.read(filename))
    return data
end

def aws_client(credentials)
    client = Aws::IAM::Client.new(
       access_key_id: credentials['aws_access_key_id'],
       secret_access_key: credentials['aws_secret_access_key'],
       region: 'us-east-1'
    )
    return client
end

def get_users_with_access_keys(client)
    puts "{"
    client.list_users.users.each do |user|
        name=user.user_name
	puts "#{name}:["
        client.list_access_keys({user_name: name}).access_key_metadata.each do |key|
	    if key == client.list_access_keys({user_name: name}).access_key_metadata.last
      	        puts "#{key.access_key_id}"
	    else
		puts "#{key.access_key_id},"
	    end
        end
	if user == client.list_users.users.last
	    puts "]"
	else 
	    puts "],"
	end
    end
    puts "}"
end

aws_client = aws_client(get_credentials('credentials.json'))
get_users_with_access_keys(aws_client)
