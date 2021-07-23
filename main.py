from selenium import webdriver
from pages.home import HomePage
from pages.home import ScheduleChoice

if __name__ == "__main__":
    with webdriver.Chrome('./chromedriver.log') as driver:
        homePage = HomePage(driver)
        homePage.load()
        homePage.city()
        homePage.cine()

        schedule = ScheduleChoice(driver)
        schedule.hours()