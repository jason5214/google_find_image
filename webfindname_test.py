#encoding:utf-8

from selenium import webdriver
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re,json,os,sys


option = webdriver.ChromeOptions()
option.add_argument('headless')
driver = webdriver.Chrome(chrome_options=option)
# driver = webdriver.Chrome()


for imgNO in range(66,80):
    driver.get("https://www.baidu.com/")
    driver.find_element_by_class_name("soutu-btn").click()
    driver.find_element_by_class_name("upload-pic")
    upload = driver.find_element_by_class_name("upload-pic")
    try:
        upload.send_keys("C:\\Users\Administrator\Desktop\DQD4\\"+str(imgNO)+".png")
    except:
        continue
    else:
        time.sleep(1)
        sreach_window = driver.current_window_handle  # 页面重定位
        bs = BeautifulSoup(driver.page_source, 'html.parser').find_all('div', {'class': 'guess-info-text'})
        bsimg = "NotFound"
        for i in bs:
            bsimg = i.find('a').text

        f = open('C:\\Users\Administrator\Desktop\python\DQDname.txt','a')
        print (imgNO,bsimg)
        print(imgNO,bsimg,file=f)
        f.close()


