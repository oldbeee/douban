import os

class FileIO():

    def __init__(self):
        self.signtab = "\t"
        self.signenter = "\n"

    def openfile(self, file_url):
        fo = open(file_url, "wb")
        return fo

    def writeline(self, movieinfo, file_url):
        if os.path.exists(file_url):
            fo = open(file_url, "a")
            fo.write(movieinfo)
        else:
            fo = open(file_url, "w")
            fo.write("TODAY INFO LIST \n")
            fo.write(movieinfo)
        fo.close()

    def closefile(selfs, fo):
        fo.close()

    def writefile(self, file_url, movielist):
        fo = open(file_url, "wb")
        writeIndex = "Index" + self.signtab + "Title" + self.signtab + "Quote" + self.signtab + \
            "Critical" + self.signtab + "Star" + self.signtab + "MovieInfo" + self.signenter
        fo.write(writeIndex)
        for movieinfo in movielist:
            writeline = str(movieinfo.Index) +  self.signtab + str(movieinfo.title) + self.signtab + str(movieinfo.quote) + \
                        self.signtab + str(movieinfo.critical) + self.signtab + str(movieinfo.star) + self.signtab + \
                        str(movieinfo.movieInfo) + self.signenter
            fo.write(writeline)
        fo.close()