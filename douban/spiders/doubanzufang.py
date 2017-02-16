# -*- coding: utf-8 -*-
import re
from time import strftime
from ..IOText.writefile import FileIO
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from douban.items import DoubanmovieItem, DoubanAiqingItem,DoubanZufangItem
from movieInfo import MovieInfo, Doubanzufang

class DoubanZufang(CrawlSpider):
    name = "zufang"
    start_urls = ["https://www.douban.com/group/550725/discussion?start=0"]
    url = "https://www.douban.com/group/550725/discussion?start=0"
    fangziList = []
    index = 0
    signtab = "\t"
    signenter = "\n"
    num = 0

    def parse(self, response):
        item = DoubanZufangItem()
        selector = Selector(response)
        fangziInfo = selector.xpath('//td[@class="title"]')
        for eachInfo in fangziInfo:
            title = eachInfo.xpath('a/@title').extract()[0]
            href = eachInfo.xpath('a/@href').extract()[0]
            item['title'] = title.encode("utf-8")
            item['url'] = href.encode("utf-8")
            #demo = u"滨兴"
            pattern = re.compile(r"滨兴|南岸|长兴|铂金名筑")
            zufangInfo = Doubanzufang(item['title'], item['url'])
            if pattern.search(item['title']):
                print item['title']
                self.fangziList.append(zufangInfo)
        print "**********" + str(self.num) + "*******"
        nextLink = selector.xpath('//span[@class="next"]/link/@href').extract()

        if self.num<10:
            yield Request(str(nextLink[0]), callback=self.parse)
            self.num = self.num + 1
        else:
            fileIO = FileIO()
            filename = "./_" + str(strftime("%Y_%m_%d")) + ".txt"
            #filename = "./_2017/02/14.txt"
            print filename
            # fo = fileIO.openfile("./zufanginfo.txt")
            fo = fileIO.openfile(filename)
            # print self.fangziList.count()
            for zufangInfo in self.fangziList:
                # print "-------------"
                # print self.fangziList.count()
                writeline = str(self.index) + "\t" + str(zufangInfo.title) + "\t" + str(zufangInfo.url) + "\n"
                self.index = self.index + 1
                fo.write(writeline)
            fo.close()


    # fileIO = FileIO()
    # fo = fileIO.openfile("./zufanginfo.txt")
    # #print self.fangziList.count()
    # for zufangInfo in  fangziList:
    #     print "-------------"
    #     print fangziList.count()
    #     writeline = str(index) + "\t" + str(zufangInfo.title) + "\t"+ str(zufangInfo.url) +"\n"
    #     index = index + 1
    #     fo.write(writeline)
    # fo.close()

