from selenium import webdriver
import os

CHROME_DRIVER_PATH = os.environ.get('CHROME_DRIVER_PATH')

browser = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
browser.get('http://localhost:8000')

assert 'Django' in browser.title

