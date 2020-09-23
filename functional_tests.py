from selenium import webdriver
import os
import superlists.settings as settings

CHROME_DRIVER_PATH = os.environ.get('CHROME_DRIVER_PATH')

browser = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
browser.get('http://localhost:8000')

assert 'Django' in browser.title

assert len(settings.SECRET_KEY)>20, settings.SECRET_KEY
