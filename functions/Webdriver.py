import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def conectar():
    dir_path = os.getcwd()
    profile = os.path.join(dir_path, "profile", "wpp")
    options = webdriver.ChromeOptions()
    options.add_argument(r"user-data-dir={}".format(profile))

    driver = webdriver.Chrome("./chromedriver.exe", chrome_options=options)

    driver.get(f"https://google.com.br/")
    driver.maximize_window()

    #WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[4]/div')))
    #time.sleep(5)
    
    return driver