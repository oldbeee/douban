from ..IOText.writefile import FileIO
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from douban.items import DoubanAiqingItem
from movieInfo import MovieInfo,AiQingMovieInfo

class AQdianying(CrawlSpider):
    name = "aiqingdianying"
    start_urls = ['https://movie.douban.com/tag/%E7%88%B1%E6%83%85']
    movielist = []

    def parse(self, response):
        item = DoubanAiqingItem()
        selector = Selector(response)
        Movies = selector.xpath('//tr[@class="item"]')
        for eachMovie in Movies:
            # title = eachMovie.extract()
            title = eachMovie.xpath('td/div[@class="pl2"]/a/text()').extract()[0]
            # title = eachMovie.xpath('td/div[@class="pl2"]').extract()
            print "-----------------------------------", title
            item['title'] = title.encode("utf-8")
            aiqingmovieInfo = AiQingMovieInfo(item['title'])
            self.movielist.append(aiqingmovieInfo)
            # yield item
        fileIO = FileIO()
        fo = fileIO.openfile("./aiqingmovie.txt")
        for movieInfo in self.movielist:
            writeline = str(movieInfo.title) + "\n"
            fo.write(writeline)
        fo.close()


