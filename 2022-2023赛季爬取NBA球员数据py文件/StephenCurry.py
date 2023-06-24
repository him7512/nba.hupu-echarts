##!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2023-6-1
# @Author : 刘奇
# @Email : lq010705@163.com
import requests
import csv
import lxml.etree

url = 'https://nba.hupu.com/players/stephencurry-3311.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit'
                  '/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari'
                  '/537.36 Edg/114.0.1823.51'
}

response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

# 使用lxml和XPath解析HTML文档
html_doc = lxml.etree.HTML(response.text)

# 查找包含库里赛季数据的表格行
trs = html_doc.xpath("/html/body/div[3]/div[3]/div[1]/div[3]/div[3]/div/div/div[1]/table[2]/tbody/tr")
trs2 = html_doc.xpath("/html/body/div[3]/div[3]/div[1]/div[3]/div[3]/div/div/div[2]/table[2]/tbody/tr")

# 定义新的表头行
new_header = [
    "赛季", "球队", "场次", "时间", "首发", "投篮", "二分命中率", "三分", "三分命中率", "罚球", "罚球命中率", "篮板", "助攻", "抢断", "盖帽", "失误","犯规","得分"
]

# 打开CSV文件进行写入
with open('StephenCurry_REGULAR.csv', 'w', newline="", encoding='utf-8') as f5:
    csv_writer = csv.writer(f5)
    csv_writer.writerow(new_header)
    for i in range(1, 16):
        csv_writer.writerow([
            trs[i].xpath("./td[1]/text()")[0],
            trs[i].xpath("./td[2]/text()")[0],
            trs[i].xpath("./td[3]/text()")[0],
            trs[i].xpath("./td[4]/text()")[0],
            trs[i].xpath("./td[5]/text()")[0],
            trs[i].xpath("./td[6]/text()")[0],
            trs[i].xpath("./td[7]/text()")[0],
            trs[i].xpath("./td[8]/text()")[0],
            trs[i].xpath("./td[9]/text()")[0],
            trs[i].xpath("./td[10]/text()")[0],
            trs[i].xpath("./td[11]/text()")[0],
            trs[i].xpath("./td[12]/text()")[0],
            trs[i].xpath("./td[13]/text()")[0],
            trs[i].xpath("./td[14]/text()")[0],
            trs[i].xpath("./td[15]/text()")[0],
            trs[i].xpath("./td[16]/text()")[0],
            trs[i].xpath("./td[17]/text()")[0],
            trs[i].xpath("./td[18]/text()")[0]
        ])
with open('StephenCurry_PLATOFFS.csv', 'w', newline="", encoding='utf-8') as f6:
    csv_writer = csv.writer(f6)
    csv_writer.writerow(new_header)
    for i in range(1, 10):
        csv_writer.writerow([
            trs2[i].xpath("./td[1]/text()")[0],
            trs2[i].xpath("./td[2]/text()")[0],
            trs2[i].xpath("./td[3]/text()")[0],
            trs2[i].xpath("./td[4]/text()")[0],
            trs2[i].xpath("./td[5]/text()")[0],
            trs2[i].xpath("./td[6]/text()")[0],
            trs2[i].xpath("./td[7]/text()")[0],
            trs2[i].xpath("./td[8]/text()")[0],
            trs2[i].xpath("./td[9]/text()")[0],
            trs2[i].xpath("./td[10]/text()")[0],
            trs2[i].xpath("./td[11]/text()")[0],
            trs2[i].xpath("./td[12]/text()")[0],
            trs2[i].xpath("./td[13]/text()")[0],
            trs2[i].xpath("./td[14]/text()")[0],
            trs2[i].xpath("./td[15]/text()")[0],
            trs2[i].xpath("./td[16]/text()")[0],
            trs2[i].xpath("./td[17]/text()")[0],
            trs2[i].xpath("./td[18]/text()")[0]
        ])
