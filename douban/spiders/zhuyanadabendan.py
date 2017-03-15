# -*- coding utf-8 -*-
import re
from scrapy.contrib.spiders import CrawlSpider
from ..IOText.writefile import FileIO
from scrapy.http import Request
from scrapy.selector import  Selector
from movieInfo import ShoujiInfo,IntroInfo
from douban.items import ShoujiinfoItem,IntroItem



class SHOUJI360(CrawlSpider):
    name = "dabendan"
    start_urls=["http://zhushou.360.cn/list/index/cid/11/?page=1"]
    pre_url = "http://zhushou.360.cn/"
    fo = FileIO()
    introinfo = []
    filename =''

    def parse(self, response):
        item = ShoujiinfoItem()
        introitem = IntroItem()
        selector = Selector(response)
        shoujiinfo = selector.xpath('//div[@class="icon_box"]/ul[@class="iconList"]/li')
        for eachInfo in shoujiinfo:
            title = eachInfo.xpath('h3/a/text()').extract()[0]
            download_times = eachInfo.xpath('span/text()').extract()[0]
            item['title'] = title.encode("utf-8")
            item['download_times'] = download_times.encode("utf-8")
            backurl = eachInfo.xpath('a/@href').extract()[0]
            url = self.pre_url + backurl
            yield Request(url, callback = self.getIntro, meta = {'item':IntroItem})
            # yield Request(url, callback=self.getIntro)
            # Request(url ,)
            # request.meta['item'] = request
            # print request.meta['item']
            # print self.introinfo[0] + "--------------"
            shouji360 = ShoujiInfo(item['title'], item['download_times'], '123', '234')
            self.filename = "./zhuyanadabendan/" + item['title'] + ".txt"
            # print str(len(self.introinfo)) + "-----------"
            writeline = str(shouji360.title) + "\n" + str(shouji360.download_time) + "\n"
            self.introinfo = []
            FileIO.writeline(self.fo, writeline, self.filename)


    def getIntro(self, response):
        print "$$$$$$$$$$$$$$$@@@@@@@@@@@@@"
        # introinfotemp = IntroInfo()
        # item = IntroItem()
        selector = Selector(response)
        # filename = selector.xpath('//div[@class="warper"]/div[@class="main clearfix"]/div[@class="main-left fl"]/div[@class="product btn_type1"]/div[@class="app-clearfix"]/dd/h2/span/text()').extract()[0]
        filename = selector.xpath(
            '//div[@class="warper"]/div[@class="main clearfix"]/div[@class="main-left fl"]/div[@id="app-info-panel"]/div[@class="product btn_type1"]/dl[@class="clearfix"]/dd/h2/span/text()').extract()[0]
        intro = selector.xpath('//div[@class="warper"]/div[@class="main clearfix"]/div[@class="main-left fl"]/div[@class="infors"]/div[@class="mod-info"]/div[@class="infors-txt"]/div[@class="sdesc clearfix"]/div[@class="breif"]/text()').extract()
        # print "1111" + str(intro) + "************"
        tag = selector.xpath('//div[@class="warper"]/div[@class="main clearfix"]/div[@class="main-left fl"]/div[@class="infors"]/div[@class="app-tags"]/a/text()').extract()
        # print "2222" + str(tag) + "************"
        intros = ""
        tags = ""
        for intro_item in intro:
            intros = intros  + intro_item.encode("utf-8")
        for tag_item in tag:
            tags = tags + tag_item.encode("utf-8") + " "
        filename = filename.encode("utf-8")
        print filename
        self.introinfo.append(intro)
        self.introinfo.append(tag)
        filename = "./zhuyanadabendan/" + filename + ".txt"
        writeline = str(tags) + "\n" + str(intros)
        FileIO.writeline(self.fo,writeline, filename)
        # print "2222" + str(self.introinfo[1]) + "************"
        # print str(self.introinfo[0]) + "--------------"