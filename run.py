from selenium import webdriver
import time

class PhoenixCrawler():
  def __init__(self):
    self.page_num = 10

  def run(self):
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://www.phoenixdesign.com/en/geschichten/luqel/')
    time.sleep(4.0)
    browser.save_screenshot('screenshot{0}.png'.format(0))

    for i in range(self.page_num):
      browser.execute_script("getCurrentSection().scrollTop = getCurrentSection().scrollHeight;")
      element = browser.find_element_by_class_name('luqel-controls-next')
      element.click()
      time.sleep(5.0)
      browser.save_screenshot('screenshot{0}.png'.format(i+1))
      attribute = browser.find_element_by_id('luqel-footer').get_attribute("class")
      if "luqel-preview" in attribute:
        break

PhoenixCrawler().run()
