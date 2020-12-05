from threading import Thread
from TikiTarget import TikiTarget
from TikiItem import TikiItem
from TikiHelper import *
from bs4 import BeautifulSoup
import requests

class TikiHunterThread(Thread): #Kế thừa
    MAX_PAGE = 1

    def __init__(self, target):
        Thread.__init__(self)
        self.target = target
        self.bestItem = None
        self.name = target.getKeyword()

    def __findBestItem(self):
        # for to MAX_PAGE
        searchLink = self.target.getSearchLink(1)
        # print(searchLink)

        headers = {'user-agent': 'adsbot-google'}

        response = requests.get(searchLink, headers=headers)
        # print(response.text.encode('cp1252', errors='ignore'))

        bsoup = BeautifulSoup(response.text, "lxml")
        # <a> class = search-a-product-item
        listElement = bsoup.findAll("a", {"class": "product-item"})
        print(len(listElement))

        i = 0
        for e in listElement:
            print(str(i) + ": ")

            if(e.get_text().find("Đã hết hàng") >= 0 or e.get_text().find("Ngừng kinh doanh") >= 0):
                print("====== Đã hết hàng ======")
                continue

            newItem = TikiItem()
            product_name = e.find("div", {"class": "name"})
            newItem.product_name = product_name.span.text

            newItem.url = "https://tiki.vn" + e.get('href') 
            
            discount_price = e.find("div", {"class": "price-discount__price"})
            newItem.discount_price = convertToPrice(discount_price.text)

            review_num = e.find("div", {"class": "review"})
            if (review_num != None):
                newItem.review_num = review_num.text


            if(newItem.isValidItem(self.target.parterns)):
                print(newItem.info().encode('cp1252', errors='ignore'))
                if(self.bestItem == None):
                    self.bestItem = newItem
                else:
                    if(newItem.discount_price < self.bestItem.discount_price):
                        self.bestItem = newItem

            i+=1


        print("Best Item: ")
        if (self.bestItem != None):
            print(self.bestItem.info())
            print("==================")

    def run(self):
        print("Start Thread " + self.name)
        
        while True:
            self.__findBestItem()

        print("End Thread: " + self.name)
