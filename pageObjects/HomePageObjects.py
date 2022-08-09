import inspect
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium import webdriver
from utilities.BaseClass import BaseClass

class TraCuuDiem(BaseClass):
    def __init__(self,user_input_sbd):
        BaseClass.__init__(self)
        self.user_input_sbd = user_input_sbd
        webpage = "https://thanhnien.vn/giao-duc/tuyen-sinh/2022/tra-cuu-diem-thi-thpt-quoc-gia.html#"+str(self.user_input_sbd)
        print(webpage)
        self.driver.get(webpage)
        print("Load Website complete")

    diemSinh = (By.CSS_SELECTOR, ("tbody tr td:nth-child(11)"))
    field_sbd = (By.CSS_SELECTOR, ("#txtkeyword"))
    displayed_sbd = (By.CSS_SELECTOR, ("tbody tr td:nth-child(4)"))

    def display_webname(self):
        return self.driver.title

    def check_sbd_tontai(self):
        if int(len(self.driver.find_elements(*TraCuuDiem.displayed_sbd))) ==int(0):
            return 0 #not valid sbd
        elif self.user_input_sbd in self.sbd_thisinh_found():
            return 1
        else:
            return 0 #not valid sbd

    def enter_sbd(self):
        return self.driver.find_element(*TraCuuDiem.field_sbd).send_keys(self.user_input_sbd)

    def sbd_thisinh_found(self):
        return self.driver.find_element(*TraCuuDiem.displayed_sbd).get_attribute('innerHTML')

    def TimKiem(self):
        return self.driver.find_element(By.LINK_TEXT, "Tìm kiếm").click()

    def access_DiemSinh(self):
        return self.driver.find_element(*TraCuuDiem.diemSinh).get_attribute('innerHTML')

    def access_DiemSinh(self):
        return self.driver.find_element(*TraCuuDiem.diemSinh).get_attribute('innerHTML')
