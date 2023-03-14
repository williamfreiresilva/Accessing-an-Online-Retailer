from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt

def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_argument("disable-blink-features=AutomationControlled")
  prefs = {"credentials_enable_service": False,
     "profile.password_manager_enabled": False}
  options.add_experimental_option("prefs", prefs)
  options.add_experimental_option("excludeSwitches",["enable-automation"])

  driver = webdriver.Chrome(options=options)
  driver.get("https://titan22.com/account/login?return_url=%2Faccount")
  return driver

def main():
  driver = get_driver()
  driver.find_element(by="id",value="CustomerEmail").send_keys("<your-email")
  time.sleep(2)
  driver.find_element(by="id",value="CustomerPassword").send_keys("<your-password" + Keys.RETURN)
  time.sleep(2)
  driver.find_element(by="xpath",value="/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a").click()
  print(driver.current_url)
  
print(main())
