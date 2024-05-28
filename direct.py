import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


url = 'https://downloadwella.com/ao3ln7fqjm0u/Havana.(NKIRI.COM).2022.NF.WEB-DL.DOWNLOADED.FROM.NKIRI.COM.mkv.html'

def download(url):
    driver = webdriver.Chrome()
    driver.get(url)
    dbtn = driver.find_element(By.ID, 'downloadbtn')
    dbtn.send_keys(Keys.ENTER)
    
    return "Download started"

download(url)