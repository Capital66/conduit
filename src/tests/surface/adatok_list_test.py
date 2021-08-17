from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
import time

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

def test_webshop():
    driver.get("http://localhost:1667/#/")

    sign_in = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
    sign_in.click()

    email = driver.find_element_by_xpath('//input[@placeholder="Email"]')
    email.send_keys("testuser3@example.com")

    password = driver.find_element_by_xpath('//input[@placeholder="Password"]')
    password.send_keys("Abcd123$")

    sign_in_button = driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    sign_in_button.click()
    time.sleep(3)

    global_feed_button = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[1]/ul/li[2]/a')
    global_feed_button.click()

    elements = driver.find_elements_by_class_name('preview-link')

    with open ("input.txt", "w") as file:
        for element in elements:
            file.write(str(element.get_attribute('href')) + "\n")

    with open("input.txt", "r") as file2:
        result = file2.readlines()

    assert len(elements) == len(result)

    driver.close()