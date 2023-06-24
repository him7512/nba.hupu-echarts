##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2023-6-1
# @Author : 刘奇
# @Email : lq010705@163.com
import csv
import lxml.etree
import requests

# 以浏览器的身份发送请求
# 场均得分前49位球员
url = 'https://nba.hupu.com/stats/players'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit'
                 '/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari'
                 '/537.36 Edg/114.0.1823.51'
}

response = requests.get(url ,headers=headers)
# print(response.text)
response.encoding = 'utf-8'
response.close()
#if response.ok:
#    print("请求成功")
#else:
#    print("请求失败")

#用lxml和XPath进行解析XML文件
html_doc = response.text
tree = lxml.etree.HTML(html_doc)

#将需要解析的链接整合成一个列表
htmls = ["https://nba.hupu.com"+tree.xpath("/html/body/div[3]/div[4]/div/div/span[1]/a/@href")[0]]            #得分

#对于每个链接取得相应的数据（用for循环获取）
for href in htmls:
    # print(href)  #打印出相应的网址
    resp = requests.get(href)
    resp.encoding = 'utf-8'
    kidhtml = lxml.etree.HTML(resp.text)
    trs = kidhtml.xpath("/html/body/div[3]/div[4]/div/table/tbody/tr")  #解析整个表

    if href == htmls[0]:
        f1 = open("PlayerScore.csv", 'w', newline="", encoding='utf-8')
        table_writer = csv.writer(f1)

        #选择需要的列
        table_writer.writerow([trs[0].xpath("./td[2]/text()")[0],
                             trs[0].xpath("./td[3]/text()")[0],
                                trs[0].xpath("./td[4]/text()")[0],
                               trs[0].xpath("./td[5]/text()")[0],
                             trs[0].xpath("./td[6]/text()")[0],
                                trs[0].xpath("./td[7]/text()")[0],
                               trs[0].xpath("./td[8]/text()")[0],
                               trs[0].xpath("./td[9]/text()")[0],
                             trs[0].xpath("./td[10]/text()")[0],
                               trs[0].xpath("./td[11]/text()")[0],
                             trs[0].xpath("./td[12]/text()")[0]])

        for tr in trs[1:]:
            name = tr.xpath("./td[2]/a/text()")[0]
            team = tr.xpath("./td[3]/a/text()")[0]
            score = tr.xpath("./td[4]/text()")[0]
            hitShot = tr.xpath("./td[5]/text()")[0]
            hitPossibility = round(float(tr.xpath("./td[6]/text()")[0].split("%")[0]) / 100, 3)   #调整百分数
            hitThree = tr.xpath("./td[7]/text()")[0]
            threeHitPossibility = round(float(tr.xpath("./td[8]/text()")[0].split("%")[0]) / 100, 3)
            freeThrow = tr.xpath("./td[9]/text()")[0]
            twoHitPossibility = round(float(tr.xpath("./td[10]/text()")[0].split("%")[0]) / 100, 3)
            times = tr.xpath("./td[11]/text()")[0]
            time = tr.xpath("./td[12]/text()")[0]

            table_writer.writerow([ name, team, score, hitShot, hitPossibility, hitThree, threeHitPossibility, freeThrow, twoHitPossibility,times,time])
