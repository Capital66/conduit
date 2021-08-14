from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
import time

driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome(ChromeDriverManager().install())

def test_webshop():
    driver.get("http://localhost:1667/#/")

    driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[3]/a').click()

    username = driver.find_element_by_xpath('//input[@placeholder="Username"]')
    username.send_keys("Omegauser")

    email_value = "omegauser@yahoo.com"
    email = driver.find_element_by_xpath('//input[@placeholder="Email"]')
    email.send_keys(email_value)

    password_value = "om62EG#>"
    password = driver.find_element_by_xpath('//input[@placeholder="Password"]')
    password.send_keys(password_value)

    sign_in_button = driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    sign_in_button.click()
    time.sleep(3)

    OK_button = driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]')
    OK_button.click()

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