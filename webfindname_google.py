# -*- coding:utf-8 -*-

from selenium import webdriver
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re,json,os


option =  webdriver.ChromeOptions()
option.add_argument('headless')
#driver = webdriver.Chrome(chrome_options=option)
driver = webdriver.Chrome()

for imgNO in range(219,225):
    driver.get("https://www.google.com/imghp?hl=en&tab=wi")
    time.sleep(1)
    driver.find_element_by_class_name("gsst_e").click()
    driver.find_element_by_xpath('//*[@id="qbug"]/div/a').click()
    driver.find_element_by_class_name("qbtbp")
    upload = driver.find_element_by_xpath('//*[@id="qbfile"]')



    try:
        upload.send_keys("C:\\Users\Administrator\Desktop\国旗\\" + str(imgNO) + ".png")
    except:
        continue
    else:
        sreach_window = driver.current_window_handle  # 页面重定位
        bs = BeautifulSoup(driver.page_source, 'html.parser').find_all('div', {'class': 'r5a77d'})
        bsimg = str(imgNO) + "NotFound"
        for i in bs:
            bsimg = i.find('a').text
            bsimg = bsimg.replace('/',' ')
            bsimg = bsimg.replace('-','')
            bsimg = bsimg.replace('"','')
            bsimg = bsimg.replace(':', '')
        old = 'C:\\Users\Administrator\Desktop\国旗\\' + str(imgNO) + '.png'
        new = 'C:\\Users\Administrator\Desktop\国旗\\' + str(bsimg) + '.png'
        try:
            os.rename(old,new)
        except:
            new = 'C:\\Users\Administrator\Desktop\国旗\\' + str(bsimg) + '(' + str(imgNO)+ ')' + '.png'
            os.rename(old, new)
    driver.close