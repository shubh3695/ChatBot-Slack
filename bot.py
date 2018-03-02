import time
import event
from slackclient import SlackClient

'''

@author ssaxena36

'''

class Bot(object):
    def __init__(self):
        '''
        Ensuring Safety of API Token
        '''
        file = open("/home/ssaxena36/Desktop/Hack36Apps/key.txt", "r")
        self.slack_client = SlackClient(file.read().strip())
        self.bot_name = "py3bot"
        self.bot_id = self.get_bot_id()

        if self.bot_id is None:
            exit("Error, could not find " + self.bot_name)

        self.event = event.Event(self)
        self.listen()

    def get_bot_id(self):
        api_call = self.slack_client.api_call("users.list")
        if api_call.get('ok'):
            # retrieve all users so we can find our bot
            users = api_call.get('members')
            for user in users:
                if 'name' in user and user.get('name') == self.bot_name:
                    return "<@" + user.get('id') + ">"

            return None

    def listen(self):
        if self.slack_client.rtm_connect(with_team_state=False):
            print("Successfully connected, listening for commands")
            while True:
                self.event.wait_for_event()
                time.sleep(1)
        else:
            exit("Error, Connection Failed")
