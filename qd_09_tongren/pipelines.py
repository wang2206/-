# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import csv
import os

from itemadapter import ItemAdapter


# class CsvPipeline(object):
#     # CSV数据，保存
#     def __init__(self):
#         self.file = open('tongren.csv', mode='a', encoding='utf-8', newline='')
#         self.csv_write = csv.DictWriter(self.file, fieldnames=['href','title', 'name','date','text'])
#         self.csv_write.writeheader()
#
#     def process_item(self, item, spider):
#         d = dict(item)
#         self.csv_write.writerow(d)
#         return item
#
#     def close_spider(self, spider):
#         self.file.close()
class TextPipeline(object):
    def __init__(self):
        self.result = "小说/"

    def process_item(self, item, spider):
        title = item['title']
        span = item['span']
        h1 = item['h1']
        text = item['text']
        if not os.path.exists(self.result + title):
            os.makedirs(self.result + title)
        if not os.path.exists(self.result + title + "/" + h1):
            with open(self.result + title + "/" + h1+'.txt', mode='w', encoding='utf-8') as f:
                info = title + '\n' + span + '\n' + '  ' + text
                f.write(info)
        return item
        # self.file = open('小说\\' + f'{title}\\' + h1 + '.txt', mode='w', encoding='utf-8')
        # info = title + '\n' + span + '\n' + '  ' + text
        # self.file.write(info)

