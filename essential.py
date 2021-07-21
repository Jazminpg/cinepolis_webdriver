from selenium import webdriver
from pages.home import HomePage

if __name__ == "__main__":
    with webdriver.Chrome('./chromedriver.log') as driver:
        home = HomePage(driver)
        home.load()
        home.city()
        home.cine()
        

