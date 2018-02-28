from pycricbuzz import Cricbuzz


class Cricket(object):
    def __init__(self):
        self.c = Cricbuzz()
    def score(self):
        matches = self.c.matches()
        val = '\n'
        for match in matches:
            if match['mchstate'] != 'nextlive':
                d = (self.c.livescore(match['id'])['matchinfo'])
                val += 'Match Description: ' + d['mchdesc']+', '+d['srs']+'.\n'
                val += 'Match Type: ' + d['type'] + '\n'
                val += 'Match State: ' + d['mchstate'] + '\n'
                val += 'Match Status: ' + d['status'] + '.\n\n'
        if val == '\n':
            return "No Match Updates.. :("
        return val