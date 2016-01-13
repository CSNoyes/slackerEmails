from slacker import Slacker

slack = Slacker('API KEY HERE')
users = slack.users.list()
users = users.body['members']

outputFile = open('emails.txt','w')

for user in users:
    if 'email' in user['profile'].keys():
        if user['profile']['email'] is not None:
            outputFile.write(user['profile']['email'] + '\n')