

class TikiItem:
    def __init__(self):
        self.product_name = ""
        self.discount_price = 0
        self.review_num = ""
        self.url = ""

    def info(self):
        return self.product_name + " | " + str(self.discount_price) + " | " + self.review_num + " | " + self.url

    def isValidItem(self, patterns):
        for p in patterns:
            if self.product_name.lower().find(p.lower()) < 0:
                return False
        return True