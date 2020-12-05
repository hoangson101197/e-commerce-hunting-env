from TikiTarget import TikiTarget
from TikiHelper import *
from TikiItem import TikiItem
from TikiHunterThread import TikiHunterThread
from TikiDisplayThread import TikiDisplayThread
import requests
from bs4 import BeautifulSoup 

TARGET_FILE = "C:/Users/hoang/projects/e-commerce_hunting/category_list.txt"
headers = {'user-agent': 'adsbot-google'}


targets = getTargetsFromFile(TARGET_FILE)

#========================================
threads = []

thread1 = TikiHunterThread(targets[0])
thread1.start()
# thread1.join() # đợi thread kết thúc mới tiếp tục các dòng lệnh dưới

thread2 = TikiHunterThread(targets[1])
thread2.start()
# thread2.join()
threads.append(thread2)

displayThread = TikiDisplayThread()
displayThread.addHunter(thread1)
displayThread.addHunter(thread2)
displayThread.start()
threads.append(displayThread)

for t in threads: # Chạy 2 thread cùng lúc
    t.join()

print("=== END MAIN ===")

# for target in targets:
#     print(target.info())

#========================================
# target = targets[1]
# searchLink = target.getSearchLink(1)

# response = requests.get(searchLink, headers=headers)
# # print(response.text.encode('cp1252', errors='ignore'))

# bsoup = BeautifulSoup(response.text, "lxml")
# # <a> class = search-a-product-item
# listElement = bsoup.findAll("a", {"class": "product-item"})
# print(len(listElement))

# bestItem = None

# i = 0
# for e in listElement:
#     print(str(i) + ": ")

#     if(e.get_text().find("Đã hết hàng") >= 0 or e.get_text().find("Ngừng kinh doanh") >= 0):
#         print("====== Đã hết hàng ======")
#         continue

#     newItem = TikiItem()
#     product_name = e.find("div", {"class": "name"})
#     newItem.product_name = product_name.span.text

#     newItem.url = "https://tiki.vn" + e.get('href') 
    
#     discount_price = e.find("div", {"class": "price-discount__price"})
#     newItem.discount_price = convertToPrice(discount_price.text)

#     review_num = e.find("div", {"class": "review"})
#     if (review_num != None):
#         newItem.review_num = review_num.text


#     if(newItem.isValidItem(target.parterns)):
#         print(newItem.info().encode('cp1252', errors='ignore'))
#         if(bestItem == None):
#             bestItem = newItem
#         else:
#             if(newItem.discount_price < bestItem.discount_price):
#                 bestItem = newItem

#     i+=1


# print("--END--")
# if (bestItem != None):
#     print(bestItem.info())
