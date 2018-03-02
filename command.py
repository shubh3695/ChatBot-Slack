from random import randint
import calculator, cricket, fixer, wordmeaning, news, moviedets, lyric, weathering, dialogflow

'''

@author ssaxena36

'''

class Command(object):
    def __init__(self):
        self.commander = ""
        self.commands = { 
            "jump" : self.jump,
            "help" : self.help,
            "hi" : self.hi,
            "calculate": self.calculate,
            "cricscore": self.cricscore,
            "currency": self.currency,
            "meaning" : self.meaning,
            "getnews": self.getnews,
            "imdb": self.imdb,
            "lyrics": self.lyrics,
            "weather": self.weather
        }
        self.info = {
            "jump" : "Just to check if I'm alive! ;)",
            "help" : "Get all possible commands!",
            "hi" : "Wish me Hi!",
            "calculate": "Calculate some arithmetic query!",
            "cricscore": "Get live cricket score!",
            "currency": "Get currency conversion!",
            "meaning" : "Find meaning of some word/phrase",
            "getnews": "Get news search",
            "imdb": "Get latest movies, tv series or search a movie",
            "lyrics": "Lyrics to a song you like!",
            "weather": "Weather to your searched location!"
        }
 
    def handle_command(self, user, command):
        response = "<@" + user + ">: "
        self.commander = command.split()
        if self.commander[0] in self.commands:
            response += self.commands[self.commander[0]]()
        else:
            res = dialogflow.AITalks().converse(' '.join(self.commander))
            if res == "":
                response += "Sorry I don't understand the command: " + self.commander[0] + ". "
                response += "Try @py3bot help for all commands."
            else:
                response += res
        return response
    def hi(self):
        m1, m2 = 0, 2
        responses = ["Hey Man, how are you", "Hi, its Py3Bot", "Yep! Here to help"]
        return responses[randint(m1, m2)] +". Try '@py3bot help for all commands."
    def jump(self):
        return "Beep Bop! Py3Bot will make you jump jump."
    def help(self):
        response = "\nCurrently I support the following commands:\r\n"
        for command in self.commands:
            response += command + ": "+self.info[command]+"\r\n"
        return response
    def calculate(self):
        if len(self.commander) != 4:
            return "Incorrect Parameter Sizes.\nExample:\n @py3bot calculate 1 + 2"
        return calculator.Calculator(float(self.commander[1]), float(self.commander[3]), self.commander[2]).solve()
    def cricscore(self):
        return cricket.Cricket().score()
    def currency(self):
        #from to
        # ex. currency USD to INR
        if len(self.commander) != 4:
            return "Incorrect Parameter Sizes.\nExample:\n @py3bot currency USD to INR"
        return fixer.Currency().getCurrency(self.commander[1], self.commander[3])
    def meaning(self):
        if len(self.commander) != 2:
            return "Incorrect Parameter Sizes.\nExample:\n @py3bot meaning star"
        return wordmeaning.PyDict().getMeaning(self.commander[1])
    def getnews(self):
        if len(self.commander) < 2:
            return "Incorrect Parameter Sizes.\nExample:\n @py3bot getnews Donald Trump"
        return news.News().getNews(' '.join(self.commander[1: ]))
    def imdb(self):
        if len(self.commander) < 2:
            return "Incorrect Parameter Sizes.\nExample:\n @py3bot imdb search Thor"
        if len(self.commander) == 2:
            return moviedets.Movie().query_movie(self.commander[1])
        else:
            return moviedets.Movie().query_movie(self.commander[1], self.commander[2])
    def lyrics(self):
        if len(self.commander) < 3:
            return "Incorrect Parameter Sizes.\nExample:\n @py3bot lyrics maroon5 , wait"            
        else:
            artist, song, i, onedone = "", "", 1, False
            for i in self.commander[1:]:
                if i == ',':
                    onedone = True
                    continue
                if not onedone:
                    artist += i+ ' '
                else:
                    song += i+ ' '
            if artist == "" or song == "":
                return "No Artist/Song?"
            return lyric.SongLyrics().getLyrics(artist, song)
    def weather(self):
        if len(self.commander) < 2:
            return "Incorrect Parameter Sizes.\nExample:\n @py3bot weather Allahabad"
        return weathering.Weathering().getWeather(' '.join(self.commander[1: ]))