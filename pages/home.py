from selenium.webdriver.common.by import By
from touches.randoms import randomSelectChoice
from selenium.webdriver import ActionChains

from random import randint

class HomePage:
    URL = 'https://cinepolis.com/'
    CITIES = (By.CSS_SELECTOR, '#cmbCiudades')
    CINES = (By.CSS_SELECTOR, '#cmbComplejos')

    def __init__(self, driver):
        self.driver = driver
    def load(self):
        self.driver.get(self.URL)
    def city(self):
        randomSelectChoice(self.driver, self.CITIES)
    def cine(self):
        randomSelectChoice(self.driver, self.CINES)

class ScheduleChoice:

    def __init__(self, driver):
        self.driver = driver
    def hours(self):
        SLIDERS = self.driver.find_elements_by_css_selector('a[class="ui-slider-handle ui-state-default ui-corner-all"]')
        print('found slider_Hour')
        slider_1 = SLIDERS[0]
        slider_2 = SLIDERS[1]
        target = self.driver.find_elements_by_css_selector('span[class*=ui-slider-pip]')
        random_1 = randint(1, len(target)-1)
        random_target_1 = target[random_1]
        ActionChains(self.driver).drag_and_drop(slider_1, random_target_1).perform()

        random_2 = random_1 + randint(1, (len(target)-1 - random_1))
        random_target_2 = target[random_2]
        ActionChains(self.driver).drag_and_drop(slider_2, random_target_2).perform()


        

