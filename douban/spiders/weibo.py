#! -*- encoding:utf-8 -*-
import re
import os
import time

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy.http import FormRequest

#from src.items import SrcItem


class WeiboSpider(CrawlSpider):
    '''
            这是一个使用scrapy模拟登录新浪微博的例子，
            希望能对广大的同学有点帮助 ，这是所有代码
    '''

    name = 'weibo'
    allowed_domains = ['weibo.com', 'sina.com.cn']

    def start_requests(self):
        username = '********'
        url = 'http://login.sina.com.cn/sso/prelogin.php?entry=miniblog&callback=sinaSSOController.preloginCallBack&user=%s&client=ssologin.js(v1.3.14)&_=%s' % \
              (username, str(time.time()).replace('.', ''))
        print url
        return [Request(url=url, method='get', callback=self.post_message)]

    def post_message(self, response):
        serverdata = re.findall('{"retcode":0,"servertime":(.*?),"nonce":"(.*?)"}', response.body, re.I)[0]
        print serverdata
        servertime = serverdata[0]
        print servertime
        nonce = serverdata[1]
        print nonce
        formdata = {"entry": 'miniblog',
                    "gateway": '1',
                    "from": "",
                    "savestate": '7',
                    "useticket": '1',
                    "ssosimplelogin": '1',
                    "username": '*******',
                    "service": 'miniblog',
                    "servertime": servertime,
                    "nonce": nonce,
                    "pwencode": 'wsse',
                    "password": '*******',
                    "encoding": 'utf-8',
                    "url": 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
                    "returntype": 'META'}

        return [FormRequest(url='http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.3.14)',
                            formdata=formdata, callback=self.check_page)]

    def check_page(self, response):
        url = 'http://weibo.com/'
        request = response.request.replace(url=url, method='get', callback=self.parse_item)
        return request

    def parse_item(self, response):
        with open('%s%s%s' % (os.getcwd(), os.sep, 'logged.html'), 'wb') as f:
            f.write(response.body)