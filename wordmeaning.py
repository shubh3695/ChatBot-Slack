from PyDictionary import PyDictionary

'''

@author ssaxena36

'''

class PyDict(object):
    def __init__(self):
        pass
    def getMeaning(self, word):
        dictionary=PyDictionary()	
        res = dictionary.meaning(word)
        if res == None:
            return "No Meanings Found."
        wkeys = res.keys()
        ans = ""
        for i in wkeys:
            ans += i+' :\n'
            count = 1
            for j in res[i]:
                ans += str(count)+'. '+j+'\n'
                count += 1
                if count == 6:
                    break
            ans += '\n'
        return ans
