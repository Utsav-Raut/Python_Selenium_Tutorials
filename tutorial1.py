import pytest
import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from time import sleep

def test_lambdatest_todo_app():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    
    chrome_driver = webdriver.Chrome(chrome_options=options, executable_path=r"D:\Programming\libraries\chromedriver.exe")

    chrome_driver.get("https://lambdatest.github.io/sample-todo-app/")
    chrome_driver.maximize_window()

    chrome_driver.find_element_by_name('li1').click()
    chrome_driver.find_element_by_name('li2').click()

    print(chrome_driver.title)
    page_title = 'Sample page - lambdatest.com'
    assert page_title == chrome_driver.title

    sample_txt = "Hi! Welcome to Easter Island!!"
    text_field = chrome_driver.find_element_by_id("sampletodotext")
    text_field.send_keys(sample_txt)

    sleep(5)

    chrome_driver.find_element_by_xpath("//input[@type='submit']").click()

    sleep(5)

    output_str = chrome_driver.find_element_by_name("li6").text
    sys.stderr.write(output_str)

    sleep(4)

    chrome_driver.close()


