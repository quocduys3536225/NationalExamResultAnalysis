from selenium import webdriver
import time
import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import  pandas as pd

from pageObjects.HomePageObjects import TraCuuDiem
from TestData.searchPageData import searchPageData
from utilities.BaseClass import BaseClass
excel = pd.DataFrame()

for str_sbd in range(2047165 , 2057168):
    #tracuu = TraCuuDiem(user_input_sbd="02047165")
    sbd = str("0")+ str(str_sbd)
    #print(sbd)
    tracuu = TraCuuDiem(user_input_sbd=sbd)
    #print("Title is :" + tracuu.display_webname())
    dictionary = {"sbd": sbd}
    cot_diem = tracuu.driver.find_elements(By.CSS_SELECTOR, "tr.table-heading:nth-of-type(2) > td")
    tong_so_mon_thi = len(cot_diem)

    if (tracuu.check_sbd_tontai()):
        for i in range(0, tong_so_mon_thi):
            link_to_diem = "tbody tr td:nth-child(" + str(7+i) + ")"
            #print(link_to_diem)
            dictionary[cot_diem[i].get_attribute('innerHTML')] = tracuu.driver.find_element(By.CSS_SELECTOR , link_to_diem).get_attribute('innerHTML').replace('\n', '')
    tracuu.close_brower()
    #print(dictionary)
    excel = excel.append(dictionary, ignore_index=True )
    excel.to_csv("dataset.csv")
    #print(output)
#print(excel)
