import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
url = 'https://downloadwella.com/kaoaeztlu62g/Orion.and.the.Dark.(NKIRI.COM).2024.NF.WEBRip.DOWNLOADED.FROM.NKIRI.COM.mkv.html'
driver = webdriver.Edge()
driver.get(url)
time.sleep(20)
driver.maximize_window()
# window = driver.find_element(By.TAG_NAME, 'html')
# window.send_keys(Keys.PAGE_DOWN)
time.sleep(20)
print("Done")