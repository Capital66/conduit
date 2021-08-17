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

    new_article = driver.find_element_by_xpath('//*[@id="app"]/nav/div/ul/li[2]/a')
    new_article.click()
    time.sleep(2)

    article_title = driver.find_element_by_xpath('//input[@placeholder="Article Title"]')
    article_title.send_keys("Rock")

    this_article = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[2]/input')
    this_article.send_keys('Szoljon a rock')

    article = driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/fieldset/fieldset[3]/textarea')
    article.send_keys('Let There Be Rock')

    tag = driver.find_element_by_xpath('//input[@placeholder="Enter tags"]')
    tag.send_keys('#rock')
    time.sleep(3)

    publish = driver.find_element_by_xpath('//button[@type="submit"]')
    publish.click()

    testuser3 = driver.find_element_by_xpath('//a[@href="#/@testuser3/"]')
    testuser3.click()

    my_articles = driver.find_element_by_xpath('//a[@href="#/@testuser3/"]')
    my_articles.click()

    element = driver.find_element_by_xpath('//a[@href="#/articles/rock"]')
    assert str("rock" in element.get_attribute('href')) == "True"

    driver.close()