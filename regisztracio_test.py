from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
import time

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

def test_webshop():
    driver.get("http://localhost:1667/#/")

    sign_up = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[3]/a')
    sign_up.click()

    username = driver.find_element_by_xpath('//input[@placeholder="Username"]')
    username.send_keys("Omegauser")

    email = driver.find_element_by_xpath('//input[@placeholder="Email"]')
    email.send_keys("omegauser@yahoo.com")

    password = driver.find_element_by_xpath('//input[@placeholder="Password"]')
    password.send_keys("om62EG#>")

    sign_in_button = driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary pull-xs-right"]')
    sign_in_button.click()
    time.sleep(3)

    message = driver.find_element_by_class_name('swal-text')
    assert message.text == "Your registration was successful!"

    OK_button = driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]')
    OK_button.click()
    assert driver.find_element_by_class_name('swal-modal').is_displayed() == False

    driver.close()