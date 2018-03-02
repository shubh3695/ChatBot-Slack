import os.path
import sys, json
try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai
class AITalks(object):
    def __init__(self):
        file = open('/home/ssaxena36/Desktop/Hack36Apps/apiaikey.txt','r')
        self.CLIENT_ACCESS_TOKEN = file.read().strip()
        #print(self.CLIENT_ACCESS_TOKEN)
        self.ai = apiai.ApiAI(self.CLIENT_ACCESS_TOKEN)
    def converse(self, query):
        try:
            request = self.ai.text_request()
            request.lang = 'en'  # optional, default value equal 'en'
            request.query = query
            response = request.getresponse()
            encoding = response.info().get_content_charset('utf8')  # JSON default
            data = json.loads(response.read().decode(encoding))
            #print(data['result'].keys())
            data = data['result']
            if data['action'] == 'input.unknown':
                return ""
            data = data['fulfillment']
            data = data['speech']
            return data
        except:
            return ""
