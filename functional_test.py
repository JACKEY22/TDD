# vi functional_test.py
# Chrome Version 87.0.4280.66 (Official Build) (64-bit)
from selenium import webdriver

browser = webdriver.Chrome(executable_path='./chromedriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title

