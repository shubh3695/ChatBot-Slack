import json, requests

'''

@author ssaxena36

'''

class Currency(object):
    def __init__(self):
        self.bases = "Valid Bases:\n ['HKD', 'HRK', 'CHF', 'HUF', 'THB', 'SGD', 'CNY', 'BRL',\n'INR', 'ZAR', 'ILS', 'EUR', 'JPY', 'ISK', 'MXN', 'NOK',\n'AUD', 'RUB', 'NZD', 'PLN', 'CZK', 'CAD', 'IDR', 'DKK',\n'BGN', 'MYR', 'GBP', 'TRY', 'KRW', 'SEK', 'RON', 'PHP']"
    def getCurrency(self, fro, to):
        if fro == to:
            return "Same Conversion? Huh?\n" +self.bases
        query = 'https://api.fixer.io/latest?base='+fro.upper()+'&symbols='+to.upper()
        res = requests.get(query).json()
        print(res)
        if res.get('error', None) != None:
            return res['error']+'\n'+self.bases
        val = 'Base: '+res['base']+'\n'+'Date: '+res['date']+'\n'
        if res['rates'].get(to.upper(), None) == None:
            return val + ' Invalid Conversion.\n' + self.bases
        return val + fro.upper()+' to '+to.upper()+ ' : '+str(res['rates'][to.upper()])