from os import truncate
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

USERNAME = ""
PASSWORD = ""

def autoScreening(username, password):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=chrome_options)
    driver.get("https://sfsu.co1.qualtrics.com/jfe/form/SV_cUPMQtMOTr76xjT")

    try:
        WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element_by_xpath('//*[@id="NextButton"]'))
    finally:
        driver.find_element_by_xpath('//*[@id="NextButton"]').click()

    try:
        WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element_by_xpath('//*[@id="username"]'))
    finally:
        emailField = driver.find_element_by_xpath('//*[@id="username"]')
        emailField.send_keys(username)
        passField = driver.find_element_by_xpath('//*[@id="password"]')
        passField.send_keys(password)
        driver.find_element_by_xpath('//*[@id="main"]/div/div/form/div[3]/button').click()

    try:
        WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element_by_xpath('//*[@id="QR~QID108~1"]'))
    finally:
        driver.find_element_by_xpath('//*[@id="QID108-1-label"]').click()
        driver.find_element_by_xpath('//*[@id="NextButton"]').click()

    try:
        WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element_by_xpath('//*[@id="QR~QID3~1"]'))
    finally:
        driver.find_element_by_xpath('//*[@id="QID3-1-label"]').click()
        driver.find_element_by_xpath('//*[@id="NextButton"]').click()

    try:
        WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element_by_xpath('//*[@id="QR~QID4~1"]'))
    finally:
        driver.find_element_by_xpath('//*[@id="QID4-1-label"]').click()
        driver.find_element_by_xpath('//*[@id="NextButton"]').click()

    try:
        WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element_by_xpath('//*[@id="QR~QID6~1"]'))
    finally:
        driver.find_element_by_xpath('//*[@id="QID6-1-label"]').click()
        driver.find_element_by_xpath('//*[@id="NextButton"]').click()

    try:
        WebDriverWait(driver, 5).until(
            lambda driver: driver.find_element_by_xpath('//*[@id="QID14"]/div[3]/div/fieldset/legend/div/div[9]/div[3]/strong'))
    finally:
        driver.find_element_by_xpath('//*[@id="NextButton"]').click()

    driver.quit()

if __name__ == '__main__':
    autoScreening(username=USERNAME, password=PASSWORD)
