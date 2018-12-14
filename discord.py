import requests

channel_types_discord = {
    0: 'server_text',
    1: 'dm',
    2: 'sever_voice',
    3: 'group_dm',
    4: 'server_category'
}
channel_types = {
        'server_text': 0,
       'server_voice': 1,
    'server_category': 2,
                 'dm': 3,
           'group_dm': 4
}


class Server:
    def __init__(self, id, name, channels):
        self.id = int(id)
        self.name = str(name)
        self.channels = list(channels)


class Channel:
    def __init__(self, client, id, name, type):
        self.client = client
        self.id = id
        self.name = name
        self.type = channel_types[channel_types_discord[type]]
        self.last_msg_id = self.__call_api__()['last_message_id']

    def __call_api__(self, url=''):
        base_url = 'channels/{}'.format(self.id)
        return self.client.__call_api__('{}{}'.format(base_url,url))

    def get_new_messages(self):
        messages = self.__call_api__(url='/messages?after={}'.format(self.last_msg_id))
        l_messages = []
        if messages:
            for message in messages:
                l_messages.append(
                    Message(
                        message['content'],
                        message['author']
                    )
                )
            self.last_msg_id = messages[-1]['id']
        return l_messages


class Message:
    def __init__(self, text, author):
        self.text = text
        self.author = User(author['username'], author['id'])

    def __str__(self):
        return '{}: {}'.format(self.author, self.text)


class User:
    def __init__(self, name, id):
        self.name = name
        self.id = int(id)

    def __str__(self):
        return self.name


class Client:
    def __init__(self, token):
        self.token = token
        self.servers = []
        self.__populate_servers__()

    def __call_api__(self, url):
        resp = requests.get('https://discordapp.com/api/{}'.format(url), headers={'authorization': self.token})
        return resp.json()

    def __populate_servers__(self):
        for server in self.__call_api__('users/@me/guilds'):
            lserver = self.get_server(server['id'])
            self.servers.append(lserver)

    def get_server(self, id):
        base_url = "guilds/{}".format(id)
        base_json = self.__call_api__(base_url)
        channels = self.__call_api__(base_url+'/channels')
        l_channels = []
        for channel in channels:
            if channel['type'] == 0 or channel['type'] == 1 or channel['type'] == 3:
                l_channels.append(
                    Channel(
                        self,
                        channel['id'],
                        channel['name'],
                        channel['type']
                    )
                )

        return Server(base_json['id'], base_json['name'], l_channels)
