from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import uuid


class Selenium:
    driver = None

    def __init__(self):
        pass

    def init_driver(self):
        mobile_emulation = {
            "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 3.0},
            "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
        }
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option(
            "mobileEmulation", mobile_emulation)

        driver = webdriver.Chrome(options=chrome_options)
        driver.get('website_url')
        self.driver = driver

    def close_drive(self):
        self.driver.quit()
        self.driver = None

    def find_and_wait(self, css_selector):
        wait = WebDriverWait(self.driver, 40)
        element = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, css_selector)))
        return element

    def wait_until_visible(self, css_selector):
        while(self.find_and_wait(css_selector) == None):
            time.sleep(5)
            pass

    def click(self, css_selector):
        button = self.find_and_wait(css_selector)
        print(button)
        button.click()

    def context_click(self, css_selector):
        button = self.find_and_wait(css_selector)
        ActionChains(self.driver).move_to_element(button).perform()
        ActionChains(self.driver).context_click(button).perform()

    def submit(self, css_selector):
        form = self.find_and_wait(css_selector)
        form.submit()

    def send_keys(self, css_selector, value):
        inputElement = self.find_and_wait(css_selector)
        inputElement.send_keys(value)

