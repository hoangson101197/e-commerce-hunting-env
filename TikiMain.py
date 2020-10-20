


TARGET_FILE = "C:/Users/hoang/projects/e-commerce_hunting/e-commerce_hunting_env/category_list.txt"
targetFile = open(TARGET_FILE, "r", encoding="utf8")
lines = targetFile.readlines()
targetFile.close()

for line in lines:
    print("~" + line.strip() + "~")