from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

def test_webshop():
    driver.get("http://localhost:1667/#/")

    sign_in = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
    sign_in.click()

    email = driver.find_element_by_xpath('//input[@placeholder="Email"]')
    email.send_keys("omegauser@yahoo.com")

    password = driver.find_element_by_xpath('//input[@placeholder="Password"]')
    password.send_keys("om62EG#>")

    sign_in_button = driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    sign_in_button.click()
    time.sleep(3)

    assert driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[4]/a').text == "Omegauser"

    driver.close()