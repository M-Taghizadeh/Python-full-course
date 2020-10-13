from selenium import webdriver
import time

url = "C:/Users/Zanis/AppData/Local/Programs/Python/Python35/Scripts/chromedriver.exe"
driver = webdriver.Chrome(url)

# go to google:
driver.get("https://google.com")
# find check box
search_box = driver.find_element_by_name("q")
search_box.clear()

# Enter Search Keywoard and submit
search_box.send_keys("دانشجویار")
search_box.submit()
time.sleep(5)
driver.quit()
