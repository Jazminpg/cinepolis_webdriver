from selenium import webdriver
from pages.home import HomePage

def OpenandClose():
    driver = webdriver.Chrome('./chromedriver.log')
    homePage = HomePage(driver)
    homePage.load()
    homePage.city()
    homePage.cine()

OpenandClose()

