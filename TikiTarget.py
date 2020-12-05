

class TikiTarget:
    def __init__(self, parternStr = "", categoryStr = ""):
        self.parternsString = parternStr
        self.parterns = self.__splitPattern()
        self.categoryUrl = categoryStr
    def info(self):
        return "Parterns: " + str(self.parternsString) + " | category: " + self.categoryUrl

    def __splitPattern(self):
        newList = self.parternsString.split(",")
        i = 0
        while i < len(newList):
            newList[i] = newList[i].strip()
            i+=1
        return newList

    # Máy ảnh, lấy liền, Fujifilm => Máy ảnh lấy liền Fujifilm
    def getKeyword(self):
        keyword = ""
        for key in self.parterns:
            keyword = keyword + " " + key
        return keyword

    def getSearchLink(self, pageNum):
        return self.categoryUrl + "?q=" + self.getKeyword() + "&href=categorySearch&page=" + str(pageNum)
