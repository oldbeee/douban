#!/bin/bash

cd /Users/biwangshen/gitDocuments/douban
PATH = $PATH:/usr/local/bin
export PATH
scrapy crawl zufang

##basepath = $(cd `dirname $0`; pwd)
#baseDirForScriptSelf=$(cd "$(dirname "$0")"; pwd)
#echo "full path to currently executed script is : ${baseDirForScriptSelf}"
#cd ${baseDirForScriptSelf}
#echo `pwd` >> /Users/biwangshen/gitDocuments/douban/aaaaa.txt
echo "hello1 biwangsjem" >> /Users/biwangshen/gitDocuments/douban/aaaaa.txt
##cur_dir = $(pwd)
##echo $cur_dir >> /Users/biwangshen/gitDocuments/douban/aaaaa.txt
#python /Users/biwangshen/gitDocuments/douban/main.py
