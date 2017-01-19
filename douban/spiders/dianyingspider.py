# -*- coding: utf-8 -*-
import sys

import scrapy

from ..IOText.writefile import FileIO
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from douban.items import DoubanmovieItem
from movieInfo import MovieInfo


class Douban(CrawlSpider):
    name = "douban"
    start_urls = ['http://movie.douban.com/top250']
    #url = 'http://movie.douban.com/top250'
    url = "http://movie.douban.com/top250"
    movieList = []
    index = 0
    signtab = "\t"
    signenter = "\n"

    def parse(self, response):
        # print response.body

        item = DoubanmovieItem()
        selector = Selector(response)
        Movies = selector.xpath('//div[@class="info"]')
        for eachMoive in Movies:
            title = eachMoive.xpath('div[@class="hd"]/a/span/text()').extract()
            fullTitle = ''
            for each in title:
                fullTitle += each
            movieInfo = eachMoive.xpath('div[@class="bd"]/p/text()').extract()
            star = eachMoive.xpath('div[@class="bd"]/div[@class="star"]/span/text()').extract()[0]
            critical = eachMoive.xpath('div[@class="bd"]/div[@class="star"]/span/text()').extract()[1]
            quote = eachMoive.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()

            if quote:
                quote = quote[0]
            else:
                quote = ''
            item['title'] = fullTitle.encode('utf-8')
            item['movieInfo'] = ';'.join(movieInfo).encode('utf-8')
            item['star'] = star.encode('utf-8')
            item['critical'] = critical.encode('utf-8')
            item['quote'] = quote.encode('utf-8')
            # self.index = self.index+1
            movieInfo = MovieInfo(item['title'], item['quote'], item['critical'], item['star'], item['movieInfo'])
            self.movieList.append(movieInfo)
            yield item
        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()
        if nextLink:
            nextLink = nextLink[0]
            print nextLink
            yield Request(self.url + nextLink, callback=self.parse)
        else:
            moviesortedlist = sort_start(self.movieList)
            fileurl = "./movie_collection.txt"
            filestarurl = "./star_collection.txt"
            # FileIO.writefile(fileurl, self.movieList)
            fileIO = FileIO()

            fo = fileIO.openfile(fileurl)
            writeIndex = "Index" + self.signtab + "Title" + self.signtab + "Quote" + self.signtab + \
                         "Critical" + self.signtab + "Star" + self.signtab + "MovieInfo" + self.signenter
            fo.write(writeIndex)
            for moveInfo in moviesortedlist:
                self.index = self.index + 1
                writeline = str(self.index) + self.signtab + str(moveInfo.title) + self.signtab + str(moveInfo.quote) + \
                            self.signtab + str(moveInfo.critical) + self.signtab + str(moveInfo.star) + self.signtab + \
                            str(moveInfo.movieInfo) + self.signenter
                print writeline
                fo.write(writeline)
            fo.close()


def sort_start(movielist):
    sortedlist = []
    sorttemplist = movielist
    High_Scor = -1

    while len(sorttemplist) > 0:
        for movieinfo in sorttemplist:
            if movieinfo.star > High_Scor:
                High_Scor = movieinfo.star
                movietempinfo = movieinfo
        sorttemplist.remove(movietempinfo)
        sortedlist.append(movietempinfo)
        High_Scor = -1
    return sortedlist


