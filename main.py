import discord
from threading import Thread

client = discord.Client('NDYzMDkzNTE1ODk5ODk1ODA5.DvSPRQ.rpijLCzjjojOLGG2FzcqP9tbmno')\

active_server_idx = 0
print('Init done')

print('Servers:')
for idx, server in enumerate(client.servers):
    print('{}| {}'.format(idx, server.name))
active_server_idx = int(input('Server: '))
print('Channels:')
for idx, channel in enumerate(client.servers[active_server_idx].channels):
    print('{}| {}'.format(idx, channel.name))
active_channel_idx = int(input('Channel: '))

active_channel = client.servers[active_server_idx].channels[active_channel_idx]


def message_thread ():
    global active_channel, client
    while True:
        for message in active_channel.get_new_messages():
            print(message)


msg_disp_thr = Thread(target=message_thread)
msg_disp_thr.start()

print (active_channel.id)

while True:
    uin = input('> ')
    active_channel.send_message(uin)
