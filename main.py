import discord
client = discord.Client('NDYzMDkzNTE1ODk5ODk1ODA5.DvSPRQ.rpijLCzjjojOLGG2FzcqP9tbmno')\

channels =[]
for server in client.servers:
    for channel in server.channels:
        channels.append(channel)
print('PPP')

while True:
    for channel in channels:
        for message in channel.get_new_messages():
            print("{}| {}".format(channel.name, str(message)))
