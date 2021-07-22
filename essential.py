from selenium import webdriver
from pages.home import HomePage

with webdriver.Chrome('./chromedriver.log') as driver:
    homePage = HomePage(driver)
    homePage.load()
    homePage.city()
    homePage.cine()
        

