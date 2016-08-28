from selenium import webdriver
import os

os.environ['SELENIUM_SERVER_JAR'] = '/Users/changyi/projects/eclipse-workspace/tdd-python/support/selenium-server-standalone-3.0.0-beta2.jar'

browser = webdriver.Safari()
browser.get('http://localhost:8000')

assert 'Django' in browser.title