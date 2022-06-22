import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Abrir(Cursor, Driver, Whatsapp):
    Driver.get(f"https://web.whatsapp.com/send?phone={Whatsapp}")
    WebDriverWait(Driver, 120).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[4]/div')))
    time.sleep(2)
    try:
        Driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div/div').click()
        Cursor.execute(f"UPDATE ``.`` SET `PrimeiroContato` = 'Número Inválido' WHERE (`Whatsapp` = {Whatsapp});")
        
    except:
        pass