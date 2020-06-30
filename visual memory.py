from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from config import Config
from pynput.keyboard import Key, Controller
import time
import pynput
from selenium.common.exceptions import NoSuchElementException


def memory():
    global activeSquares
    driver = webdriver.Chrome()
    keyboard = Controller()
    driver.get("https://www.humanbenchmark.com/tests/memory")
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[4]/div[1]/div/div/div/div[2]/button").click()
    score = 0

    while True:
        try:
            activeSquares = driver.find_elements_by_class_name("active")
        except NoSuchElementException:
            pass
        time.sleep(1)

        for i in range(1, len(activeSquares)):
            activeSquares[i].click()

        if len(activeSquares) == 1:
            score -= 1

        time.sleep(0.1)
        score += 1


memory()
