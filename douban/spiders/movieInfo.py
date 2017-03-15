class MovieInfo():
    def __init__(self, title, quote, critical, star, movieInfo):
        # self.Index = Index
        self.title = title
        self.quote = quote
        self.critical = critical
        self.star = star
        self.movieInfo = movieInfo

class AiQingMovieInfo():
    def __init__(self, title):
        self.title = title


class Doubanzufang():
    def __init__(self, title, url):
        #self.price = price
        self.title = title
        self.url = url

class ShoujiInfo():
    def __init__(self, title, download_time, intro, tag):
        self.title = title
        self.download_time = download_time
        self.intro = intro
        self.tag = tag

class IntroInfo():
    def __init__(self, intro, tag):
        self.intro = intro
        self.tag = tag