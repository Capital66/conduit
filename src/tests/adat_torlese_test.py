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

    testuser3 = driver.find_element_by_xpath('//a[@href="#/@testuser3/"]')
    testuser3.click()
    time.sleep(3)

    edit_profile = driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div/div/a')
    edit_profile.click()
    time.sleep(3)

    about = driver.find_element_by_xpath('//textarea[@placeholder="Short bio about you"]')
    about.send_keys('Born: 1966')

    update_button = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/button')
    update_button.click()
    time.sleep(3)

    OK_button = driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]')
    OK_button.click()
    time.sleep(3)

    testuser3.click()
    time.sleep(3)
    edit_profile.click()
    time.sleep(3)
    about.clear()
    time.sleep(3)
    driver.find_element_by_xpath('//input[@placeholder="Your username"]').click()
    time.sleep(3)
    update_button.click()
    time.sleep(3)
    assert driver.find_element_by_class_name('swal-title').text == "Update successful!"

    OK_button = driver.find_element_by_xpath('//button[@class="swal-button swal-button--confirm"]')
    OK_button.click()
    time.sleep(3)
    assert driver.find_element_by_class_name('swal-modal').is_displayed() == False
    assert about.get_attribute('value') == ""

    driver.close()