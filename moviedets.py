from imdbpie import Imdb
class Movie(object):
    def __init__(self):
        pass
    def query_movie(self, query, data = None):
        imdb = Imdb()
        res = "\n"
        if query == "popularshows":
            ans = imdb.get_popular_shows()
            print(ans)
            for i in range(10):
                res += ans['ranks'][i]['title'] + "\n"
        elif query == "popularmovies":
            ans = imdb.get_popular_movies()
            print(ans)
            for i in range(10):
                res += ans['ranks'][i]['title'] + "\n"
        elif query == "search":
            ans = imdb.search_for_title(data)
            for i in range(5):
                res += ans[i]['title'] + " ("+ans[i]['year']+")\n"
        #return res
        if res == "\n":
            return "No Data found :("
        return res